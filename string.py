a = "SANJI"
print(a[ : ])

c=int(input("Enter a year: "))
if (c%4==0 and c%100!=0) or (c%400==0):
    print(c,"is a leap year")
else:    print(c,"is not a leap year")