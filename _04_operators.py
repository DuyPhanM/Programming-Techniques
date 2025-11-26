# 1. Toán tử số học
a = 30 + 38 / 2 // 3 ** 2 * 3 % 5 - 2
print(a)

# Toán tử số học dùng với chuỗi
a = '3' + '3'
b = 3 * [3]

print(a)
print(b)
###########################################################

# 2. Toán tử logic
'''
Một chương trình bốc thăm trúng thưởng có thể lệ như sau:
Bạn sẽ bốc 1 lá thăm từ hộp đỏ chứa 26 lá thăm chữ cái 
và một lá thăm từ hộp xanh chứa 10 lá thăm con số
Nếu 2 lá thăm bạn bốc được ghép được thành 'K3'
Bạn sẽ trúng thưởng

Kết quả rút thăm của bạn như sau
'''
red_ballot  = 'D'
blue_ballot = '3'

choice = red_ballot == 'K' and blue_ballot == '3'

print(choice)
###########################################################

# 3. Toán tử gán

a = 32
a /= 2
a /= 2
a /= 2

print(a)

