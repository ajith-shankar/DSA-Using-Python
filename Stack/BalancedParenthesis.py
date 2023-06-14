# Write a program to check balanced parenthesis

def isBalanced(expr):
    stack = []
    for x in expr:
        # if it is opening bracket push it to the stack
        if x in ('(', '{', '['):
            stack.append(x)
        else:
            # if stack is empty
            if not stack:
                return False
            # if characters are not matching then return False
            elif not isMatching(stack[-1], x):
                return False
            # if characters are matching then pop the stack
            else:
                stack.pop()

    # stack is not empty return false (extra characters or less closing brackets)
    if stack:
        return False
    else:
        return True


def isMatching(a, b):
    if a == '(' and b == ')' or \
            a == '{' and b == '}' or \
            a == '[' and b == ']':
        return True
    else:
        return False

# Time complexity : O(N)
# Space complexity : O(N) (bcz opening brackets n/2 +  closing brackets n/2)
