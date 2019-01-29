from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Place your database schema code here

# Example code:
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    user_name = Column(String)
    password = Column(String)
    address = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    code = Column(String)

    def __repr__(self):
        return ("User Name: {},adress: {},phone number: {}, Password: {}, Email: {}".format(self.user_name, self.adress, self.phone_number, self.password, self.email))

class Posts(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key = True)
    user_id = Column(String)
    message = Column(String)
    image = Column(String)
    likes = Column(Integer)
    dislikes = Column(Integer)

   
    

    def __repr__(self):
        return ("Name: {}, address: {}, message: {}".format(self.user_name, self.message))


