# Tính hóa đơn mua hàng

prices = [120000, 2500, 12000, 18000]
# Theo thứ tự là giá thịt lợn(kg), đậu phụ(miếng), cà chua(kg) và hành lá(kg)

pork, tofu, tomato, scallion = 0.3, 4, 0.5, 0.1

payment = pork * prices[0] + tofu * prices[1] + tomato * prices[2] + scallion * prices[3]

print(f'Vui lòng thanh toán {int(payment)} VND.')

