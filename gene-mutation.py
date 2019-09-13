def queue_bfs(start, end, bank):
    queue = []
    distance = {start: 0}
    queue.append(start)
    res = None
    while len(queue) > 0 and res is None:
        temp = queue.pop(0)
        if temp == end:
            res = distance[temp]
            break
        for choice in bank:
            diff = 0
            for i in range(8):
                if choice[i] != temp[i]:
                    diff = diff + 1
            if diff == 1:
                if choice in distance.keys() and distance[temp] + 1 < distance[choice]:
                    distance[choice] = distance[temp] + 1
                else:
                    queue.append(choice)
                    distance[choice] = distance[temp] + 1
    return res

if __name__ == '__main__':
    start = 'AAAAACCC'
    end = 'AACCCCCC'
    bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC']
    res = queue_bfs(start, end, bank)
    if res is None:
        print(-1)
    else:
        print(res)
