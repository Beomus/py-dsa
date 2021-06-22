def balancedBrackets_v1(string):
    if string is None:
        return True
    if isClose(string[0]):
        return False
    stack = []
    for char in string:
        if isOpen(char):
            stack.append(char)
        elif isClose(char):
            if isMatch(stack[-1], char):
                stack.pop(-1)  # list.pop() automatically pops the last element
            elif not isMatch(stack[-1], char):
                return False
    return len(stack) == 0


def isOpen(bracket):
    return True if bracket in "([{" else False


def isClose(bracket):
    return True if bracket in ")]}" else False


def isMatch(openBracket, closeBracket):
    if openBracket == "[" and closeBracket == "]":
        return True
    elif openBracket == "(" and closeBracket == ")":
        return True
    elif openBracket == "{" and closeBracket == "}":
        return True
    else:
        False


def balancedBrackets_v2(string):
    openBrackets = "([{"
    closeBrackets = ")]}"
    matching = {")": "(", "}": "{", "]": "["}

    if string is None:
        return True

    stack = []
    for char in string:
        if char in openBrackets:
            stack.append(char)
        elif char in closeBrackets:
            if len(stack) == 0:
                return False
            elif matching[char] == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
