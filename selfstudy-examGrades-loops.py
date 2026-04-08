num = int(input("How many exam grades dose each student have"))
student = 0
while True:
   
    total = 0
    if student == 1:
        print("enter the exam grades")
    else:
       print("enter the exam grades for anather student") 
    
    for i in range(1, num+1):
        grade = float(input(f"Exam {i}:"))
        total = total + grade
    Avareg = total / num
    print("The Avareg is: ", Avareg)
        
    
    
    

