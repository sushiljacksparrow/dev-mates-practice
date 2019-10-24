def sort_util(i, visited, stack, pair):
    visited[i] = True
    for j in pair:
        if j[1] == i:
            sort_util(j[0], visited, stack, pair)

    stack.append(i)

def sort(n, pair):
    visited = [False]*n
    stack = []

    for i in range(n):
        if not visited[i]:
            sort_util(i, visited, stack, pair)

    print(stack)

if __name__ == '__main__':
    sort(2, [[1,0]])
