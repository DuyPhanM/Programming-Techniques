students = [
    {'name': 'An', 'math': 8.2, 'physics': 9.5, 'chemistry': 8.5},
    {'name': 'Bình', 'math': 6.5, 'physics': 7.5, 'chemistry': 7},
    {'name': 'Cường', 'math': 9, 'physics': 9, 'chemistry': 10},
    {'name': 'Dương', 'math': 8, 'physics': 7, 'chemistry': 8.5},
]

# Kiểm tra điểm liệt
def isValid(student):
    if student['math'] < 7 or student['physics'] < 7 or student['chemistry'] < 7:           # 10
        return False
    else:
        return True                                                                         # 11

# Tính điểm xét tuyển và xác nhận trúng tuyển
def checkPassed(student):
    avg = round((student['math']*2 + student['physics'] + student['chemistry'])/4, 1)       # 13
    if avg >= 8.1:                                                                          # 14
        return (avg, 'trúng tuyển')                                                         # 15
    return (avg, 'không trúng tuyển')
    
def result(name):                                                                 
    res = []                                                                                # 2
    for student in students:                                                                # 3 5 7
        if name == student['name']:                                                         # 4 6 8
            if isValid(student):                                                            # 9
                res = checkPassed(student)                                                  # 12
            else:
                return 'Bạn không trúng tuyển do điểm liệt'
            break                                                                           # 16
    if res == []:                                                                           # 17
        return 'Không có tên thí sinh này.'
    return f'Bạn đã {res[1]} với điểm xét tuyển là {res[0]}.'                               # 18
    
print(result('Cường'))                                                                      # 1

