'''
Một quán cà phê hầu gái tuyển nhân viên làm việc theo ngày lẻ 
với ca mặc định là 8h, lương 50k/giờ 
hoặc với thời gian làm việc và lương theo thỏa thuận riêng .
'''

def day_salary(work_hours=8, hourly_rate=50):
    salary = work_hours * hourly_rate
    return salary

# Eimi chỉ muốn làm 5h rồi đi học
print(f'Eimi: {day_salary(5)}k')

# Yua nổi tiếng nên thỏa thuận lương 100k/h
print(f'Yua: {day_salary(hourly_rate=100)}k')

# Arina làm theo ca và lương mặc định
print(f'Arina: {day_salary()}k')

# Minami tăng ca làm 10h và được tăng lương lên 60k/h
print(f'Minami: {day_salary(10, 60)}k')
