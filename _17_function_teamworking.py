# Hàm tính cạnh huyền bằng Pythagoras
def pythagoras(edge1, edge2):
    hypotenuse = (edge1**2 + edge2**2)**0.5
    return hypotenuse

# Hàm tính đường cao ứng với cạnh huyền
def altitude(edge1, edge2):
    # Sử dụng hàm pythagoras() để tính cạnh huyền
    hypotenuse = pythagoras(edge1, edge2)

    altitude = edge1 * edge2 / hypotenuse
    return altitude

altitude = altitude(6.2, 8)
altitude = round(altitude, 2)
print(altitude)
