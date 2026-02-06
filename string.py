a = "SANJI"
print(a[ : ])


 # Even or Odd
 
b =int(input("Enter a number: "))

if b%2==0:
    print("Even")
else:  
     print("Odd")
  # Leap year
c=int(input("Enter a year: "))
if (c%4==0 and c%100!=0) or (c%400==0):
    print(c,"is a leap year")
else:    print(c,"is not a leap year")