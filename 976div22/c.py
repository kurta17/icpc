t = int(input())

for _ in range(t):
    b,c,d = map(int,input().split())

    or_op = b | d
    and_op = c & d 
    a = or_op - and_op

    or_a = a | b
    and_a = a & c

    if or_a - and_a == d:
        print(a)
    else:
        print(-1)

