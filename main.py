username=input("enter username :")
password=input("enter password :")

hidden_password='*'*len(password)
print(f'Hello {username}, your password {hidden_password} is {len(password)} long')