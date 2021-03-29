""" DB modules """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ DB storage class """
    __classes = [State, City, Place,
                 User, Amenity, Review]
    __var_env = {
        'HBNB_MYSQL_USER': os.getenv('HBNB_MYSQL_USER'),
        'HBNB_MYSQL_PWD': os.getenv('HBNB_MYSQL_PWD'),
        'HBNB_MYSQL_HOST': os.getenv('HBNB_MYSQL_HOST'),
        'HBNB_MYSQL_DB': os.getenv('HBNB_MYSQL_DB')
    }
    __engine = None
    __session = None

    def __init__(self):
        self.engine = self.__var_env

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, en_var):
        user = en_var['HBNB_MYSQL_USER']
        password = en_var['HBNB_MYSQL_PWD']
        dataBase = en_var['HBNB_MYSQL_DB']
        host = en_var['HBNB_MYSQL_HOST']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              password,
                                              host,
                                              dataBase),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        result = {}
        if cls in self.__classes:
            rows = self.__session.query(cls).all()

            for obj in rows:
                key_name = cls.__name__ + '.' + obj.id
                result[key_name] = obj

        elif not cls:
            for class_name in self.__classes:
                rows = self.__session.query(class_name).all()

                for obj in rows:
                    key_name = class_name.__name__ + '.' + obj.id
                    result[key_name] = obj
        return result

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        try:  # try to find obj using eval className
            className = eval(obj.__class__.__name__)
            res = self.__session \
                .query(className) \
                .filter(className.id == obj.id) \
                .one_or_none()

            print('from db res = ', res)
            if res:  # delete from db
                self.__session.delete(res)
                self.__session.commit()
        except Exception:
            # todo: delete line below
            raise Exception

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        self.__session = scoped_session(session_factory)
