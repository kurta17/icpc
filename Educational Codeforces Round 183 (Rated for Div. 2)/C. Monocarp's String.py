# def check(a, l):
#     a_ran_c = a[:l].count('a')
#     b_ran_c = a[:l].count('b')
#     print(a_ran_c,b_ran_c,l)
#     for i in range(l,n):
#         print(a_ran_c,b_ran_c,l)
#         if ac - a_ran_c == bc - b_ran_c:
#             return True
#         if a[i] == 'a' and a[i-l] == 'b':
#             a_ran_c += 1
#             b_ran_c -= 1
#         elif a[i] == 'b' and a[i-l] == 'a':
#             b_ran_c += 1
#             a_ran_c -= 1

#     return False


# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(str, input().strip()))
#     ac = a.count('a')
#     bc = a.count('b')
#     print(ac,bc)
#     i = -1
#     j = n - 1
#     if check(a,abs(ac-bc)):
#         print(abs(bc-ac))
#         continue
#     while i < j:
#         mid = (i + j) // 2
#         if check(a,mid):
#             j = mid 
#         else:
#             i = mid + 1
#     print(mid-1)


for _ in range(int(input())):
    n = int(input())
    s = list(map(str, input().strip()))


    ac = s.count('a')
    bc = n - ac
    d = ac - bc
    
    if d == 0:
        print(0)
        continue
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == 'a':
            val = 1
        else:
            val = -1
        prefix[i] = prefix[i - 1] + val

    ans = n+1
    mp = {}
    mp[0] = 0

    for i in range(1,n+1):
        tar = prefix[i] - d
        if tar in mp:
            j = mp[tar]
            l = i - j
            ans = min(ans,l)
        mp[prefix[i]] = i

    # print(mp)
    if ans == n:
        print(-1)
    else:
        print(ans)
