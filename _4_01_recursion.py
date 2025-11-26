def fibonacci(n):
    # 1. Điều kiện dừng đệ quy
    if n < 2:
        return n
    
    # 2. Cấu trúc tương đồng
    return fibonacci(n-1) + fibonacci(n-2)
