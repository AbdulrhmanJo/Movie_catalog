from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///MovieCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Abdulrhman", email="Abdulrhman@udacity.com",
             picture='https://image.flaticon.com/icons/png/512/149/149071.png')
session.add(User1)
session.commit()

# Items for Comedy
category1 = Category(name="Comedy", cover="http://innov8tiv.com/wp-content/uploads/2018/08/Best-Comedy-Movies-of-2018-2.jpg",user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Dumplin'",
                    description="Willowdean ('Dumplin'), the plus-size teenage daughter of a former beauty queen, signs up for her mom's Miss Teen Bluebonnet pageant as a protest that escalates when other contestants follow her footsteps, revolutionizing the pageant and their small Texas town.",
                    directorName="Anne Fletcher",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMDMyNzQyMjgtZTM2NS00ZjQwLThjYTMtZDlhOTNhNTMzNTkwXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category1, user_id=1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Mary Poppins Returns",
                    description="Decades after her original visit, the magical nanny returns to help the Banks siblings and Michael's children through a difficult time in their lives.",
                    directorName="Rob Marshall",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjM0MjEzOTQ1NF5BMl5BanBnXkFtZTgwODg4ODc5NjM@._V1_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category1, user_id=1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Home Alone",
                    description="An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.",
                    directorName="Chris Columbus",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMzFkM2YwOTQtYzk2Mi00N2VlLWE3NTItN2YwNDg1YmY0ZDNmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,672,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category1, user_id=1)

session.add(item3)
session.commit()


# Items for action
category2 = Category(name="Action", cover="https://img4.looper.com/img/gallery/how-john-wick-changed-action-movies-and-no-one-noticed/humor-and-self-awareness-1525449768.jpg",user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Aquaman",
                    description="Arthur Curry learns that he is the heir to the underwater kingdom of Atlantis, and must step forward to lead his people and be a hero to the world.",
                    directorName="James Wan",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BOTk5ODg0OTU5M15BMl5BanBnXkFtZTgwMDQ3MDY3NjM@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category2, user_id=1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Avengers: Infinity War",
                    description="The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
                    directorName="Anthony Russo, Joe Russo",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category2, user_id=1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Ready Player One",
                    description="When the creator of a virtual reality world called the OASIS dies, he releases a video in which he challenges all OASIS users to find his Easter Egg, which will give the finder his fortune.",
                    directorName="Steven Spielberg",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category2, user_id=1)

session.add(item3)
session.commit()


# Items for Romance
category3 = Category(name="Romance", cover="https://s4.scoopwhoop.com/anj/sw/602c1731-c52a-40d4-96ba-d00841afcf1c.jpg",user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="A Star Is Born",
                    description="A musician helps a young singer find fame, even as age and alcoholism send his own career into a downward spiral.",
                    directorName="Bradley Cooper",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjE3MDQ0MTA3M15BMl5BanBnXkFtZTgwMDMwNDY2NTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category3, user_id=1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Shape of Water",
                    description="At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity.",
                    directorName="Guillermo del Toro",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BNGNiNWQ5M2MtNGI0OC00MDA2LWI5NzEtMmZiYjVjMDEyOWYzXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category3, user_id=1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="The Great Gatsby",
                    description="A writer and wall street trader, Nick, finds himself drawn to the past and lifestyle of his millionaire neighbor, Jay Gatsby.",
                    directorName="Baz Luhrmann",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMTkxNTk1ODcxNl5BMl5BanBnXkFtZTcwMDI1OTMzOQ@@._V1_SY1000_SX666_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category3, user_id=1)

session.add(item3)
session.commit()


# Items for Drama
category4 = Category(name="Drama", cover="http://d1lofqbqbj927c.cloudfront.net/GT-exitos/2017/11/06113309/image-w1280.jpg",user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="The Fault in Our Stars",
                    description="Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.",
                    directorName="Josh Boone",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjA4NzkxNzc5Ml5BMl5BanBnXkFtZTgwNzQ3OTMxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category4, user_id=1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Greatest Showman",
                    description="Celebrates the birth of show business and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.",
                    directorName="Michael Gracey",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjI1NDYzNzY2Ml5BMl5BanBnXkFtZTgwODQwODczNTM@._V1_SY1000_CR0,0,684,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category4, user_id=1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Ben Is Back",
                    description="A drug addicted teenage boy shows up unexpectedly at his family's home on Christmas Eve.",
                    directorName="Peter Hedges",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BZGY3ZWMyYjEtMDMzYi00NDQyLWE1MWEtMDNmMjRlOGVkNDc3XkEyXkFqcGdeQXVyODAzODU1NDQ@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category4, user_id=1)

session.add(item3)
session.commit()


# Items for Horror
category5 = Category(name="Horror", cover="http://ocdn.eu/images/pulscms/ZTM7MDA_/1bbbea73f06f6e9adce13a3338532265.jpeg",user_id=1)

session.add(category5)
session.commit()

item1 = CategoryItem(name="The Nun",
                    description="A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.",
                    directorName="Corin Hardy",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjM3NzQ5NDcxOF5BMl5BanBnXkFtZTgwNzM4MTQ5NTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category5, user_id=1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Halloween",
                    description="Laurie Strode confronts her long-time foe Michael Myers, the masked figure who has haunted her since she narrowly escaped his killing spree on Halloween night four decades ago.",
                    directorName="David Gordon Green",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMmMzNjJhYjUtNzFkZi00MWQ4LWJiMDEtYWM0NTAzNGZjMTI3XkEyXkFqcGdeQXVyOTE2OTMwNDk@._V1_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category5, user_id=1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="A Quiet Place",
                    description="In a post-apocalyptic world, a family is forced to live in silence while hiding from monsters with ultra-sensitive hearing.",
                    directorName="John Krasinski",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category5, user_id=1)

session.add(item3)
session.commit()


# Items for Adventure
category6 = Category(name="Adventure",cover="http://assets.signature-reads.com/wp-content/uploads/2015/12/chris-hemsworth-in-the-heart-of-the-sea.jpg" ,user_id=1)

session.add(category6)
session.commit()

item1 = CategoryItem(name="Interstellar",
                    description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                    directorName="Christopher Nolan",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category6, user_id=1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Christopher Robin",
                    description="A working-class family man, Christopher Robin, encounters his childhood friend Winnie-the-Pooh, who helps him to rediscover the joys of life.",
                    directorName="Marc Forster",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjAzOTM2OTAyNF5BMl5BanBnXkFtZTgwNTg5ODg1NTM@._V1_SY1000_SX675_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category6, user_id=1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Inception",
                    description="A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                    directorName="Christopher Nolan",
                    coverUrl='https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                    trailer='https://www.youtube.com/watch?v=WDkg3h8PCVU',
                    category=category6, user_id=1)

session.add(item3)
session.commit()

print "added Movies!"
