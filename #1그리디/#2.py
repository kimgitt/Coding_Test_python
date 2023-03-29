# 큰 수의 법칙
n, m ,k = map(int, input().split())
sum = 0
5
num = list(map(int, input().split()))
num.sort(reverse=True)

first_num = num[0]
second_num = num[1]

while True:
    for i in range(k):
        if m == 0:
            break
        sum += first_num
        m -= 1
    if m == 0:
        break
    sum += second_num
    m -= 1

print(sum)
