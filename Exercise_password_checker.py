username, password = input('What is your username and pasword\n').split()

print(f"Hello, {username} your password {'*' * len(password)} is {len(password)} letters long ")