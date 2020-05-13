def prompts():
    
    AFFIRMATION="yes","y","yeh","ok","1","yup"
    REJECTION="no","n","0","nope","nah"
    
    complete=False
    
    while not complete:
        
        while True:
            my_name=input("Please,enter your name:")
            if my_name:
                break
            print("You obviously have a name,try again!:")
            
        while True:
            try:
                my_age=int(input("Now how old are you again?:"))
                
                if 1 <= my_age <= 120:
                    break
                print("No i do not believe you,try again")
                
            except ValueError:
                print("We only determine age by whole numbers,try again")
                    
        print(f"welcome to python {my_name}")
        print(f"you are {my_age} years old")
                    
        while True:
            answer=input("is your information correct?:").lower().strip()
            
            if answer in AFFIRMATION:
                print("your information is correct,thank you")
                
                complete=True
                break
            
            elif answer in REJECTION:
                print("Why you lie like that? please retry ")
                break
            
            else:
                print("please enter a valid answer")
            
    return my_name,my_age

name,age=prompts()

print("just to prove i know,you are {my_name} and you are {my_age} years old")