board = [1, 9, 4, 5]

# Thay đổi giá trị theo chỉ số trong danh sách
board[2] = 7            # board = [1, 9, 7, 5]

# Thêm phần tử vào cuối danh sách
board.append(4)         # board = [1, 9, 7, 5, 4]

# Loại bỏ phần tử theo chỉ số
remove = board.pop(4)   # remove = 4, board = [1, 9, 7, 5]

# Chèn thêm 1 phần tử
board.insert(0, 4)      # board = [4, 1, 9, 7, 5]

# Thay đổi 1 phần đoạn trong danh sách
board[0:1] = [3, 0, 4]  # board = [3, 0, 4, 1, 9, 7, 5]

print(board)
