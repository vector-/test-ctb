from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import yaml
import random
QUIZ_FILE = 'quiz.yaml'
PASS_FILE = 'passwd.yaml'
HIST_FILE = 'hist.yaml'

def load_questions(filename):
    with open(filename, 'r') as file:
        all_questions = yaml.safe_load(file)
        # 隨機選擇30個問題
        selected_questions = random.sample(all_questions, 30)
        # 重新編號選中的問題
        for i, question in enumerate(selected_questions, 1):
            question['number'] = i
    return selected_questions

def load_passwords(filename):
    with open(filename, 'r') as file:
        passwords = yaml.safe_load(file)
    return passwords

def save_passwords(filename, passwords):
    with open(filename, 'w') as file:
        yaml.dump(passwords, file, default_flow_style=False)

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


app = Flask(__name__)
passwords=load_passwords(PASS_FILE)

team_members = [
    {
        "name": "Suzie Jing",
        "title": "Team Leader",
        "image": "///"
    },
    {
        "name": "Evelyn Zhang",
        "title": "Web front-end developer",
        "image": "///"
    },
    {
        "name": "Peter Sun",
        "title": "Web back-end developer",
        "image": "///"
    },
    {
        "name": "Joanna Yang",
        "title": "Problem Designer",
        "image": "///"
    },
    {
        "name": "Sophia Sun",
        "title": "Data integrator",
        "image": "lisa.jpg"
    },
    {
        "name": "Seven Shao",
        "title": "Data Analyst",
        "image": "///"
    },
    {
        "name": "Zhou",
        "title": "Context Writer",
        "image": "///"
    }
]

@app.route('/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username, team_members=team_members)


@app.route('/test')
def test():# 添加測試問題數據
    questions = load_questions(QUIZ_FILE)
    return render_template("Quiz.html", questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    choices = request.json.get('choices', [])
    return calculate(choices)


@app.route('/login', methods=['POST','GET'])
def login():
    return render_template("login.html", signup=True)


# route for signup
@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    pass1 = request.form.get('password')
    pass2 = request.form.get('checking_password')

    if pass1 == pass2:
        passwords.append({'name':username, 'pass': pass1})
        save_passwords(PASS_FILE, passwords)
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
    for user in passwords:
        if user['name'] == username:
            if user['pass'] == password:
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return render_template("login.html", error = "Wrong password")
    return render_template("login.html", error = "User does not exist")
    # TODO validate the password for the user
    # hint: compare password with the one stored inside the password file
    # passwords contains all users and passwords, you need to
    # loop/traverse遍历 the passwords to find the name matched with 
    # the variable 'username', then compare 'pass' in the dict 
    # and the variable 'password'
    # TODO decide the page being redirected to
if __name__ == '__main__':
    app.run(debug=True, port = 8888)