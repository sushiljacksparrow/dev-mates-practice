def reverse(words):
    l = len(words)
    res = ''
    current = ''
    for i in range(l):
        if words[i] == ' ':
            res += ' ' + current
            current = ''
        else:
            current = words[i] + current
    res = res + ' ' + current
    return res


if __name__ == '__main__':
    res = reverse('hello world')
    print(res)
