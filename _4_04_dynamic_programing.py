def fib_dp(n):
    # 1. Kiểm tra nếu là giá trị khởi đầu
    if n <= 1:
        return n
        
    # 2. Tạo danh sách lưu trữ
    dp = [0] * (n + 1)
    # 3. Thiết lập giá trị khởi đầu
    dp[1] = 1
    
    # 4. Dùng vòng lặp để tính toán và lưu vào danh sách
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    # 5. Giá trị cần tìm ở cuối danh sách
    return dp[n]
