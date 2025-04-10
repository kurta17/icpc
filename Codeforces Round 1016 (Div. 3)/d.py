# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().split()))


# def solve_queries(n, queries):
#     N = 1 << n
    
#     def get_number(x, y):
#         x, y = x - 1, y - 1
#         start = 0
#         size = N
#         while size > 2:
#             half = size // 2
#             cells = half * half
#             if x < half and y < half: 
#                 pass  
#             elif x >= half and y >= half:  
#                 start += cells
#                 x -= half
#                 y -= half
#             elif x >= half and y < half:  
#                 start += 2 * cells
#                 x -= half
#             else: 
#                 start += 3 * cells
#                 y -= half
#             size = half
#         if x == 0 and y == 0: return start + 1  
#         if x == 1 and y == 1: return start + 2  
#         if x == 1 and y == 0: return start + 3 
#         if x == 0 and y == 1: return start + 4  
    
#     def get_position(d):
#         d = d - 1
#         x, y = 0, 0
#         start = 0
#         size = N
#         while size > 2:
#             half = size // 2
#             cells = half * half
#             if d < cells:
#                 pass 
#             elif d < 2 * cells:
#                 x += half
#                 y += half
#                 d -= cells
#                 start += cells
#             elif d < 3 * cells:
#                 x += half
#                 d -= 2 * cells
#                 start += 2 * cells
#             else:
#                 y += half
#                 d -= 3 * cells
#                 start += 3 * cells
#             size = half
#         if d == 0: return (x + 1, y + 1)
#         if d == 1: return (x + 2, y + 2)
#         if d == 2: return (x + 2, y + 1)
#         if d == 3: return (x + 1, y + 2)
    
#     results = []
#     for q in queries:
#         parts = q.split()
#         if parts[0] == '->':
#             x, y = int(parts[1]), int(parts[2])
#             num = get_number(x, y)
#             results.append(str(num))
#         elif parts[0] == '<-':
#             d = int(parts[1])
#             r, c = get_position(d)
#             results.append(f"{r} {c}")
#     return results

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     q = int(input())
#     queries = [input() for _ in range(q)]
#     answers = solve_queries(n, queries)
#     for ans in answers:
#         print(ans)



def get_id(n, row, col):
    row -= 1
    col -= 1
    size = 2 ** n
    val = 0

    while size > 2:
        half = size // 2
        block = half * half
        if row < half and col < half:
            pass
        elif row >= half and col >= half:
            val += block
            row -= half
            col -= half
        elif row >= half:
            val += 2 * block
            row -= half
        else:
            val += 3 * block
            col -= half

        size = half

    if row == 0 and col == 0: 
        return val + 1
    if row == 1 and col == 1: 
        return val + 2
    if row == 1 and col == 0: 
        return val + 3
    return val + 4

def get_coords(n, val):
    val -= 1
    size = 2 ** n
    row = col = 0
    while size > 2:
        half = size // 2
        block = half * half

        if val < block:
            pass
        elif val < 2 * block:
            row += half
            col += half
            val -= block
        elif val < 3 * block:
            row += half
            val -= 2 * block
        else:
            col += half
            val -= 3 * block

        size = half

    if val == 0: 
        return row + 1, col + 1
    if val == 1: 
        return row + 2, col + 2
    if val == 2: 
        return row + 2, col + 1
    return row + 1, col + 2

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    for _ in range(q):
        que = input().split()
        if que[0] == '->':
            r, c = int(que[1]), int(que[2])
            print(get_id(n, r, c))
        else:  # '<-'
            id = int(que[1])
            r, c = get_coords(n, id)
            print(f"{r} {c}")
