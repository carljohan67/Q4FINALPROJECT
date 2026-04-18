#GROUP 4: Tanguilig, Catapang, Gomez, Flestado, Ilagan
#8-Sampaguita

users={
    "user1":"pass1",
    "user2":"pass2"
    }

#Login/signup
login_option=int(input("""Hello, user.
Input 1 to login(Note for login the users and corresponding passwords are user1: pass1 and user2:pass2)
Input 2 to sign up
: """))
print("")

#Checking user and password
import time
password_att=0
if login_option==1:
    username=input("Enter username: ")
    while username not in users:
        username=input("User not found, try again: ")
    password=input("Enter password: ")
    while users[username]!=password:
        password_att=password_att+1
        password=input("Wrong password, try again: ")
        #Account lock
        if password_att>=3:
            print("Try again after 10s")
            password_att=0
            time.sleep(10)
    print(f"Welcome, {username}!")

#Sign-in
if login_option==2:
    new_user=input("Enter new username: ")
    new_password=input("Enter new password: ")
    #Confirm new user
    users.update({new_user:new_password})
    username=input("Confirm username: ")
    while username not in users:
        username=input("User not found, try again: ")
    password=input("Confirm password: ")
    while users[new_user]!=password:
        password_att=password_att+1
        password=input("Wrong password, try again: ")
        #Account lock
        if password_att>=3:
            print("Try again after 10s")
            password_att=0
            time.sleep(10)
    print(f"Welcome, {username}!")

print("""Welcome to the Grade 8 Pisay GWA Calculator
Would you like to
1. Calculate your grade per subject
2. Calculate your GWA for the entire quarter
Or click any other number to exit""")
response1=int(input("Please enter your response: "))
if response1==1:
    response=0
    while response!=2:
        answer=1
        answer2=1
        answer3=1
        totalfascore=0
        totalfamaxscore=0
        totalaascore=0
        totalaamaxscore=0
        totalltscore=0
        totalltmaxscore=0
        
        print("""Which subject would you like to calculate your GWA?
1. Math 3
2. Math 2
3. ADTECH 2
4. Social Science 2
5. Biology 1
6. Chemistry 1
7. Physics 1
8. Earth Science 1
9. PEHM 2
10. Values Education 2
11. Computer Science 2
12. English 2
13. Filipino 2""")
        
        subjectnum=int(input("Please input the subject with its corresponding number: "))
        while True:
            if subjectnum==1 or subjectnum==2 or subjectnum==5 or subjectnum==6:
                if subjectnum==1:
                    subject="Math 3"
                elif subjectnum==2:
                    subject="Math 2"
                elif subjectnum==5:
                    subject="Biology 1"
                else:
                    subject="Chemistry 1"
                #FA calculation    
                while answer!=2:
                    print("Please input your score for the FA")
                    fascore=float(input("Score: "))
                    print("Please type your maximum score for the FA")
                    famaxscore=float(input("Max Score: "))
                    while famaxscore<fascore:
                        print("Your score can not be greater than the max score")
                        fascore=float(input("Please input your score for the FA: "))
                        famaxscore=float(input("Please type your maximum score for the FA: "))
                    answer=int(input("Do you still have any fas to input(please input 1 or 2): "))
                    while answer!=1 and answer!=2:
                        print("Please pick between 1 or 2")
                        answer=int(input("Do you have anymore fas to input: "))
                    totalfascore=totalfascore+fascore
                    totalfamaxscore=totalfamaxscore+famaxscore
                #AA calculation    
                while answer2!=2:
                    print("Please input your score for the AA")
                    aascore=float(input("Score: "))
                    print("Please type your maximum score for the AA")
                    aamaxscore=float(input("Max Score: "))
                    while aamaxscore<aascore:
                        print("Your score can not be greater than the max score")
                        aascore=float(input("Please input your score for the AA: "))
                        aamaxscore=float(input("Please type your maximum score for the AA: "))
                    answer2=int(input("Do you still have any aas to input(please input 1 or 2): "))
                    while answer2!=1 and answer2!=2:
                        print("Please pick between 1 or 2")
                        answer2=int(input("Do you have anymore aas to input: "))
                    totalaascore=totalaascore+aascore
                    totalaamaxscore=totalaamaxscore+aamaxscore
                #LT calculation    
                while answer3!=2:
                    print("Please input your score for the LT")
                    ltscore=float(input("Score: "))
                    print("Please type your maximum score for the LT")
                    ltmaxscore=float(input("Max Score: "))
                    while ltmaxscore<ltscore:
                        print("Your score can not be greater than the max score")
                        ltscore=float(input("Please input your score for the LT: "))
                        ltmaxscore=float(input("Please type your maximum score for the LT: "))
                    answer3=int(input("Do you still have any lts to input(please input 1 or 2): "))
                    while answer3!=1 and answer3!=2:
                        print("Please pick between 1 or 2")
                        answer3=int(input("Do you have anymore lts to input: "))
                    totalltscore=totalltscore+ltscore
                    totalltmaxscore=totalltmaxscore+ltmaxscore
                #Perio calculation    
                perioscore=float(input("Please input your score for the perio: "))
                maxperioscore=float(input("Please input the max score for the perio: "))
                while maxperioscore<perioscore:
                    print("Your score can not be greater than the max score")
                    perioscore=int(input("Please input your score for the Perio: "))
                    maxperioscore=int(input("Please type your maximum score for the Perio: "))
                #Raw grade calculation    
                fapercentage=totalfascore/totalfamaxscore*0.30
                aapercentage=totalaascore/totalaamaxscore*0.15
                ltpercentage=totalltscore/totalltmaxscore*0.30
                periopercentage=perioscore/maxperioscore*0.25
                GWA=fapercentage+aapercentage+ltpercentage+periopercentage
                grading=int(input("Please input 1 for first grading and please input 2 for the other gradings: "))
                
                while grading!=1 and grading!=2:
                    grading=int(input("Please input 1 or 2: "))
                #Raw grade calculation with previous raw grade
                if grading==2:
                    previousrawgrade=float(input(f"Please input your raw grade(0-100) in {subject}: "))
                    while previousrawgrade>100 or previousrawgrade<0:
                        previousrawgrade=float(input("Please input your raw grade again it can not over 100 or under 0: "))
                    GWA=(GWA*2/3) + (previousrawgrade/300)
                rawgrade=round(GWA*100,2)
                
                print(f"Raw grade: {rawgrade}")
                #GWA calculation
                if GWA<=1.00 and GWA>=0.96:
                    print(f"Your grade for {subject} is 1.00")
                elif GWA<0.96 and GWA>=0.9:
                    print(f"Your grade for {subject} is 1.25")
                elif GWA<0.9 and GWA>=0.84:
                    print(f"Your grade for {subject} is 1.50")
                elif GWA<0.84 and GWA>=0.78:
                    print(f"Your grade for {subject} is 1.75")
                elif GWA<0.78 and GWA>=0.72:
                    print(f"Your grade for {subject} is 2.00")
                elif GWA<0.72 and GWA>=0.66:
                    print(f"Your grade for {subject} is 2.25")
                elif GWA<0.66 and GWA>=0.6:
                    print(f"Your grade for {subject} is 2.50")
                elif GWA<0.6 and GWA>=0.55:
                    print(f"Your grade for {subject} is 2.75")
                elif GWA<0.55 and GWA>=0.5:
                    print(f"Your grade for {subject} is 3.00")
                elif GWA<0.5 and GWA>=0.4:
                    print(f"Your grade for {subject} is 4.00")
                elif GWA<0.4 and GWA>=0:
                    print(f"Your grade for {subject} is 5.00")
                else:
                    print("Invalid Grade")
                break        
            elif subjectnum==3 or subjectnum==9:
                if subjectnum==3:
                    subject="ADTECH 2"
                else:
                    subject="PEHM 2"
                #FA calculation    
                while answer!=2:
                    print("Please input your score for the FA")
                    fascore=float(input("Score: "))
                    print("Please type your maximum score for the FA")
                    famaxscore=float(input("Max Score: "))
                    while famaxscore<fascore:
                        print("Your score can not be greater than the max score")
                        fascore=float(input("Please input your score for the FA: "))
                        famaxscore=float(input("Please type your maximum score for the FA: "))
                    answer=int(input("Do you still have any fas to input(please input 1 or 2): "))
                    while answer!=1 and answer!=2:
                        print("Please pick between 1 or 2")
                        answer=int(input("Do you have anymore fas to input: "))
                    totalfascore=totalfascore+fascore
                    totalfamaxscore=totalfamaxscore+famaxscore
                #AA calculation    
                while answer2!=2:
                    print("Please input your score for the AA")
                    aascore=float(input("Score: "))
                    print("Please type your maximum score for the AA")
                    aamaxscore=float(input("Max Score: "))
                    while aamaxscore<aascore:
                        print("Your score can not be greater than the max score")
                        aascore=float(input("Please input your score for the AA: "))
                        aamaxscore=float(input("Please type your maximum score for the AA: "))
                    answer2=int(input("Do you still have any aas to input(please input 1 or 2): "))
                    while answer2!=1 and answer2!=2:
                        print("Please pick between 1 or 2")
                        answer2=int(input("Do you have anymore aas to input: "))
                    totalaascore=totalaascore+aascore
                    totalaamaxscore=totalaamaxscore+aamaxscore
                #Raw grade calculation    
                fapercentage=totalfascore/totalfamaxscore*0.30
                aapercentage=totalaascore/totalaamaxscore*0.70
                grading=int(input("Please input 1 for first grading and please input 2 for the other gradings: "))
                
                while grading!=1 and grading!=2:
                    grading=int(input("Please input 1 or 2: "))
                #Raw grade calculation with previous raw grade
                if grading==2:
                    previousrawgrade=float(input(f"Please input your raw grade(0-100) in {subject}: "))
                    while previousrawgrade>100 or previousrawgrade<0:
                        previousrawgrade=float(input("Please input your raw grade again it can not over 100 or under 0: "))
                    GWA=(GWA*2/3) + (previousrawgrade/300)
                rawgrade=round(GWA*100,2)
                #GWA calculation
                print(f"Raw grade: {rawgrade}")
                if GWA<=1.00 and GWA>=0.96:
                    print(f"Your grade for {subject} is 1.00")
                elif GWA<0.96 and GWA>=0.9:
                    print(f"Your grade for {subject} is 1.25")
                elif GWA<0.9 and GWA>=0.84:
                    print(f"Your grade for {subject} is 1.50")
                elif GWA<0.84 and GWA>=0.78:
                    print(f"Your grade for {subject} is 1.75")
                elif GWA<0.78 and GWA>=0.72:
                    print(f"Your grade for {subject} is 2.00")
                elif GWA<0.72 and GWA>=0.66:
                    print(f"Your grade for {subject} is 2.25")
                elif GWA<0.66 and GWA>=0.6:
                    print(f"Your grade for {subject} is 2.50")
                elif GWA<0.6 and GWA>=0.55:
                    print(f"Your grade for {subject} is 2.75")
                elif GWA<0.55 and GWA>=0.5:
                    print(f"Your grade for {subject} is 3.00")
                elif GWA<0.5 and GWA>=0.4:
                    print(f"Your grade for {subject} is 4.00")
                elif GWA<0.4 and GWA>=0:
                    print(f"Your grade for {subject} is 5.00")
                else:
                    print("Invalid Grade")
                break
            elif subjectnum==7:
                subject="Physics 1"
                #FA calculation
                while answer!=2:
                    print("Please input your score for the FA")
                    fascore=float(input("Score: "))
                    print("Please type your maximum score for the FA")
                    famaxscore=float(input("Max Score: "))
                    while famaxscore<fascore:
                        print("Your score can not be greater than the max score")
                        fascore=float(input("Please input your score for the FA: "))
                        famaxscore=float(input("Please type your maximum score for the FA: "))
                    answer=int(input("Do you still have any fas to input(please input 1 or 2): "))
                    while answer!=1 and answer!=2:
                        print("Please pick between 1 or 2")
                        answer=int(input("Do you have anymore fas to input: "))
                    totalfascore=totalfascore+fascore
                    totalfamaxscore=totalfamaxscore+famaxscore
                #AA calculation    
                while answer2!=2:
                    print("Please input your score for the AA")
                    aascore=float(input("Score: "))
                    print("Please type your maximum score for the AA")
                    aamaxscore=float(input("Max Score: "))
                    while aamaxscore<aascore:
                        print("Your score can not be greater than the max score")
                        aascore=float(input("Please input your score for the AA: "))
                        aamaxscore=float(input("Please type your maximum score for the AA: "))
                    answer2=int(input("Do you still have any aas to input(please input 1 or 2): "))
                    while answer2!=1 and answer2!=2:
                        print("Please pick between 1 or 2")
                        answer2=int(input("Do you have anymore aas to input: "))
                    totalaascore=totalaascore+aascore
                    totalaamaxscore=totalaamaxscore+aamaxscore
                #LT calculation    
                while answer3!=2:
                    print("Please input your score for the LT")
                    ltscore=float(input("Score: "))
                    print("Please type your maximum score for the LT")
                    ltmaxscore=float(input("Max Score: "))
                    while ltmaxscore<ltscore:
                        print("Your score can not be greater than the max score")
                        ltscore=float(input("Please input your score for the LT: "))
                        ltmaxscore=float(input("Please type your maximum score for the LT: "))
                    answer3=int(input("Do you still have any lts to input(please input 1 or 2): "))
                    while answer3!=1 and answer3!=2:
                        print("Please pick between 1 or 2")
                        answer3=int(input("Do you have anymore lts to input: "))
                    totalltscore=totalltscore+ltscore
                    totalltmaxscore=totalltmaxscore+ltmaxscore
                #Raw grade calculation
                if totalfamaxscore == 0:
                    fapercentage = 0
                else:
                    fapercentage = totalfascore/totalfamaxscore*0.30
                    
                if totalaamaxscore == 0:
                    aapercentage = 0
                else:
                    aapercentage = totalaascore/totalaamaxscore *0.15
                    
                if totalltmaxscore == 0:
                    ltpercentage = 0
                else:
                  ltpercentage=totalltscore/totalltmaxscore*0.55  

                GWA=fapercentage+aapercentage+ltpercentage
                grading=int(input("Please input 1 for first grading and please input 2 for the other gradings: "))
                
                while grading!=1 and grading!=2:
                    grading=int(input("Please input 1 or 2: "))
                #Raw grade calculation with previous grade
                if grading==2:
                    previousrawgrade=float(input(f"Please input your raw grade(0-100) in {subject}: "))
                    while previousrawgrade>100 or previousrawgrade<0:
                        previousrawgrade=float(input("Please input your raw grade again it can not over 100 or under 0: "))
                    GWA=(GWA*2/3) + (previousrawgrade/300)
                rawgrade=round(GWA*100,2)
                
                print(f"Raw grade: {rawgrade}")
                #GWA calculation
                if GWA<=1.00 and GWA>=0.96:
                    print(f"Your grade for {subject} is 1.00")
                elif GWA<0.96 and GWA>=0.9:
                    print(f"Your grade for {subject} is 1.25")
                elif GWA<0.9 and GWA>=0.84:
                    print(f"Your grade for {subject} is 1.50")
                elif GWA<0.84 and GWA>=0.78:
                    print(f"Your grade for {subject} is 1.75")
                elif GWA<0.78 and GWA>=0.72:
                    print(f"Your grade for {subject} is 2.00")
                elif GWA<0.72 and GWA>=0.66:
                    print(f"Your grade for {subject} is 2.25")
                elif GWA<0.66 and GWA>=0.6:
                    print(f"Your grade for {subject} is 2.50")
                elif GWA<0.6 and GWA>=0.55:
                    print(f"Your grade for {subject} is 2.75")
                elif GWA<0.55 and GWA>=0.5:
                    print(f"Your grade for {subject} is 3.00")
                elif GWA<0.5 and GWA>=0.4:
                    print(f"Your grade for {subject} is 4.00")
                elif GWA<0.4 and GWA>=0:
                    print(f"Your grade for {subject} is 5.00")
                else:
                    print("Invalid Grade")
                break
            elif subjectnum==4 or subjectnum==8 or subjectnum==11 or subjectnum==12 or subjectnum==13:
                if subjectnum==4:
                    subject="Social Science"
                elif subjectnum==8:
                    subject="Earth Science"
                elif subjectnum==11:
                    subject="Computer Science"
                elif subjectnum==12:
                    subject="English"
                else:
                    subject="Filipino"
                #FA Calculation
                while answer!=2:
                        print("Please input your score for the FA")
                        fascore=float(input("Score: "))
                        print("Please type your maximum score for the FA")
                        famaxscore=float(input("Max Score: "))
                        while famaxscore<fascore:
                            print("Your score can not be greater than the max score")
                            fascore=float(input("Please input your score for the FA: "))
                            famaxscore=float(input("Please type your maximum score for the FA: "))
                        answer=int(input("Do you still have any fas to input(please input 1 or 2): "))
                        while answer!=1 and answer!=2:
                            print("Please pick between 1 or 2")
                            answer=int(input("Do you have anymore fas to input: "))
                        totalfascore=totalfascore+fascore
                        totalfamaxscore=totalfamaxscore+famaxscore
                #AA calculation        
                while answer2!=2:
                    print("Please input your score for the AA")
                    aascore=float(input("Score: "))
                    print("Please type your maximum score for the AA")
                    aamaxscore=float(input("Max Score: "))
                    while aamaxscore<aascore:
                        print("Your score can not be greater than the max score")
                        aascore=float(input("Please input your score for the AA: "))
                        aamaxscore=float(input("Please type your maximum score for the AA: "))
                    answer2=int(input("Do you still have any aas to input(please input 1 or 2): "))
                    while answer2!=1 and answer2!=2:
                        print("Please pick between 1 or 2")
                        answer=int(input("Do you have anymore aas to input: "))
                    totalaascore=totalaascore+aascore
                    totalaamaxscore=totalaamaxscore+aamaxscore
                #LT calculation    
                while answer3!=2:
                    print("Please input your score for the LT")
                    ltscore=float(input("Score: "))
                    print("Please type your maximum score for the LT")
                    ltmaxscore=float(input("Max Score: "))
                    while ltmaxscore<ltscore:
                        print("Your score can not be greater than the max score")
                        ltscore=float(input("Please input your score for the LT: "))
                        ltmaxscore=float(input("Please type your maximum score for the LT: "))
                    answer3=int(input("Do you still have any lts to input(please input 1 or 2): "))
                    while answer2!=1 and answer2!=2:
                        print("Please pick between 1 or 2")
                        answer3=int(input("Do you have anymore lts to input: "))
                    totalltscore=totalltscore+ltscore
                    totalltmaxscore=totalltmaxscore+ltmaxscore
                #Calculation of Grade
                fapercentage=totalfascore/totalfamaxscore*0.30
                aapercentage=totalaascore/totalaamaxscore*0.40
                ltpercentage=totalltscore/totalltmaxscore*0.30
                GWA=fapercentage+aapercentage+ltpercentage
                grading=int(input("Please input 1 for first grading and please input 2 for the other gradings: "))
                while grading!=1 and grading!=2:
                    grading=int(input("Please input 1 or 2: "))
                if grading==2:
                    #Calculating based of previousrawgrade
                    previousrawgrade=float(input(f"Please input your raw grade(0-100) in {subject}: "))
                    while previousrawgrade>100 or previousrawgrade<0:
                        previousrawgrade=float(input("Please input your raw grade again it can not over 100 or under 0: "))
                    GWA=(GWA*2/3) + (previousrawgrade/300)
                rawgrade=round(GWA*100,2)
                #Calculation of GWA
                print(f"Raw grade: {rawgrade}")
                if GWA<=1.00 and GWA>=0.96:
                    print(f"Your grade for {subject} is 1.00")
                elif GWA<0.96 and GWA>=0.9:
                    print(f"Your grade for {subject} is 1.25")
                elif GWA<0.9 and GWA>=0.84:
                    print(f"Your grade for {subject} is 1.50")
                elif GWA<0.84 and GWA>=0.78:
                    print(f"Your grade for {subject} is 1.75")
                elif GWA<0.78 and GWA>=0.72:
                    print(f"Your grade for {subject} is 2.00")
                elif GWA<0.72 and GWA>=0.66:
                    print(f"Your grade for {subject} is 2.25")
                elif GWA<0.66 and GWA>=0.6:
                    print(f"Your grade for {subject} is 2.50")
                elif GWA<0.6 and GWA>=0.55:
                    print(f"Your grade for {subject} is 2.75")
                elif GWA<0.55 and GWA>=0.5:
                    print(f"Your grade for {subject} is 3.00")
                elif GWA<0.5 and GWA>=0.4:
                    print(f"Your grade for {subject} is 4.00")
                elif GWA<0.4 and GWA>=0:
                    print(f"Your grade for {subject} is 5.00")
                else:
                    print("Invalid Grade")
                break
            elif subjectnum==10:
                completion=int(input("Have you completed all your requirements in Values Education? please input 1 for yes and 2 for no"))
                while completion!=1 and completion!=2:
                    print("Please input only 1 or 2")
                    completion=int(input("Response: "))
                if completion==1:
                    print("You have completed all your requirements for Values Education")
                else:
                    print("You have not completed all your requirements for values education")
                break
            else:
               print("Please only input from 1 to 13")
        response=int(input("Would you like to try for another subject or quit the program(please enter 1 or 2): "))
        while response!=1 and response!=2:
            response=int(input("Please enter 1 or 2: "))
elif response1==2:
    subjects=["Math 3","Math 2","ADTECH","SocSci","Biology","Chemistry","Physics","Earth Science","PEHM","Filipino","Computer Science","English","Values Education"]
    grades = [0] * 12
    gradesformatted=[]
    valid_grades = [1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 4.00, 5.00]
    print("Please input your grades and only pick from 1.00,1.25,1.50,1.75,2.00,2.25,2.50,2.75,3.00,4.00, and 5.00 unless its Values Education")
    g = 0
    for i in range(13):
        print(f"{subjects[i]}:")
        subject=subjects[i]
        if subject==subjects[12]:
            status=input("Please input complete or incomplete:")
            while status!="complete" and status!="incomplete":
                status=input("Please input only complete or incomplete: ")
        else:
            grade=float(input("Please input your grade: "))
            while grade not in valid_grades:
                print("Invalid grade please input your grade again")
                grade=float(input(f"{subjects[i]}: "))
            grades[g]=round(grade,2)
            g += 1
    if status=="complete":
        print(f"""{subjects[0]}: {grades[0]:.2f}
              {subjects[1]}: {grades[1]:.2f}
              {subjects[2]}: {grades[2]:.2f}
              {subjects[3]}: {grades[3]:.2f}
              {subjects[4]}: {grades[4]:.2f}
              {subjects[5]}: {grades[5]:.2f}
              {subjects[6]}: {grades[6]:.2f}
              {subjects[7]}: {grades[7]:.2f}
              {subjects[8]}: {grades[8]:.2f}
              {subjects[9]}: {grades[9]:.2f}
              {subjects[10]}: {grades[10]:.2f}
              {subjects[11]}: {grades[11]:.2f}
              {subjects[12]}: {status}""")
        TotalGWA=sum(grades)/len(grades)
        TotalGWA=round(TotalGWA,2)
        if TotalGWA<=1.50:
            print(f"Final GWA: {TotalGWA}, Congrats you are apart of the Director's List")
        else:
            print(f"Final GWA: {TotalGWA}")
        
    else:
        print(f"""{subjects[0]}: {grades[0]:.2f}
              {subjects[1]}: {grades[1]:.2f}
              {subjects[2]}: {grades[2]:.2f}
              {subjects[3]}: {grades[3]:.2f}
              {subjects[4]}: {grades[4]:.2f}
              {subjects[5]}: {grades[5]:.2f}
              {subjects[6]}: {grades[6]:.2f}
              {subjects[7]}: {grades[7]:.2f}
              {subjects[8]}: {grades[8]:.2f}
              {subjects[9]}: {grades[9]:.2f}
              {subjects[10]}: {grades[10]:.2f}
              {subjects[11]}: {grades[11]:.2f}
              {subjects[12]}: {status}""")
        TotalGWA=sum(grades)/len(grades)
        TotalGWA=round(TotalGWA,2)
        print(f"Final GWA: {TotalGWA}(Probationary Status: Please complete your VE requirements)")
  

              
                    
print("Thank you for using our program")
input("The program is closing, Press anything to exit")
