
def reverseParentheses(s):
    k = [i for i in s]
    start_paren_stack, end_paren_stack = retrieve_paren_indeces(s)

    while(start_paren_stack):
        start = start_paren_stack.pop()
        end = end_paren_stack.pop()
        sub = k[start:end+1][::-1]
        k[start:end+1] = sub

    print("".join(k).replace("(", "").replace(")", ""))
    return "".join(k).replace("(", "").replace(")", "")

def retrieve_paren_indeces(s):
    k = s[::]
    start_parens, end_parens = [], []
    for i, x in enumerate(k):
        if x == "(":
            start_parens.append(i)
            end_parens.append(None)
        elif x == ")":
            actual_len = len([x for x in end_parens if x!=None])
            dist =  actual_len - len(start_parens)
            if dist == -1:
                first_none = -1
                for j, y in enumerate(end_parens):
                    if y is None:
                        first_none =j
                        break
                end_parens[first_none] = i
            else:
                first_none = abs(dist) - 1
                for j in range(first_none, len(end_parens)):
                    if end_parens[j] is None:
                        first_none = j
                        break
                end_parens[first_none] = i
    return  start_parens, end_parens
