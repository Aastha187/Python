import sys
name=input("\nEnter your name:")
course_name=input("Enter your course name:")
print("\nName: ",name)
print("Course Name: ",course_name)
print("Python version: ",sys.version,"\n")
 1 write a function that takes a list as input and return its sum commulative sum min and max value using for loop define function documentation using docs stringamd show its user 
    n = int (input("Enter number:"))
    sum = 0
    list1 = list()
    for i in range(n):
        num = int(input("Enter number: "))
        list1.apend(num)
    for i in list1:
        sum = sum+1
     print("Sum", sum)
     print("Average",sum/n)
     print("Minimum",min(list1))
     print("Maximum",max(list1))
     print(cl)
        
    