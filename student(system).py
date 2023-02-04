import os
def new_student():
    f1=open("students.txt","a")
    ID=int(input("Enter student ID: "))
    if isfound(str(ID),"students.txt"):
        print("Student ID already exists")
        return
    name=input("Enter student name: ")
    mobile=input("Enter student mobile: ")
    f1.write(str(ID)+','+name+','+mobile+',0.0\n')
    f1.close()
    return
def isfound(ID,file):
    f1r=open(file,"r")
    for line in f1r:
        if str(ID)==line.split(",")[0]:
            f1r.close()
            return True
    f1r.close()
    return False
def new_course():
    f2=open("courses.txt","a")
    courseID=(input("Enter course no.: "))
    if isfound(str(courseID),"courses.txt"):
        print("Course ID already exists")
        return
    name=input("Enter course name: ")
    credits=int(input("Enter course credits: "))
    f2.write(str(courseID)+','+name+','+str(credits)+"\n")
    f2.close()
def new_grade():
    f3=open('students.txt','r') 
    f3c=open('courses.txt','r')
    
    ID=int(input("Enter student ID: "))
    if not isfound(str(ID),'students.txt'):
        print("Student ID does not exist")
        return
    else:

        st=f3.readlines()
        for line in st:
            inID=line.split(",")[0]
            if ID==int(inID):
                name=line.split(",")[1]
                mobile=line.split(",")[2]
                print("Student name: ",name)
                courseID=input("Enter course no.: ")
                x=f3c.readlines()
                if isfound(str(courseID),'courses.txt'):
                   for i in x:
                          if courseID==(i.split(",")[0]):
                            course_name=i.split(",")[1]
                            print("Course name: ",course_name)
                            course_credits=int(i.split(",")[2])
                            grade=input("Enter grade: ")
                            while grade not in ['A','B','C','D','F']:
                                grade=input("Enter grade: ")
                            try:
                                if isfound(inID,'grades.txt')and iscoID_ingrd(courseID) :
                                    
                                    g=open('grades.txt',"r")
                                    gradefile=g.readlines()
                                    # replace only the line with same id
                                    gw=open('grades.txt','w')     
                                    for line in gradefile:

                                        if str(ID)==line.split(',')[0].rstrip('\n') and courseID==line.split(',')[1]:       
                                            gw.write(str(ID)+','+courseID+','+grade)
                                        else:
                                            gw.write(line)
                                            
                                    gw.close()
                                    g.close()
                                    
                                else:
                                    grd=open("grades.txt",'a')
                                    grd.write(str(ID)+','+courseID+','+grade+'\n')
                                    grd.close()
                            except FileNotFoundError:
                                    grd=open("grades.txt",'a')
                                    grd.write(str(ID)+','+courseID+','+grade+'\n')
                   new = open("tmp.txt", "a")
                   for line in st:
                        student_ID=line.split(',')[0]
                        name=line.split(',')[1]
                        mobile=line.split(',')[2]
                        if  isfound(student_ID,'grades.txt'):
                            GPA=calculate_GPA(student_ID)
                            new.write(str(student_ID)+','+name+','+mobile+','+str(GPA)+'\n')
                        else:
                             new.write(str(student_ID)+','+name+','+mobile+',0.0\n')
                   f3.close()
                   new.close()
                   os.remove('students.txt')
                   os.rename('tmp.txt','students.txt')
                else:
                    print('Course ID does not exist')           
                f3c.close() 
                
                return 
                
            
def iscoID_ingrd(course_ID):
    gra=open('grades.txt','r')
    for line in gra:  
        print(line)
        if str(course_ID)==line.split(',')[1]:
            gra.close()
            return True
    gra.close()
    return False   
    
def grade_pc(grade,course_credits):
    
    if grade=='A':
        points=4
    elif grade=='B':
        points=3
    elif grade=='C':
        points=2
    elif grade=='D':
        points=1
    elif grade=='F':
        points=0
    return points*course_credits

def get_transcript():
    student=open("students.txt","r")
    grades=open("grades.txt","r")
    courses=open('courses.txt',"r")
    courseread=courses.readlines()
    id=int(input("Enter student ID: "))
    if not isfound(str(id),"students.txt"):
        print("Student ID does not exist")
        return
    else:
        allname=[]
        allid=[]
        allgrade=[]
        c=0
        for line in student:
            f_ID=line.split(",")[0]
            if id==int(f_ID):
                name=line.split(",")[1]
                mobile=line.split(",")[2]
                print("Student name: ",name)
                if c==0:
                    GPA=calculate_GPA(id)
                    print('GPA=',GPA,end='\n'*2)
                    c+=1
                for line in grades:
                    cond=False
                    f_ID=line.split(",")[0]
                    if str(id)==str(f_ID):
                      courseID=line.split(",")[1]
                      grade=line.split(",")[2].rstrip('\n')
                      allgrade.append(grade)
                      cond=True
                      if cond:
                       for line in courseread:
                        c_ID=line.split(",")[0]            
                        if str(courseID)==str(c_ID):
                            course_name=line.split(",")[1]
                            allname.append(course_name)
                            allid.append(courseID)
                            
        for i in range(len(allname)):
            print(allname[i],allid[i],allgrade[i],sep=' ')

    student.close()
    grades.close()
    courses.close()     
def calculate_GPA(ID):
    found=False
    student=open("students.txt","r")
    grades=open("grades.txt","r")
    courses=open("courses.txt","r")
    if not isfound(str(ID),"students.txt"):
        print("Student ID does not exist")
        return
    total_up=0
    totalcredits=0
    colines=courses.readlines()
    for line in grades:
        if str(ID) ==line.split(",")[0]:
        
            for line1 in colines:
                x=line1.split(',')[0]
                y=line.split(',')[1]
                if line1.split(",")[0] == line.split(",")[1]:
                    credit = line1.split(",")[2].rstrip('\n')
                    total_up += grade_pc(line.split(",")[2].rstrip('\n'), int(credit))
                    totalcredits += int(credit)
                    found=True
    student.close()
    grades.close()
    courses.close()
    if found:                
        GPA=total_up/totalcredits
    else:
        GPA=0.0
    return GPA
    
    
    
def main():
    print('please select one of the following:')
    list=['1-add new student','2-add new course','3-add new grade','4-print student transcript','5-to exit']
    for i in list:
        print(i)
    choice=int(input("Enter your choice: "))
    while choice!=5:
        if choice==1:
            new_student()
        elif choice==2:
            new_course()
        elif choice==3:
            new_grade()
        elif choice==4:
            get_transcript()
        print('please select one of the following:')
        for i in list:
            print(i)
        choice=int(input("Enter your choice: "))

main()

