import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Vaild")
else:
    print("Invaild")