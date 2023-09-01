
     
import random
import string
import time
def krish():
    characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")
    length=int(input("Enter the length of the password:-"))
    password=[]
    
    
    for i in range(length):
        password.append(random.choice(characters))
        
 
    random.shuffle(password)
   
    passwords="".join(password)
    print(passwords)
    
  
    
    
    
    
    
while True:
    user_input=int(input("""
                Do you want to generate new password?
                1 Yes
                2 No
                """))
    
    if user_input==1:
        krish()  
    elif user_input==2:
        print("OK buddy")
        print("ON MY WAY, PROGRESSING....")
        time.sleep(3)
        print("It is exited.")
        quit()
        
    else:
        print("Invalid operation, Enter 1 or 2.")
        
    
    




    
    
    
