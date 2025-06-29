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
Một quán ăn phục vụ theo món ăn mà khách hàng bốc thăm được
Quán sử dụng sợi bún và bánh đa
Món ăn kèm gồm: cá, hải sản và thập cẩm

Giả sử An muốn ăn bún hải sản nhưng bốc thăm ra bún cá
'''

noodles = 'bún'
#noodles = 'bánh đa'

topping = "cá"
#topping = "hải sản"
#topping = "thập cẩm"

choice = noodles == 'bún' and topping == "hải sản"

print(choice)
###########################################################

# 3. Toán tử gán

a = 32
a /= 2
a /= 2
a /= 2

print(a)
