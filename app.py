from flask import Flask, render_template, request, redirect, url_for, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[
            {"roles": "system", "content": "You are a helpfull skill-learning assistant."},
            {"roles": "user", "content": user_message}
        ]
    )

    ai_reply = response['choices'][0]['message']['content']
    return jsonify({'reply': ai_reply})

@app.route('/')
def home():
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
