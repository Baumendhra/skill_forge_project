from flask import Flask, render_template, request, redirect, url_for,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

# Route for chatbot backend (handling user message)
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json['message']

    # Simple Bot logic (You can make this smarter later)
    if "web development" in user_message.lower():
        bot_response = "Web Development includes HTML, CSS, JS, and frameworks like React."
    elif "data science" in user_message.lower():
        bot_response = "Data Science covers Python, Machine Learning, and Data Analysis!"
    else:
        bot_response = "Sorry, I am still learning. Please ask about skills!"

    return jsonify({"response": bot_response})


@app.route('/')
def home_1():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/literacy')
def literacy():
    return render_template('literacy.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        answers = {
            "q1": "b",
            "q2": "a",
            "q3": "c"
        }
        for question, correct in answers.items():
            if request.form.get(question) == correct:
                score += 1
        return redirect(url_for('result', score=score))
    return render_template('quiz.html')

@app.route('/result')
def result():
    score = request.args.get('score')
    return render_template('result.html', score=score)

@app.route('/certificate')
def certificate():
    return render_template('certificate.html')

@app.route('/chat-ui')
def chat_ui():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(debug=True)
