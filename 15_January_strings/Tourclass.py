class Tour:
    def __init__(self):
        self.Tcode ="not Assigned"
        self.NoofAdults =0
        self.NoofKids = 0
        self.KM = 0
        self.TotalFare  = 0.0

    def assign_fare(self):

        if self.KM>= 1000:
            adult_fare = 500 
        elif 500<= self.KM <1000 :
            adult_fare = 200 

        else:
            adult_fare = 200 

        kid_fare = adult_fare/ 2
        self.TotalFare = (self.NoofAdults * adult_fare) + (self.NoofKids * kid_fare)                





    def enter_tour(self):
        self.TCode = input("Enter Tour Code: ")  
        self.NoofAdults = int(input("Enter Number of Adults: "))
        self.NoofKids = int(input("Enter Number of Kids: "))
        self.Kilometers = int(input("Enter Kilometers: "))
        self.assign_fare()    

    def show_tour(self):
        
        print("\n--- Tour Details ---")
        print(f"Tour Code      : {self.TCode}")
        print(f"Number of Adults : {self.NoofAdults}")
        print(f"Number of Kids  : {self.NoofKids}")
        print(f"Kilometers      : {self.Kilometers}")
        print(f"Total Fare      : {self.TotalFare}")

if __name__ == "__main__":
    tour = Tour()
    tour.enter_tour()
    tour.show_tour()    