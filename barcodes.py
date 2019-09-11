
if __name__=='__main__':
    input = [1,3, 3]
    l = len(input)

    # edge case, if the last two elements are same then this will not work
    if l > 2 and input[l-1] == input[l-2]:
        input[0], input[l-1] = input[l-1], input[0]

    for i in range(l):
        for j in range(1, l):
            if i + 1 < l and input[i] == input[i+1] and not input[i+1] is input[j]:
                input[i+1], input[j] = input[j], input[i+1]
    print(input)
