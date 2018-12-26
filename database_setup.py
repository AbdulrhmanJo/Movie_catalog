from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    cover = Column(String(240), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class CategoryItem(Base):
    __tablename__ = 'category_item'

    name = Column(String(90), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    directorName = Column(String(250), nullable=False)
    coverUrl = Column(String(450), nullable=False)
    trailer = Column(String(450), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'director': self.directorName,
            'genre': self.category.serialize,
            'coverUrl': self.coverUrl,
            'trailer': self.trailer,
            'description': self.description
        }


engine = create_engine('sqlite:///MovieCatalog.db')
Base.metadata.create_all(engine)
