from flask import Flask, render_template, jsonify, request
import yaml
#akaishuichi#

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = yaml.safe_load(file)
    return questions


app = Flask(__name__)
@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/test')
def test():# 添加測試問題數據
    questions = load_questions('quiz.yaml')
    return render_template("Quiz.html", questions=questions)


def calculate(choices):
    total_questions = len(choices)
    choice_count = {}
    for choice in choices:
        if choice in choice_count:
            choice_count[choice] += 1
        else:
            choice_count[choice] = 1
    percentages = {choice: (count / total_questions) * 100 for choice, count in choice_count.items()}
    return jsonify(percentages)


@app.route('/submit', methods=['POST'])
def submit():
    choices = request.json.get('choices', [])
    return calculate(choices)


if __name__ == '__main__':
    app.run(debug=True, port = 8888)