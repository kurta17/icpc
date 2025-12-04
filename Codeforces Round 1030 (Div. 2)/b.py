for _ in range(int(input())):
    n = int(input())
    answers = []
    for i in range(1,19):
        m = 1 + 10**i
        if n % m == 0:
            x = n // m
            if x > 0:
                answers.append(x)
    if answers == []:
        print(0)
    else:
        print(len(answers))
        answers.sort()
        print(*answers)

