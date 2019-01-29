
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_user_by_id(id):
	account = session.query(Users).filter_by(id = id).first()
	return account
	
def get_user_by_name(name):
	account = session.query(Users).filter_by(user_name = name).first()
	return account

def get_all_users():
    users = session.query(Users).all()
    return users
	
def add_user(user_name, address, phone_number, password, email):
    code = str(random.randint(1000,10000))

    for i in get_all_users():
        if code == i.code:
            code = str(random.randint(1000,10000))
    account = Users(user_name=user_name, address=address, phone_number=phone_number ,password=password, email = email, code = code)
    session.add(account)
    session.commit()

def check_password(user_name, entered_password):
	account = session.query(Users).filter_by(user_name = user_name).first()
	if account.password == entered_password:
		return True
	else:
		return False

def add_message( msg, img, user_id):
	msg = Posts( message = msg, image = img, likes = 0, dislikes = 0, user_id=user_id)
	session.add(msg)
	session.commit()


# def get_name_from_id(user_id):
# 	users = session.query(Users).filter_by(id=user_id).first()
# 	name = users.user_name
# 	return name



# RECENTLY DELETED CODE : 1
# def get_name_from_id(user_id):
# 	users = session.query(Users).filter_by(id=user_id).first()
# 	name = users.user_name
# 	return name


# def get_addres_from_id(user_id):
# 	users = session.query(Users).filter_by(id=user_id).first()
# 	addres = users.addres
# 	return addres

# def get_phone_from_id(user_id):
# 	users = session.query(Users).filter_by(id=user_id).first()
# 	phone = users.phone_number
# 	return phone

# def get_email_from_id(user_id):
# 	users = session.query(Users).filter_by(id=user_id).first()
# 	email = users.email
# 	return email




def get_all_msgs():
	messages = session.query(Posts).all()
	return messages
	
def likePost(id):
	post = session.query(Posts).filter_by(id = id).first()
	post.likes+=1
	session.commit()

def dislikePost(id):
	post = session.query(Posts).filter_by(id = id).first()
	post.dislikes+=1
	session.commit()	

def get_all_msgs_name(name):
	return session.query(Posts).filter_by(user_name = name).all()


def delete_all_msgs():
	session.query(Posts).delete()
	session.commit()

def delete_all_users():
	session.query(Users).delete()
	session.commit()

