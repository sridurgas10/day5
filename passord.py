import random
pswd=''
length=0
def cre_pswd(length):
    
    digits='0123456789'
    punctuation='!@#$%^&*'
    lower='abcdefghijklmnopqrstuvxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVXYZ'
   
   
    if length:
       punc=input("1.do you want special characterin pswd\n2.don't want special character in pswd\n")
       if punc=='1':
        all_char=lower+upper+digits+punctuation
        pswd=''.join(random.choices(all_char,k=length))
       elif punc=='2':
          all_char=lower+upper+digits
          pswd=''.join(random.choices(all_char,k=length))
    else: 
        print('maximum length of pswd is 12 characters') 
    print("generated passord",pswd)
      
try:  
 length=int(input("please enter a passord length\n"))
    
 pswd=cre_pswd(length)
 
except ValueError:
   print("Plese enter an integer\n") 


