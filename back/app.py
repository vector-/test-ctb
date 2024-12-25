from flask import Flask, render_template, jsonify, request, session
import yaml
##

QUIZ_FILE = 'quiz.yaml'
PASS_FILE = 'passwd.yaml'
HIST_FILE = 'hist.yaml'

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = yaml.safe_load(file)
    return questions

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
app.secret_key = 'your_secret_key_here'

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
# TODO define a route handler for signup
@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    pass1 = request.form.get('password')
    pass2 = request.form.get('checking_password')

    if pass1 == pass2:
        passwords.append({'name':username, 'pass': pass1})
        save_passwords(PASS_FILE, passwords)
        session['username'] = username
        return render_template("home.html", username=username, team_members=team_members)
    else:
        return jsonify({
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
        if user['name'] == username and user['pass'] == password:
            session['username'] = username  # 添加这行：登录成功后存储用户名到session
            return jsonify({'success': True, 'message': 'Login successful'})
    
    return jsonify({'success': False, 'message': 'Invalid username or password'})
  # TODO validate the password for the user
    # hint: compare password with the one stored inside the password file
    # passwords contains all users and passwords, you need to
    # loop/traverse遍历 the passwords to find the name matched with 
    # the variable 'username', then compare 'pass' in the dict 
    # and the variable 'password'

    # TODO decide the page being redirected to
    return jsonify({'message': 'submited ok'})
if __name__ == '__main__':
    app.run(debug=True, port = 8888)