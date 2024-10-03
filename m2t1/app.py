from flask import Flask, render_template, request

app = Flask(__name__)

# Global variable to track attempts (this will reset if the server restarts)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global attempts
    feedback = None
    error = None

    if request.method == 'POST':
        full_equation = request.form['full_equation']
        
        try:
            # Split the input to get the equation and the user-provided answer
            equation, user_answer = full_equation.split('=')
            correct_answer = eval(equation.strip())
        except Exception:
            error = "Invalid equation format. Please use 'num1 operation num2 = answer'."
        else:
            # Check the user's answer
            if float(user_answer.strip()) == correct_answer:
                feedback = "✅ Correct!"
                attempts = 0  # Reset attempts on success
            else:
                attempts += 1
                if attempts >= 3:
                    feedback = f"EEE! The correct answer is {correct_answer}."
                    attempts = 0  # Reset attempts after three tries
                else:
                    feedback = f"Incorrect! You have {3 - attempts} tries left."

    return render_template('index.html', feedback=feedback, error=error)

if __name__ == '__main__':
    app.run(debug=True)


