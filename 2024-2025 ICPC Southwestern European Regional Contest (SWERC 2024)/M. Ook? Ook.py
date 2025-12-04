s = input().strip()
ans = ""
for i in s:
    if i == "O":
        ans+=".-.-"
    else:
        ans+=".-"
print(ans)

