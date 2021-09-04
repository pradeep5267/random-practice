def fib(n, memo_dict):
    if(n <= 2):
        return 1
    if(n in memo_dict):
        # print(memo_dict[n])
        return memo_dict[n]
    else:
        memo_dict[n] = fib(n-1, memo_dict) + fib(n-2, memo_dict)
        return memo_dict[n]

memo_dict = {}
print(fib(70, memo_dict))