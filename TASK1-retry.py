#CGPA Calculator
total_credits=0
gradepoints_total=0
cgpa=0

te_cred=2
soft_test_cred=5
res_sem_cred=3


students_name=input("Student's Name: ")

traffic_engineering_grade=float(input("Traffic Engineering Grade: "))
software_testing_grade=float(input("Software Testing Grade: "))
research_seminar_grade=float(input("Research Seminar Grade: "))

total_credits=te_cred+soft_test_cred+res_sem_cred
print("Total Credits= %d" %total_credits)

gradepoints_total=(traffic_engineering_grade*te_cred)+(software_testing_grade*soft_test_cred)+(research_seminar_grade*res_sem_cred)
print("Total Grade Point is = %f"  %gradepoints_total)

cgpa=float(gradepoints_total/total_credits)
print(students_name+ "s CGPA is " + str(cgpa))