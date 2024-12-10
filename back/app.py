from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/quiz_result')
def quiz_result():
    
@app.route('/quiz')
def quiz():# 添加測試問題數據
    questions = [
        {
            'no': 1,
            'stem': 'When you feel stressed, do you tend to eat more than usual?'
        },
        {
            'no': 2,
            'stem': 'Do you eat when you are not physically hungry?'
        },
        {
            'no': 3,
            'stem': 'Do you feel guilty after emotional eating?'
        },
        {
            'no': 4,
            'stem': 'Do you turn to food when you feel lonely or bored?'
        },
        {
            'no': 5,
            'stem': 'Do you use food as a way to cope with negative emotions?'
        }
    ]
    return render_template("quiz.html", questions=questions)
if __name__ == '__main__':
    app.run(debug=True, port = 8888)
# from flask import Flask, render_template, request, jsonify
# from collections import defaultdict
# app = Flask(__name__)
# # 儲存答案的字典
# responses = defaultdict(list)
# # 儲存每個問題各選項的計數
# option_counts = defaultdict(lambda: defaultdict(int))
# @app.route('/')
# def home():
#     return render_template("Homepage.html")
# @app.route('/test')
# def test():
#     questions = [
#         {
#             'no': 1,
#             'stem': 'When you feel stressed, do you tend to eat more than usual?'
#         },
#         {
#             'no': 2,
#             'stem': 'Do you eat when you are not physically hungry?'
#         },
#         {
#             'no': 3,
#             'stem': 'Do you feel guilty after emotional eating?'
#         },
#         {
#             'no': 4,
#             'stem': 'Do you turn to food when you feel lonely or bored?'
#         },
#         {
#             'no': 5,
#             'stem': 'Do you use food as a way to cope with negative emotions?'
#         }
#     ]
#     return render_template("Testpage.html", questions=questions)
# @app.route('/submit_answer', methods=['POST'])
# def submit_answer(): 
#     data = request.get_json()
#     question_no = str(data.get('question_no'))  # 確保 question_no 是字符串
#     answer = data.get('answer')
#     # 儲存回答
#     responses[question_no].append(answer)
#     option_counts[question_no][answer] += 1
#     # 計算百分比
#     total_responses = len(responses[question_no])
#     percentages = {}
#     for option in ['overjoyed', 'gratified', 'satisfied', 'neutral', 'disgruntled', 'discontented', 'seething']:
#         count = option_counts[question_no].get(option, 0)
#         percentages[option] = round((count / total_responses) * 100, 1) if total_responses > 0 else 0.0
#     return jsonify({
#         'status': 'success',
#         'percentages': percentages
#     })
# @app.route('/results')
# def results():
#     # 計算所有問題的百分比
#     all_percentages = {}
#     for question_no in responses:
#         total = len(responses[question_no])
#         question_percentages = {}
#         for option, count in option_counts[question_no].items():
#             question_percentages[option] = (count / total) * 100
#         all_percentages[question_no] = question_percentages
#     return render_template("results.html", percentages=all_percentages)
# if __name__ == '__main__':
#     app.run(debug=True, port = 8888)