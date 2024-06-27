def solution(n, k):
    if k == 0:
        answer = 12000 * n
    else:
        if n > 9:
            discount = 2000 * (n//10)
            answer = 12000 * n + 2000 * k - discount
        else:
            answer = 12000 * n + 2000 * k
    return answer