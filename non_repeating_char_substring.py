
def sol(input):
    n = len(input)
    res = 0
    current_max = 0
    dict = {}
    for i in range(n):
        if input[i] in dict.keys():
            if res < len(dict.keys()):
                res = len(dict.keys())
            dict = {}
        else:
            dict[input[i]] = 1
    return res


if __name__ == '__main__':
    input = 'ccccccc'
    res = sol(input)
    print(res)
