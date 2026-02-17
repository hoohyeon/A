n = int(input())
lemons = list(map(int, input().split()))

cnt1 = lemons.count(1)
cnt2 = lemons.count(2)

if cnt1 >= cnt2 and (cnt1 - cnt2) % 3 == 0:
    print("Yes")
else:
    print("No")