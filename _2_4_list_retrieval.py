# Cách truy xuất dữ liệu của str, list và tuple là tương tự nhau

# a = 'bright'
# a = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
a = (1, 2, 9, 8, 5, 6, 7)

# res = a[1]     # Lấy phần tử theo chỉ số
# res = a[-2]    # Lấy phần tử theo chỉ số ngược
# res = a[3:5]   # Lấy các phần tử từ 3 đến 4
# res = a[:2]    # Lấy các phần tử từ đầu đến 1
# res = a[3:]    # Lấy các phần tử từ 3 đến cuối

# Sắp xếp theo list tăng dần
# res = sorted(a)

# Sắp xếp theo list giảm dần
res = sorted(a, reverse=True)

print(res)
