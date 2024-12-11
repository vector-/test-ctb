

answers = {}

form_answers = ["netural", "statisfied", "netural", "netural"]

for ans in form_answers:
    print(f"ans:{ans}")
    if ans in answers:
        answers[ans] += 1
    else:
        answers[ans] = 1  # 

for item in answers:
    print(f"{item}: {answers[item]}")