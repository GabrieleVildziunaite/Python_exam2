
from app import app
from flask import render_template, request, redirect, flash, url_for

app.config['SECRET_KEY'] = 'fhadkjhakjfdh'

menu = [{"name": "Split Bill", "url": "/"},
        {"name": "Login", "url": "login"}]

@app.route('/', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        req = request.form

        user = req.get("username")
        email = req.get("email")
        psw = req.get("password")
        psw2 = req.get("password2")

        if not len(psw) >= 8:
            flash('The password must be at least 8 caracters long!')
            return redirect(request.url)
        
        if psw != psw2:
            flash('The passwords does not match. Try again!')
            return redirect(request.url)
        
        flash('User name created', "success")
        return redirect(url_for("login"))
    
    return render_template('public/register.html', title="Split Bill", title2="Register now!", menu=menu) 



@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        req = request.form

        email = req.get("email")
        psw = req.get("password")

        if not len(psw) >= 8:
            flash('Wrong email address or password')
            return redirect(request.url)
        
        flash('Login successfull', "success")
        return redirect("groups")
    
    return render_template('public/login.html', title="Log in page", title2="Log in to your account", menu=menu) 









