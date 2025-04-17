from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    st = []
    uniq = set()
    for _ in range(n):
        s = input()
        st.append(s)
        uniq.add(s)

    ans = []
    for s in st:
        found = 0
        for i in range(1,len(s)):
            pre = s[:i]
            suf = s[i:]
            if pre in uniq and suf in uniq:
                found = 1
                break
        ans.append(found)
    print(''.join(map(str,ans)))