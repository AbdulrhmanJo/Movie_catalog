# Udacity Item Catalog

A web application that provides a list of Movies within a variety of categories.

## set up

1. Clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Put the content of this respository into *catalog* folder that provides in *fullstack-nanodegree-vm*.

3. Launch the Vagrant VM from inside the *vagrant* folder with:

    `vagrant up`

  Then access the shell with:

    `vagrant ssh`

4. Move inside the catalog folder:

    `cd /vagrant/catalog`

5. Then run the database with:

    `python database_setup.py`

6. add some movies by run the seeder with:

    `python seeder.py`

7. Now you can run the application with:

    `python application.py`

    After this the web is ready for you at this URL:

     `http://localhost:8000/`

have fun.
