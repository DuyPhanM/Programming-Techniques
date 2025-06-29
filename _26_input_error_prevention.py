''' 
Kiểm soát giá trị nhập vào từ bàn phím chỉ gồm chữ và dấu cách,
không có số và các ký tự đặc biệt, tối thiểu phải có 2 từ
'''
isValid = False
while not isValid:
    name = input('Nhập tên của bạn: ')
    words = name.split()
    if len(words) < 2:
        continue
    for i in range(len(words)):
        if not words[i].isalpha():
            break
        if i == len(words) - 1:
            isValid = True

def abbreviatedName(words):
    abb = ''
    for i in range(len(words) - 1):
        abb += words[i][0].upper() + '.'
    abb += words[-1]
    return abb

print(abbreviatedName(words))
