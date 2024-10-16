from flask import Flask, render_template, request # type: ignore 

import random

app = Flask(__name__)

# Global variable to track attempts (this will reset if the server restarts)
attempts = 0
memory_bank = []  # Memory Bank to store equations

@app.route('/', methods=['GET', 'POST'])
def index():
    global attempts
    feedback = None
    error = None
    current_equation = ""  # This will hold the equation for GO

    if request.method == 'POST':
        full_equation = request.form.get('full_equation', "")

        if 'calculate' in request.form:
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
        
        if 'memory_bank' in request.form:
            # Add the equation to the Memory Bank
            memory_bank.append(full_equation)
            feedback = f"Equation added to Memory Bank: {full_equation}"

        if 'go' in request.form:
            if memory_bank:
                current_equation = random.choice(memory_bank).split('=')[0] + '='  # Get the equation part for practice
            else:
                error = "No equations in Memory Bank."

    return render_template('index.html', feedback=feedback, error=error, memory_bank=memory_bank, current_equation=current_equation)

if __name__ == '__main__':
    app.run(debug=True)



