# Kiểu tuple
location = (21.4912, 103.0023)
'''
- Thứ tự            : Có        location[0]
- Bất biến          : Có        location[0] = 0
- Giá trị duy nhất  : Không     (21.4912, 103.0023, 21.4912)
'''

print(location)

# Kiểu dictionary
person = {'name': 'Duy', 'age': 28, 'job': 'teacher'}
'''
- Thứ tự            : Có        person['name']
- Bất biến          : Không     person['name'] = 'An'
- Giá trị duy nhất  : Khóa      {'name': 'Duy', 'age': 28, 'job': 'teacher', 'name': 'An'}
'''

print(person)

# Kiểu set
hobbies = {'reading', 'traveling', 'sports', 'music'}
'''
- Thứ tự            : Không     hobbies[0]
- Bất biến          : Không     hobbies.add('art')
- Giá trị duy nhất  : Tất cả    {'reading', 'traveling', 'sports', 'music', 'sports'}
'''

print(hobbies)

# Kiểu list
shopping_list = ['milk', 'eggs', 'bread', 'butter', 'milk']

'''
- Thứ tự            : Có        shopping_list[0]
- Bất biến          : Không     shopping_list[0] = 'yogurt'
- Giá trị duy nhất  : Không     ['milk', 'eggs', 'bread', 'butter', 'milk']
'''

print(shopping_list)
