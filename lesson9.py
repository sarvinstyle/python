# Exceptions - Error Handeling
print("\n\n")
courses = ["html" , "css"]
try :
    file = open("lesson1.py")
    your_age= int(input("enter your age:"))
    if your_age <10 :
        raise Exception("invalid age")
    x = 2/your_age
    # print(courses[2])
except Exception as error:
    print("an error raised")
    print(error)
    # print(type(error))
else:
    print("you entered valid number for age")
finally:
    file.close()
 

print("___ application is finished ___")
