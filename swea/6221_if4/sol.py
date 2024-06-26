import sys
sys.stdin = open('input.txt')

man1 = input()
man2 = input()

if man1 == '가위' and man2 == '보':
    winner = 'Man1 Win!'
elif man1 == '바위' and man2 == '가위':
    winner = 'Man1 Win!'
elif man1 == '보' and man2 == '바위':
    winner = 'Man1 Win!'
elif man1 == man2:
    winner = 'draw'
else:
    winner = 'Man2 Win!'

print(f'Result : {winner}')



#man1이 이기는 경우 가위 - 보, 바위 - 가위, 보 - 바위
#같은 경우
#그 외 나머지