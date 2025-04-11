
def add_num(x,y):
    
    value=x + y
    return value

def sub_num(x,y):
    value=x-y
    return value

def mul_num(x,y):
    value=x*y
    return value

def div_num(x,y):
    value=x/y
    return value

while True:
    try:
     x=int(input("enter a number"))                
     y=int(input("enter a number"))
   
      
    except ValueError:
      print("please enter an integer") 
      continue  
    number=input("1.add two numbers 2.subract two numbers 3.multiply two numbers 4.divide to numbers 5.exit\n")
   

    if number=='1':
      print(add_num(x,y))
      
    elif number=='2':
      print(sub_num(x,y))
    elif number=='3':
      print(mul_num(x,y))
    elif number=='4':
      print(div_num(x,y))  
    elif number=='5':
      exit
    else:
       break          
  
