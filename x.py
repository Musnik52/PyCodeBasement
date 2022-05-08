import re

text = "my phone is 050-698-0095, my e-mail is boris@gmail.com"
print(re.search(r"\d{3}-\d{3,}-\d{2,5}", text))  # phone
print(re.search(r"b*\w{4}@Q?\w+.com", text))  # email
