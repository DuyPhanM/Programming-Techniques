''' 
Kiểu dict là công cụ rất đắc lực giúp mã hóa những danh sách 
phức tạp theo cách hiểu của con người thông qua cặp key-value 
'''

person = {'name': 'Duy', 'age': 28, 'job': 'teacher'}

# Lấy value ứng với key nhưng sẽ lỗi KeyError nếu key không tồn tại
res = person['name']

# Cũng lấy value ứng với key nhưng trả về None nếu không tồn tại key
# thay vì báo lỗi KeyError
res = person.get('gender')

# Trả về danh sách các key ở dạng list
res = person.keys()

# Trả về danh sách các value ở dạng list
res = person.values()

print(res)
