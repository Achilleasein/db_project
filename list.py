def solution(S,X):
    str_found = -1
    chars_found = 0
    if len(X) > len(S):
        return str_found 
    str_size = len(X)
    j = 0
    for i in range(len(S)):
        if len(X) + i > len(S):
            return str_found 
        while j < str_size:
            if X[i + j] == S[i + j]:
                chars_found += 1
            elif X[i + j] == '*':
                chars_found += 1
            else:
                chars_found -= 1
            j += 1
        if chars_found == str_size :
            str_found = 1 
        
    return str_found

S = 'abcdddddd'
X = 'abc'
print(solution(S,X))