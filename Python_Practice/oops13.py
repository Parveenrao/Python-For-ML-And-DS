# overriding built in function 

class Cart:
    def __init__(self , basket1 , basket2 , basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.others = basket3
        
        
    def __len__(self):
        print(f"Total items in the cart is :")
        return len(self.clothes) + len(self.electronics) + len(self.others)
    
Parveen = Cart(['pant' , 'shirt' , 't-shirt'] , ['earphone' , 'machine'] , ['chair'])

print(len(Parveen))       