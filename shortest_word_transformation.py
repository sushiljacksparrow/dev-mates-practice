def diff(word1, word2):
    l = min(len(word1), len(word2))
    count = 0
    for i in range(l):
        if word1[i] is not word2[i]:
            count = count + 1
            if count > 1:
                return False
    if count == 1:
        return True
    return False


def transform(start, end, dict):
    queue = [start]
    distance = {}
    distance[start] = 0
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp == end:
            return distance[temp] + 1

        for word in dict:
            if diff(word, temp) and word not in distance.keys():
                queue.append(word)
                distance[word] = distance[temp] + 1

    return -1


if __name__ == '__main__':
    start = 'hit'
    end = 'cog'
    words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    res = transform(start, end, words)
    print(res)
