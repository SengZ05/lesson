class laptop:
    def display(self):
        self.price = ''
        self.processor = ''
        self.ram = ''
        print('High Quality')
HP = laptop()
Dell = laptop()
Asus = laptop()

HP.price = '500'
Dell.processor = 'Ryzen 9'
Asus.ram = '16GB'

Dell.display()
HP.display()
Asus.display()