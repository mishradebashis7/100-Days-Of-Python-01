def get_int_array():
    return list(map(int, input().split())) 
def solve(s):
    count_a = 0
    count_b = 0
    count_c = 0
    delta_patterns = {}
    delta_patterns[(0, 0)] = 1
    for c in s:
        if c == 'a':
            count_a += 1
        elif c == 'b':
            count_b += 1
        elif c == 'c':
            count_c += 1
        combo = (count_a - count_b, count_a - count_c)
        if combo not in delta_patterns:
            delta_patterns[combo] = 1
        else:
            delta_patterns[combo] += 1
    total = 0
    for count in delta_patterns.values():
        if count > 1:
            total += (count * (count - 1)) // 2 
    return total 
T = int(input())
for _ in range(T):
    s = input().strip()
    print(solve(s))