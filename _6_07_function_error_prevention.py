''' 
Đọc, ghi file text có thể xảy ra nhiều trường hợp mắc lỗi khác nhau.
Có những lỗi có thể lường trước được như không tìm thấy file, không có quyền đọc file, 
nhưng có những lỗi hiếm gặp mà có thể chúng ta không lường trước được 
khiến việc kiểm soát lỗi ban đầu trở nên khó khăn
Vậy nên, bắt lỗi trong khi vận hành sẽ là khả thi hơn. 
'''

def readingText(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Lỗi: Tệp không tồn tại. Vui lòng kiểm tra lại tên tệp.")
    except PermissionError:
        print("Lỗi: Không có quyền đọc tệp.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

readingText('data.txt')
