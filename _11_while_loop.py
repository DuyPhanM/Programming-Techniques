# Đăng ký tài khoản mới với tên đăng nhập là dạng chữ
# và mật khẩu là dạng số, không chứa ký tự đặc biệt

username = ''
password = ''

while not username.isalpha():
    username = input('Username: ')
while not(password.isdigit() and len(password) == 6):
    password = input('Password: ')

print('\nHello ' + username + '!')
