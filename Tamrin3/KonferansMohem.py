n = int(input())
emails = set()
for i in range(n):
    email_ = input().split("@")
    if len(email_) == 2:
        emails.add(email_[1])
emails_sort = sorted(emails)
for _ in emails_sort:
    print(_)