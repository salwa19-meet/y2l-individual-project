# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session as login_session

# Add functions you need from databases.py to the next line!
from database import *
from model import *
from flask_mail import Message, Mail

# Starting the flask app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf movies'

# App routing code here

@app.route('/home', methods = ['GET','POST'])
def home():
   
    if request.method == 'GET':
        posts = get_all_msgs()
        return render_template('home.html' ,posts=posts,user_name= login_session["username"] ,myfunction = get_user_by_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        accounts = get_all_users()
        is_open = True
        for account in accounts:
            if request.form['user_name'] == account.user_name:
                is_open = False
        if is_open == False:
            print('username already taken!')
        else:
            password = request.form['password']
            confirm = request.form['password-confirm']
            email = request.form['email']
            username = request.form['user_name']
            address = request.form['address']
            phone_number = request.form['phone_number']



            if password == confirm:
                add_user(request.form['user_name'],
                    request.form['address'],
                    request.form['phone_number'],
                    request.form['password'],
                    request.form['email'])
                user = get_user_by_name(username)
                login_session["user_id"] = user.id
                login_session["username"] = user.user_name
                login_session["address"] = user.address
                login_session["email"] = user.email
                login_session["phone_number"] = user.phone_number

                return redirect(url_for('home'))
            else:
                print('password confimation does not match password!')
                return redirect(url_for('register'))

@app.route('/', methods=(['GET' , 'POST']))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        print("trying to login")

        username = request.form['user_name']
        password = request.form['password']
        accounts = get_all_users()
        is_here = False
        for account in accounts:
            if account.user_name == username:
                is_here = True
        if is_here == True:
            if check_password(username,password) == True:
                print("good password")
                user = get_user_by_name(username)
                login_session["user_id"] = user.id
                login_session["username"] = user.user_name
                login_session["address"] = user.address
                login_session["email"] = user.email
                login_session["phone_number"] = user.phone_number

                return redirect(url_for('home'))
            else:
                return(redirect(url_for('login')))
        else:
            return redirect(url_for('login'))

@app.route('/like/<int:id>')
def like(id):
    likePost(id)

@app.route('/dislike/<int:id>')
def dislike(id):
    disLikePost(id)

@app.route('/post', methods=['GET','POST'])
def post():


    if request.method == 'GET':

        return render_template('post.html',user_name= login_session["username"])
    else:
        msg = request.form['message']
        img = request.form['image']
        user_id = login_session['user_id']

        if msg == "" and img == "":
            return render_template(

                "post.html",
                posts = reversed(get_all_msgs()),
                # username = current_username,
                # address = current_address,
                # phone_number = current_phonenumber,
                # email = current_email
               

                )
        else:
            add_message(msg, img, user_id)
            return render_template(

                "post.html",
                posts = reversed(get_all_msgs()),
                # username = current_username
               

                
                
                



                )

@app.route('/profile')
def profile():
     if request.method == 'GET':
        return render_template('profile.html' , posts = get_all_msgs(),user_name=login_session["username"]  ,myfunction = get_user_by_id )

@app.route('/us', methods = ['GET','POST'])
def us():
    if request.method == 'GET':
        return render_template('us.html', myfunction = get_user_by_id,user_name= login_session["username"])



@app.route('/science', methods = ['GET','POST'])
def science():
    if request.method == 'GET':
        return render_template('science.html',posts = get_all_msgs() ,user_name= login_session["username"] ,myfunction = get_user_by_id)





@app.route('/fantasy', methods = ['GET','POST'])
def fantasy():
    if request.method == 'GET':
        return render_template('fantasy.html',posts = get_all_msgs() ,user_name= login_session["username"] ,myfunction = get_user_by_id)






@app.route('/adventure', methods = ['GET','POST'])
def adventure():
    if request.method == 'GET':
        return render_template('adventure.html',posts = get_all_msgs() ,user_name= login_session["username"] ,myfunction = get_user_by_id)







@app.route('/mystery', methods = ['GET','POST'])
def mystery():
    if request.method == 'GET':
        return render_template('mystery.html',posts = get_all_msgs() ,user_name= login_session["username"] ,myfunction = get_user_by_id)







@app.route('/drama', methods = ['GET','POST'])
def drama():
    if request.method == 'GET':
        return render_template('drama.html',posts = get_all_msgs(),user_name= login_session["username"] ,myfunction = get_user_by_id )




@app.route('/comedy', methods = ['GET','POST'])
def comedy():
    if request.method == 'GET':
        return render_template('comedy.html',posts = get_all_msgs() , user_name= login_session["username"] ,myfunction = get_user_by_id)












if __name__ == "__main__":
    app.run(debug=True)