def uncensored(text, vowels):
    lst = list(text)
    answer = ''
    c = 0
    for n, ch in enumerate(lst):
        if ch == '':
            answer += vowels[c]
            c += 1
        else:
            answer += ch
    print(answer)


uncensored('*m*d h*sh*mz*d*h', 'oiaeae')
