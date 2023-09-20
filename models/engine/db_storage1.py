#!/usr/bin/python3
"""
This module defines the DBStorage class
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Stores data in the MySQL database server
    """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        fmt = 'mysql+mysqldb://{}:{}@{}/{}'
        db_url = fmt.format(user, passwd, host, db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Queries the current database session (self.__session) for
            all arguments depending on the class name (argument cls)
        """
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            rs = self.__session.query(cls)
            for item in rs:
                key = "{}.{}".format(item.__class__.__name__, item.id)
                dictionary[key] = item
        else:
            all_cls = [State, City, User, Place, Review, Amenity]
            for _cls in all_cls:
                rs = self.__session.query(_cls)
                for item in rs:
                    key = "{}.{}".format(item.__class__.__name__, item.id)
                    dictionary[key] = item

        return dictionary

    def new(self, obj):
        """adds the new object to the current database session
            (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database
            session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            Create all tables in the database, all classes which inherits
            from Base must be imported before calling
            Base.metadata.create_all(engine)

            Creates the current database session (self.__session) from the
            engine (self.__engine) by using a sessionmaker - the option
            expire_on_commit must be set to False; and scoped_session-to
            make sure yout Session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session_scope = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_scope)
        self.__session = Session()

    def close(self):
        """ Closes a session
        """
        self.__session.close()
