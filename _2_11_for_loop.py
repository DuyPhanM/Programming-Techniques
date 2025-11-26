# Ngân hàng chỉ cho thử đăng nhập 5 lần để bảo vệ tài khoản khách hàng

accounts = [
    {'username': 'alex', 'password': '300475'},
    {'username': 'david', 'password': '190845'},
    {'username': 'emily', 'password': '270173'}
]

user = 'emily'
print('Username: ' + user)

for i in range(5):
    isValid = False
    password = input('Password: ')
    for acc in accounts:
        if acc['username'] == user and acc['password'] == password:
            isValid = True
            break
    if isValid == True:
        print('Hello ' + user + '!')
        break
