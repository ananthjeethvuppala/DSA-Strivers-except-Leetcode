keywords = ['break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var']
s = input().strip()
if s in keywords:
    print(s,'is a keyword')
else:
    print(s,'is not a keyword')