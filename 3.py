#write a program to convert muntes into hours and print it 
# example : 135 is 2 hours 15 minutes 

minutes=int(input("enter minutes"))
print(f"{minutes} is {minutes//60} hours {minutes%60} minutes")