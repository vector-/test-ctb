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


@app.route('/login', methods=['POST','GET'])
def login():
    return render_template("login.html", signup=True)


# route for signup
# TODO define a route handler for signup
@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    pass1 = request.form.get('password')
    pass2 = request.form.get('checking_password')

    if pass1 == pass2:
        # TODO write user name and password into a password file
        return render_template("home.html", username=username)
    else:
        return jsonify(
            {
                'code': -1,
                'message': 'Error: Two passwords are not same.'
            })


# route for login
@app.route('/login_submit', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"{username}--------{password}")
    # TODO validate the password for the user
    # hint: compare password with the one stored inside the password file


    # TODO decide the page being redirected to
    return jsonify({'message': 'submited ok'})

if __name__ == '__main__':
    app.run(debug=True, port = 8888)