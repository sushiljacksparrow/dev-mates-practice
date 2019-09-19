def generate(n, current, left, right):
    # print(current, left, right)
    if len(current) == 2*n:
        print(current)
    else:
        if left > 0:
            generate(n, current + '(', left-1, right)
        if left < right and right > 0:
            generate(n, current + ')', left, right-1)



if __name__ == '__main__':
    n = 4
    generate(n, '', n, n)
