import random
import matplotlib.pyplot as plt

dice = [1,2,3,4,5,6]
tryAmount = int(input("시도 횟수 : "))
sumAmount = int(input("합 개수 : "))
weight = list(map(float, input( "1~6의 가중치 띄어쓰기로 구분(0~1, 합해서 1) : ").split(" ")))
resultRange = [[x, 0] for x in range(sumAmount, sumAmount*6 + 1)]
# print(resultRange)

for _ in range(tryAmount):
    diceSum = 0
    for i in range(sumAmount):
        diceSum += random.choices(dice, weight)[0]
    for j in resultRange:
        if j[0] == diceSum:
            j[1] += 1
    
    
[print(k, " : ", v) for k, v in resultRange]


x = []
y = []
for h in resultRange:
    x.append(h[0])
    y.append(h[1])

plt.plot(x, y)
plt.grid(True)
plt.bar(x, y, color="y")
plt.show()