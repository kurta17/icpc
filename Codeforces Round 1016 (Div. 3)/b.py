# for _ in range(int(input())):
#     n = (input())
#     ind = -1
#     for i in range(len(n)-1,-1,-1):
#         if i != "0":
#             ind = i
#             break

#     if len(n) == 1:
#         print(0)
#     else:
#         other = 0
#         for i in range(ind-1):
#             if n[i] != "0":
#                 other += 1
#         print(other + len(n) - ind)
    


for _ in range(int(input())):
   n = input()
   n_zero = 0
   curr = 0
   for i in range(len(n)):
      if n[i] == '0':
         curr +=1
      else:
         n_zero+=curr
         curr = 0
   print(len(n) - n_zero - 1)
   

