# https://leetcode.com/problems/valid-parentheses/

def validateCheck(str):
    stack = []
    for s in str:
        if s == "(":
            stack.append(")")
        elif s == "{":
            stack.append("}")
        elif s == "[":
            stack.append("]")
        elif not stack or stack.pop() != s:
            return False
        
    return not stack

print(validateCheck("{(([[{}]]))}"))