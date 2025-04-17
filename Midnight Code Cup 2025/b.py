import zipfile

# Content for each file
content = "12\n" + "1 1\n" * 24

# Write files
files = ["01.out", "02.out", "03.out"]
for filename in files:
    with open(filename, "w", newline="\n") as f:
        f.write(content)

# Create zip archive
with zipfile.ZipFile("submission.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for filename in files:
        z.write(filename)

print("Files and zip created successfully.")