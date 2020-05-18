#CGPA CALCULATOR(semesterwise)

##################### SEMEMTER 1 ######################################
sem1_total_credits=0
sem1_gradepoints_total=0
sem1_gpa=0

te_cred=2
soft_test_cred=5
res_sem_cred=3


traffic_engineering_grade=float(input("Traffic Engineering Grade: "))
software_testing_grade=float(input("Software Testing Grade: "))
research_seminar_grade=float(input("Research Seminar Grade: "))

sem1_total_credits=te_cred+soft_test_cred+res_sem_cred
#####print("Total Credits= %d" %sem1_total_credits)

sem1_gradepoints_total=(traffic_engineering_grade*te_cred)+(software_testing_grade*soft_test_cred)+(research_seminar_grade*res_sem_cred)
#####print("Total Grade Point is = %f"  %sem1_gradepoints_total)

sem1_gpa=float(sem1_gradepoints_total/sem1_total_credits)
####print( "Bob's Semester-1 GPA is " + str(sem1_gpa))

################### SEMESTER 2 #######################################

sem2_total_credits=0
sem2_gradepoints_total=0
sem2_gpa=0

communication_cred=5
soft_verification_cred=5
information_cred=5


##students_name=input("Student's Name: ")

communication_grade=float(input("Communication Engineering Grade: "))
soft_varification_grade=float(input("Software Verification Grade: "))
information_grade=float(input("Inofrmation Theory Grade: "))

sem2_total_credits=communication_cred+soft_verification_cred+information_cred
#########print("Total Credits= %d" %sem2_total_credits)

sem2_gradepoints_total=(communication_grade*communication_cred)+(soft_varification_grade*soft_verification_cred)+(information_grade*information_cred)
###########print("Total Grade Point is = %f"  %sem2_gradepoints_total)

sem2_gpa=float(sem2_gradepoints_total/sem2_total_credits)
##########print("Bob's Semester-2 GPA is " + str(sem2_gpa))

print("Bob's Grade Sheet")
print("Semester-1 GPA: " +str(sem1_gpa))
print("Semester-2 GPA: " +str(sem2_gpa))
cgpa=(sem1_gradepoints_total+sem2_gradepoints_total)/(sem1_total_credits+sem2_total_credits)
print("CGPA is :" + str(cgpa))