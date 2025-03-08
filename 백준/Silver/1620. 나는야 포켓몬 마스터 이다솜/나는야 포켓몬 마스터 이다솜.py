import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = []
pokemon_dict = {}

for i in range(n):
    name = input().strip()
    pokemon.append(name)
    pokemon_dict[name] = i + 1  # 포켓몬 이름과 인덱스를 매핑

for _ in range(m):
    p = input().strip()
    
    if p.isdigit():
        print(pokemon[int(p) - 1])  # 숫자일 경우 리스트에서 직접 접근
    else:
        print(pokemon_dict[p])  # 딕셔너리에서 직접 접근
