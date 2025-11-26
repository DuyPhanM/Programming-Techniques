# Bài toán bán vé xem xiếc theo độ tuổi
'''
- Dưới 6 tuổi           : Miễn phí
- Từ 6 đến dưới 18 tuổi : 50k
- Từ 18 tuổi trở lên    : 100k 
'''
age = 38

if age < 6:
    ticketPrice = 0
elif age >= 18:
    ticketPrice = 100000
else:
    ticketPrice = 50000

print(f'Giá vé của quý khách là {ticketPrice}đ.')
