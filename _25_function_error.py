isValid = False
while not isValid:
    name = input('Nhập tên của bạn: ')
    words = name.split()
    if len(words) < 2:
        continue
    for i in range(len(words)):
        # Đặt điều kiện không chuẩn
        if words[i].isalpha():
            break
        if i == len(words) - 1:
            isValid = True
        # Đặt lệnh ngắt không hợp lý
        break

def abbreviatedName(word):
    abb = ''
    for i in range(len(words) - 1):
        # Dùng sai phép biến đổi dữ liệu
        abb += words[0][i].upper() + '.'
# Lệnh đặt sai vị trí
abb += words[-1]
    return abb

print(abbreviatedName(name))
