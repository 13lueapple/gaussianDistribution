import random
import matplotlib.pyplot as plt

moveAmount = [1, -1]
tryAmount = int(input("시도 횟수 : "))
bounceAmount = int(input("튕길 횟수 : "))
weight = list(map(float, input( "1의 가중치와 -1의 가중치 띄어쓰기로 구분(0~1, 합해서 1) : ").split(" ")))
resultRange = [[x, 0] for x in range(-bounceAmount, bounceAmount + 1, 2)]
# print(resultRange)

for _ in range(tryAmount):
    position = 0
    for i in range(bounceAmount):
        position += random.choices(moveAmount, weight)[0]
    for j in resultRange:
        if j[0] == position:
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