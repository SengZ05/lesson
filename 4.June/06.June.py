class laptop:
    charger = 'c type'
    def __init__ (self, Mem, Brand, Price):
        self.Mem = Mem
        self.Brand = Brand
        self.Price = Price
    @classmethod
    def change(cls):
        print('updated')
    def output(self):
        print('Memory: ', self.Mem)
        print('Brand: ', self.Brand)
        print('Price: ',self.Price)
        print('charger',self.charger)
        print('Charger: ', self.change)
seng = laptop('32gb', 'ALienware', '1300')
seng.output()
fong = laptop('12gb', 'dell', '1300')
fong.output()
