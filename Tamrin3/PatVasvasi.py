mail = list(input())
i = 0
while i < len(mail):
    if mail[i] == "@":
        hash_index = "".join(mail[i:]).find("#")
        if hash_index != -1:
            del mail[i + hash_index]
    i += 1
mailatfixed = "".join(mail)
words = mailatfixed.split()
mailspacefixed = " ".join(words)
resultmail = []
if "\\n" in mailatfixed:
    resultmail = mailspacefixed.split("\\n")
else:
    resultmail.append(mailspacefixed)
print("Formatted Text: ", end='')
for _ in resultmail:
    print(_)
