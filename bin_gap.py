def solution(N):
    bin_N = "{0:b}".format(N)
    zero_counter = 0
    max_zeros = 0
    for i in range(len(bin_N)):
        if bin_N[i] == '0':
            zero_counter += 1
        elif bin_N[i] == '1':
            if zero_counter > max_zeros:
                max_zeros = zero_counter
            zero_counter = 0
    return max_zeros

N =  20000
res = solution(N)
print(res)