def fib_tail(n, a=0, b=1):
    # 1. Điều kiện dừng đệ quy
    if n == 0:
        return a
        
    # 2. Cấu trúc tương đồng
    return fib_tail(n - 1, b, a + b)
    
    
    
    
