#Function to add two numbers
def add(n1, n2):
    return n1 + n2

#Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2 

#Function to multiply two numbers  
def multiply(n1, n2):
    return n1 * n2

#Function to divide two numbers
def divide(n1, n2):
    return n1 / n2

print("Select operation.")
print("1.Add '+'")
print("2.Subtract '-'")
print("3.Multiply '*'")
print("4.Divide '/'")

select=int(input("select the operator from 1,2,3,4:"))
n1=int(input("Enter the first digit:"))
n2=int(input("Enter the second digit:"))
if select==1:
    print(n1,"+",n2,"=",add(n1,n2))
elif select==2:
    print(n1,"-",n2,"=",subtract(n1,n2))
elif select==3:
    print(n1,"*",n2,"=",multiply(n1,n2))
elif select==4:
    print(n1,"/",n2,"=",divide(n1,n2))
else:
    print("Invalid option")