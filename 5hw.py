#write a program to check if a person is eligible for discount. the critera is he must be a student and age must be below 21 
#WITHOUT IF ELSE 
#input values to take are role and age
#Example : Eligible : True

role = input ("Enter role:")
age = int(input("Enter age: "))

eligible = (role == "student") and (age <21)

print("Eligable", eligible)