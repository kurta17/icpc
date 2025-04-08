import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        if all(c == s[0] for c in s):
            print(-1)
            continue
        l = s.count('L')
        i = s.count('I')
        t_char = s.count('T')
        max_initial = max(l, i, t_char)
        ceil_n3 = (n + 2) // 3
        k = max(max_initial, ceil_n3)
        m = 3 * k - n
        if m < 0 or m > 2 * n:
            print(-1)
            continue
        added_L = k - l
        added_I = k - i
        added_T = k - t_char
        if added_L < 0 or added_I < 0 or added_T < 0:
            print(-1)
            continue
        current = list(s)
        insertions = []
        possible = True
        for _ in range(m):
            inserted = False
            for pos in range(len(current) - 1):
                a = current[pos]
                b = current[pos + 1]
                if a != b:
                    possible_chars = {'L', 'I', 'T'} - {a, b}
                    c = possible_chars.pop()
                    if added_L > 0 and c == 'L':
                        current.insert(pos + 1, 'L')
                        insertions.append(pos + 1)
                        added_L -= 1
                        inserted = True
                        break
                    elif added_I > 0 and c == 'I':
                        current.insert(pos + 1, 'I')
                        insertions.append(pos + 1)
                        added_I -= 1
                        inserted = True
                        break
                    elif added_T > 0 and c == 'T':
                        current.insert(pos + 1, 'T')
                        insertions.append(pos + 1)
                        added_T -= 1
                        inserted = True
                        break
            if not inserted:
                possible = False
                break
        if possible and added_L == 0 and added_I == 0 and added_T == 0:
            print(len(insertions))
            for pos in insertions:
                print(pos)
        else:
            print(-1)

if __name__ == "__main__":
    solve()