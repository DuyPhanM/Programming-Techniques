from math import sqrt

def pythagoras(edge1, edge2):
    hyp = sqrt(edge1**2 + edge2**2)
    return hyp

# Sai kiểu dữ liệu đầu vào
err1 = pythagoras('a', 'b')

# Thiếu tham số
err2 = pythagoras(3)

# Dữ liệu đầu vào không tồn tại
a = [6, 8]
err3 = pythagoras(a[1], a[2])
