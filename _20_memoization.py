def fib_memo(n, memo={}):
    # 1. Điều kiện dừng khi kết quả cần tìm đã được lưu trữ
    if n in memo:
        return memo[n]
    # 2. Điều kiện dừng khi đệ quy về giá trị khởi đầu
    if n <= 1:
        return n
        
    # 3. Tính toán và lưu giá trị vào danh sách
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
