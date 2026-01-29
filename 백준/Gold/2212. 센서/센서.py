n = int(input())
k = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

gap = [sensor[i+1] - sensor[i] for i in range(n-1)]
gap.sort()

# 집중국이 센서보다 많으면 센서마다 설치
if n <= k:
    print(0)
else:
    print(sum(gap[:(n-1) - (k-1)]))