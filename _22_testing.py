# QUY TRINH 6 BƯỚC KIỂM TRA 1 TEST CASE
# Hàm tính cạnh huyền bằng Pythagoras
def pythagoras(edge1, edge2):
    hypotenuse = (edge1**2 + edge2**2)**0.2
    return hypotenuse

# 1. Chọn dữ liệu đầu vào là dạng số học: 3 và 4
# 2. Kết quả dự kiến: 5.0

# 3. Kích hoạt hàm pythagoras() với đầy đủ 2 tham số đầu vào
hyp = pythagoras(3, 4)

# 4. In kết quả ra Terminal để kiểm tra kết quả thực tế
print(hyp)

# 5. So sánh kết quả dự kiến khác kết quả thực tế
          # 1.9036539387158786 != 5.0

# 6. Kết luận: Hàm hoạt động không chính xác yêu cầu
