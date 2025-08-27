class laptop():
    typeofobject="Gadget"
    def __init__ (self,a,b,c,d):
        self.name=a
        self.brand=b
        self.price=c
        self.color=d
    def like(self):
        return f"{self.brand} is better than among the {self.name} products"
    def exp(self):
        return f"{self.price} in {self.brand} is expensive" 
    def col(self):
        return f"The color Black is the better color in {self.brand} than {self.color}"    

obj1 = int(input(laptop("Asus", "AsusPro", 25000, "Silver")))
obj2 = int(input(laptop("Samsung", "Samsungpad", 25000, "Blue")))
obj3 = laptop("Apple", "iPad", 250000, "Black")

mylist = [obj1,obj2,obj3]
for i in range(len(mylist)):
    print(mylist[i].like())
    print("\n")
    print(mylist[i].col())
    print("\n")
    print(mylist[i].exp())
    print("\n")