import os
from flask import Flask, render_template, redirect, url_for, request, session
from model import db, User, Tip, Category  # Assuming these models are defined in models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Change to your DB URI
app.secret_key = os.getenv('SECRET_KEY', 'fallback_secret_key')  # Fallback for local development
db.init_app(app)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to register user
        pass
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic to login user
        pass
    return render_template('login.html')

@app.route('/tips')
def tips():
    all_tips = Tip.query.all()  # Fetch all tips from the database
    return render_template('tips.html', tips=all_tips)

if __name__ == '__main__':
    app.run(debug=True)



