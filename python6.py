# Simple Calculator

a= int(input("a:"))
b= int(input("b:"))
task=input("(+,-,\,*,power,reminder):")
if(task=="+"):
    print("a+b:",a+b)
elif(task=="-"):
    print("a-b:",a-b)
elif(task=="*"):
    print("a*b:",a*b)  
elif(task=="/"):
    print("a/b:",a/b)
elif(task=="power"):
    print("power:",a**b)    
else:
    print('reminder:',a%b)