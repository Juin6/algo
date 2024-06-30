def solution(babbling):
    answer = 0
    def babytalk(word):
        list = ['aya', 'ye', 'woo', 'ma']
        y = len(word)
        z = 0
        for i in list:
            if i in word:
                z = z + len(i)
        if y == z:
            return 1
        else:
            return 0
    for i in babbling:
        answer = answer + babytalk(i)
    return answer