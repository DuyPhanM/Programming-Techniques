with open('data.inp', 'r') as f:
    content = f.read()
# content là string, dùng lệnh xử lý string để tách dữ liệu
data = content.split('\n')  # ['6', '12 64 4 24 35 93']
n = int(data[0])            # 6
arr = data[1].split()       # ['12', '64', '4', '24', '35', '93']
arr = list(map(int, arr))   # [12, 64, 4, 24, 35, 93]

with open('res.out', 'w', encoding='utf-8') as o:
    for i in range(n):
        o.write(str(arr[i]*2) + ' ')
