monster1 = {'name': 'Dark Magician Girl', 'attack': 2000, 'defend': 1700}

# Thay đổi value ứng với key
monster1['attack'] = 2300
# {'name': 'Dark Magician Girl', 'attack': 2300, 'defend': 1700}

# Thêm một cặp key-value
monster1['attribute'] = 'Dark'
# {'name': 'Dark Magician Girl', 'attack': 2300, 'defend': 1700, 'attribute': 'Dark'}

# Thay đổi nhiều value hoặc thêm nhiều cặp key-value
monster1.update(attack=2600, defend=1500, level=6)
# {'name': 'Dark Magician Girl', 'attack': 2600, 'defend': 1500, 'attribute': 'Dark', 'level': 6}

print(monster1)
