class Garments:
    def __init__(self):
       
        self.GCode = "Not Assigned"
        self.GType = "Not Assigned"
        self.GFabric = "Not Assigned"
        self.GSize = 0
        self.GPrice = 0.0

    def assign(self):
        
        if self.GFabric == "Cotton":
            if self.GType == "Trouser":
                self.GPrice = 1300
            elif self.GType == "Shirt":
                self.GPrice = 1100
        else:
            if self.GType == "Trouser":
                self.GPrice = 1170
            elif self.GType == "Shirt":
                self.GPrice = 990

    def input_data(self):
        
        self.GCode = input("Enter Garment Code: ")
        self.GType = input("Enter Garment Type: ")
        self.GFabric = input("Enter Garment Fabric: ")
        self.GSize = int(input("Enter Garment Size: "))
        self.price()  

    def display(self):
       
        print("Garment Code   :", self.GCode)
        print("Garment Type   :", self.GType)
        print("Garment Fabric :", self.GFabric)
        print("Garment Size   :", self.GSize)
        print("Garment Price  :", self.GPrice)



garment = Garments()
garment.input_data()
garment.display()
