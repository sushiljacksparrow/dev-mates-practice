
def generate(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(1, r+1):
            arr[l], arr[i] = arr[i], arr[l]
            generate(arr, l+1, r)
            arr[l], arr[i] = arr[i], arr[l]


if __name__ == '__main__':
    input = [1,1,2]
    generate(input, 0, len(input)-1)
