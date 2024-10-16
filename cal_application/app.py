from flask import Flask, render_template, request, redirect, url_for # type: ignore
import random

app = Flask(__name__)

# Memory bank for storing equations per user (keyed by username)
memory_banks = {}
current_users = {}  # Store current logged in users

@app.route('/')
def index():
    if 'username' in current_users:
        return render_template('index.html', username=current_users['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        current_users['username'] = username

        # Initialize user's memory bank if not present
        if username not in memory_banks:
            memory_banks[username] = []
        
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    current_users.pop('username', None)
    return redirect(url_for('login'))

@app.route('/save_to_memory', methods=['POST'])
def save_to_memory():
    if 'username' in current_users:
        equation = request.form['equation']
        username = current_users['username']
        memory_banks[username].append(equation)
        return 'BANKED'
    return 'You need to log in first!', 403

@app.route('/go', methods=['GET'])
def go():
    if 'username' in current_users:
        username = current_users['username']
        if memory_banks[username]:
            equation = random.choice(memory_banks[username])
            return equation
        return 'No equations in memory bank'
    return 'You need to log in first!', 403

if __name__ == '__main__':
    app.run(debug=True)


