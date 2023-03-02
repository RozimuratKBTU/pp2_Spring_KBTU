import re

# 1
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

text = input()
emails = extract_emails(text)
print(emails) # Output: ['john.doe@example.com', 'jane@example.com']

# 2

def replace(txt):
    txt = re.sub(r'\bmail\.ru\b', 'gmail.com', txt)
    txt = re.sub(r'\byahoo\.com\b', 'gmail.com', txt)
    txt = re.sub(r'\bbbk\.ru\b', 'gmail.com', txt)

    return txt

txt =input()
new_txt = replace(txt)
print(new_txt)


# 3
def valid_password(password):
    if not (8 <= len(password) <= 15):
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[!@#$%^&*()_":?<>|]',password):
        return False

    return True

password = input()
if valid_password(password):
    print('Password is valid')
else:
    print('Password is invalid')
