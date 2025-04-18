Secure Login System using Flask + Bcrypt + Rate Limiting
This is a basic login system made using Flask. It uses Bcrypt to hash passwords and has simple rate limiting to help prevent brute-force login attempts.

# What It Does
1 Lets users sign up and log in securely
2 Passwords are hashed using Bcrypt
3 Adds basic session handling with Flask
4 Uses rate limiting to block too many failed login attempts
5 Protects against basic brute-force attacks

# How to Run
1. Make sure Python is installed
2. Install required libraries:
pip install flask flask-bcrypt flask-limiter
3. Save the file as `app.py`
4. Run the app:
python app.py
5. Open your browser and go to:
http://127.0.0.1:5000

# Features
  1 Secure password hashing
  2 Login & signup forms
  3 Rate limiting (e.g. max 5 login tries per minute)
  4 In-memory user storage (can be extended to database)
 
# Example Output
After running, the browser shows a login page like:
[ Login Form ]
Username: ______ Password: ______ [Login]
If too many wrong attempts:
"Too many login attempts. Please try again later."

# Notes
1 This project is for practice and learning only.
2 You can improve it by adding a database, email verification, and CSRF protection.
