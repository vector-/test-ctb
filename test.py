
def f(arg1, arg2):
    # print(f"arg1:{arg1}, arg2:{arg2}")
    passwords.append({'name':arg1, 'pass': arg2})
    return arg1+arg2

passwords=[{
    'name':'first', 
    'pass': 'ppp'
    }]

arg1=1
arg2=2

a = f(arg1=arg1, arg2=arg2)

print(f"passwords:{passwords}")
