# f = open("myfile.txt","w")  #open file in write mode
# print("name of file:",f.name) #name of the file
# print("file mode:",f.mode) #mode of the file
# print("readable:",f.readable()) #check if file is readable
# print("writable:",f.writable()) #check if file is writable
# print("file closed:",f.closed) #check if file is closed
# f.close() #close the file
# print("file closed:",f.closed)


# f=open("myfile.txt","a") #open file in append mode and write in the file and prevous data will not be deleted
# f.write("\n Pune is a smart city")
# f.write("\n Sawantwadi is a smart city")
# f.close()
# print("operation is done and file is closed")

# f=open("myfile.txt","w") #open file in read mode
# mylist=["Pune","Sawantwadi","vengurla"] #
# tuple=("pune","sawantwadi")
# dictionary={"city1":"pune","city2":"sawantwadi"}
# f.writelines(mylist)
# f.writelines(tuple)
# f.writelines(dictionary)
# f.close()
# print("operation is done and file is closed")

# f=open("myfile.txt","r") #open file in read mode
# print(f.read()) #read the file and print the file
# f.close()

# with open("myfile.txt","w") as f: #group of operation if we want to perform it is good
#     f.write("Pune\n")
#     f.write("Sawantwadi\n")
#     f.write("Vengurla\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)

# with open("myfile.txt","r") as f: #group of operation if we want to perform it is good
#     content = print(f.read())
#     print(content)

# f1=open("OIP.jpg","rb")
# f2=open("OIP1.jpg","wb")
# data=f1.read()
# f2.write(data)
# print("operation done")

# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# # a.writerow(["StudentID","RollNo","Name","Marks"])
# studentid=int(input("Enter the student id: "))
# rollno=int(input("Enter the roll no: "))
# name=input("Enter the name: ")
# marks=int(input("Enter the marks: "))
# a.writerow([studentid,rollno,name,marks])
# print("Student record has been saved")

import csv
f=open("student1.csv","a",newline="")
a=csv.writer(f)
# a.writerow(["RollNo","Name","Mobile_no","Email_id","p1","p2","p3","total","percentage","Result"])
rollno=int(input("Enter the roll no: "))
name=input("Enter the name: ")
mobile_no=int(input("Enter the mobile_no: "))
email_id=input("Enter the email_id:")
p1=int(input("Enter the marks of p1:"))
p2=int(input("Enter the marks of p2:"))
p3=int(input("Enter the marks of p3:"))
total=p1+p2+p3
percentage=total/3.0
if p1>=40 and p2>=40 and p3>=40:
    result="Pass"
else:
    result="Fail"
a.writerow([rollno,name,mobile_no,email_id,p1,p2,p3,total,percentage,result])
print("Student record has been saved")
