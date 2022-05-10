# 시간 복잡도 예제2-1

a = 5
b = 7
print(a + b)

# 시간 복잡도 예제2-2

array = [3, 5, 1, 2, 4]     # 5개의 데이터(N=5)

for i in array:
    for j in array:
        temp = i * j
        print(temp)