# Import các hàm cần thiết từ các module trong package 'school'
from school.student.grade.grade import avg_grade
from school.reward.reward import award_scholarship

if __name__ == "__main__":
    
    print("--- Ứng dụng quản lý học sinh ---")
    
    # Test học sinh S001 (Alice)
    student_id_1 = "HS010"
    print(f"\nKiểm tra học sinh {student_id_1}:")
    avg_1 = avg_grade(student_id_1)
    if avg_1 != -1:
        print(f"  - Điểm trung bình: {avg_1}")
        if award_scholarship(student_id_1):
            print("  - Kết quả học bổng: Đủ điều kiện.")
        else:
            print("  - Kết quả học bổng: Không đủ điều kiện.")
    else:
        print(f"  - Không tìm thấy học sinh có ID: {student_id_1}")
        
    