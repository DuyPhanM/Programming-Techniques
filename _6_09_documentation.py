def pythagoras(edge1, edge2):
    """
    Tính độ dài cạnh huyền bằng định lý Pythagoras.
    
    Đầu vào:
        edge1: Độ dài cạnh góc vuông thứ nhất (float)
        edge2: Độ dài cạnh góc vuông thứ hai (float)
    
    Đầu ra:
        Độ dài cạnh huyền (float)
    """

    # Pythagoras: c2 = a2 + b2
    hypotenuse = (edge1**2 + edge2**2)**0.5     # căn bậc 2 là mũ 1/2
    
    return hypotenuse

print(pythagoras(3, 4))
