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

f1=open("OIP.jpg","rb")
f2=open("OIP1.jpg","wb")
data=f1.read()
f2.write(data)
print("operation done")
