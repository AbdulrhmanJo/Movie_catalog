
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, CategoryItem, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from sqlalchemy.pool import SingletonThreadPool


app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"


# Connect to Database and create database session
engine = create_engine('sqlite:///MovieCatalog.db?check_same_thread=false', poolclass=SingletonThreadPool)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
     # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # See if a user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    if access_token is None:
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['access_token']
            del login_session['gplus_id']
            del login_session['username']
            del login_session['email']
            del login_session['picture']
            #del login_session['gplus_id']
            #del login_session['access_token']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCategories'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCategories'))


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

#routing
@app.route('/')
@app.route('/category')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html', categories = categories)


@app.route('/category/<path:category_name>/')
@app.route('/category/<path:category_name>/movies/')
def showCategoryMovies(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(category = category).all()
    creator = getUserInfo(category.user_id)
    return render_template('CategoryMovies.html', items =items, category = category, creator= creator)


@app.route('/category/<path:category_name>/movies/<path:item_name>')
def showMovie(category_name,item_name):
    item = session.query(CategoryItem).filter_by(name = item_name).one()
    return render_template('movie.html', item =item)


@app.route('/category/<path:category_name>/movies/new/', methods=['GET', 'POST'])
def newCategoryItem(category_name):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        newMovie = CategoryItem(name=request.form['name'],
            description=request.form['description'],
            directorName=request.form['directorName'],
            coverUrl=request.form['coverUrl'],
            trailer=request.form['trailer'],
            category=category,
            user_id=login_session['user_id'])
        flash('Successfully Added!')
        session.add(newMovie)
        session.commit()
        return redirect(url_for('showCategoryMovies', category_name=category_name))
    else:
        return render_template('addItem.html', category_name=category_name)


@app.route('/category/<path:category_name>/movies/<path:item_name>/delete', methods=['GET', 'POST'])
def deleteCategoryItem(category_name,item_name):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(CategoryItem).filter_by(name=item_name).one()
    creator = getUserInfo(item.user_id)
    if creator.id != login_session['user_id']:
        flash ("You cannot delete this Movie. This item belongs to %s" % creator.name)
        return redirect(url_for('showMovie', category_name = category.name, item_name= item.name))
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash('Successfully Deleted!')
        return redirect(url_for('showCategoryMovies', category_name=category.name))
    else:
        return render_template('deleteItem.html', item=item)


@app.route('/category/<path:category_name>/movies/<path:item_name>/edit', methods=['GET', 'POST'])
def editCategoryItem(category_name,item_name):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    category = session.query(Category).filter_by(name=category_name).one()
    Item = session.query(CategoryItem).filter_by(name=item_name).one()
    creator = getUserInfo(Item.user_id)
    if creator.id != login_session['user_id']:
        flash ("You cannot edit this Movie. This item belongs to %s" % creator.name)
        return redirect(url_for('showMovie', category_name = category.name, item_name= Item.name))
    if request.method == 'POST':
        if request.form['name']:
            Item.name = request.form['name']
        if request.form['description']:
            Item.description = request.form['description']
        if request.form['directorName']:
            Item.directorName = request.form['directorName']
        if request.form['coverUrl']:
            Item.coverUrl = request.form['coverUrl']
        if request.form['trailer']:
            Item.trailer = request.form['trailer']
        flash('Successfully Edited!')
        session.add(Item)
        session.commit()
        return redirect(url_for('showMovie', category_name=category.name, item_name= Item.name))
    else:
        return render_template('editItem.html', category_name=category.name, item=Item)


#JSON
@app.route('/category/JSON')
def showCategoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories = [category.serialize for category in categories])


@app.route('/category/<path:category_name>/JSON')
@app.route('/category/<path:category_name>/movies/JSON')
def showCategoryMoviesJSON(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(category_id = category.id).all()
    return jsonify(items = [item.serialize for item in items])


@app.route('/category/<path:category_name>/movies/<path:item_name>/JSON')
def showMovieJSON(category_name,item_name):
    item = session.query(CategoryItem).filter_by(name = item_name).one()
    return jsonify(item = [item.serialize])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
