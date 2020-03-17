def isvalid(s):
    a = []
    o = ['(', '[', '{']
    for i in range(len(s)):
        if s[i] in o:
            a.append(s[i])
        else:
            p = a[len(a) - 1]
            if s[i] == ')' and p != '(':
                return False
            if s[i] == ']' and p != '[':
                return False
            if s[i] == '}' and p != '{':
                return False
            a.pop()
    if len(a) == 0:
        return True
    return False


print(isvalid('[[()[]{}]'))
