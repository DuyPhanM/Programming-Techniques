# Tính hóa đơn mua hàng

prices = [120000, 12000]
# Theo thứ tự là giá của thịt lợn(kg) và cà chua(kg)

pork, tomato = 0.3, 0.5

payment = pork * prices[0] + tomato * prices[1]

print(f'Vui lòng thanh toán {int(payment)} VND.')

