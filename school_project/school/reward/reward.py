# Import hàm từ module khác: reward gọi student
# Dùng import tuyệt đối (absolute import)
from school.student.grade.grade import avg_grade, grade_student_table

def award_scholarship(student_id):
    avg = avg_grade(student_id)
    grade_table = grade_student_table(student_id)
    lowest_grade = min(grade_table.values())
    if avg >= 8.0 and lowest_grade >= 6.5:
        return True
    return False
