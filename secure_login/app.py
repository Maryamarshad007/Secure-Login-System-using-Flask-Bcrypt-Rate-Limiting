from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Use a strong key in production

bcrypt = Bcrypt(app)
limiter = Limiter(app, key_func=get_remote_address)

# Simulated user database
users = {}

@app.route('/')
def home():
    if 'username' in session:
        return render_template("home.html", username=session['username'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists!', 'danger')
        else:
            hashed = bcrypt.generate_password_hash(password).decode('utf-8')
            users[username] = hashed
            flash('User registered successfully!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

# Brute-force protection: max 5 login attempts per minute per IP
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = users.get(username)
        if hashed_password and bcrypt.check_password_hash(hashed_password, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
