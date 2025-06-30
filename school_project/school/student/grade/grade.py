# Import dữ liệu từ module student_info.py (đặt trong thư mục ngang cấp)
# Dùng import tương đối (relative import)
from ..student_info.student_info import students_data

def avg_grade(student_id):
    for student in students_data:
        if student['id'] == student_id:
            score = student['scores']
            avg = round((sum(score.values()) + score['math'] + score['literature']) / 11, 1)
            return avg
    return -1

def grade_student_table(student_id):
    for student in students_data:
        if student['id'] == student_id:
            return student['scores']
    return None

