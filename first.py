

class ValidateAadhar:
    Name = "Swapnil"
    Number = "11111"
    City = "Nagpur"
    Receive_Date = "01-01-2022"

    def AadharDeatils(self):
        print(f"Name = {self.Name}\nNumber = {self.Number}\nCity = {self.City}\nReceive_Date = {self.Receive_Date}")

    def updateAadhar(self, Name, Number, City, Receive_Date):
        self.Name = Name
        self.Number = Number
        self.City = City
        self.Receive_Date = Receive_Date


inbound = ValidateAadhar()
inbound.AadharDeatils()

inbound.updateAadhar("Sagar", "22222", "Pune", "10-10-2020")
inbound.AadharDeatils()

inbound.AadharDeatils()

###---------------------------------
inbound2 = ValidateAadhar()
inbound2.AadharDeatils()

inbound2.updateAadhar("Tushas", "33333", "Mumbai", "20-20-2021")
inbound2.AadharDeatils()

##---------------------------------

inbound3 = ValidateAadhar()
inbound3.AadharDeatils()

inbound3.updateAadhar("Yusuf", "88888", "USA", "06-06-2019")
inbound3.AadharDeatils()

inbound3 = ValidateAadhar()

###---------------------------------

inbound.AadharDeatils()
inbound2.AadharDeatils()
inbound3.AadharDeatils()

###---------------------------------

print(inbound.Name)
print(inbound2.Name)
print(inbound3.Name)

ValidateAadhar.Name = "Soham"  ## we are updating to class attribute

print(inbound.Name)
print(inbound2.Name)
print(inbound3.Name)

###---------------------------------
print("#######################")

print(ValidateAadhar.City)  # Nagpur
print(inbound.City)  # Pune
print(inbound2.City)  # Mumbai
print(inbound3.City)  # Nagpur

print("#######################")

ValidateAadhar.City = "Japan"  ## we are updating to class attribute
print(ValidateAadhar.City)
print(inbound.City)  # Pune
print(inbound2.City)  # Mumbai
print(inbound3.City)


temp = "welcome"

result = temp.capitalize()
print(result)
