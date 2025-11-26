class Storage:
    def __init__(self, type, capacity):
        self.type = type
        self.capacity = capacity
        
    def get_info(self):
        print(f'Storage: {self.capacity}GB {self.type}.')
        
class Computer:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage # Dùng thực thể làm thuộc tính
        
    def properties(self):
        print(f'{self.name}')
        self.storage.get_info()
        
storage = Storage('SSD', 512)
computer = Computer('System76', storage)

computer.properties()
