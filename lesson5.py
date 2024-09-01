#list tuple set dictionary

students = ["sarvin" , "mina" , "ali"]
newlist = ["sarvin" , 20 , 3.5 , True]

students = list(("sarvin" , "kian" , "ali" , "sara"))

# zeros = [0] * 50 
# print(zeros)

# numbers = list(range(50))
# print(numbers)
print(len(students))
print(students[::-1])
print(students)

students[0] = "sosan"
print(students)

# packing  , unpacking
nums = [1,2,3,4]
first = nums[0]
second = nums[1]
first , second , third , fourth = nums
print(first , second , third , fourth)

first, second , *other = nums
print(first , second ,other)

first, *other , last = nums
print(first , last ,other)

students.append("sarvin")

print(students)

students += ["diba"]
#students = students + newlist

students.extend(['sarvin', "mina"])
print(students)

students.insert(2 , "masoud")
print(students)

students[2:4] = ["added1" , "added2" , "added3"]
print(students)


# remove items

students.pop()
print(students)

students.remove("sarvin")
print(students)

del students[2:4]
print(students)

#students.clear()
print(students)

# del students
# print(students)


#finding items
if 'massoud' in students :
    print(students.index('massoud'))
if students.count('massoud') > 0 :
    print(students.index('massoud'))
print(students.count('massoud'))


#loop over list

for student in students:
    print(student)

for index , name in enumerate(students):
    print(index , name)

# sort


students.append("Sarvin")
students.sort(key = str.lower)
students.sort(reverse=True , key = str.lower)
print(students)

num = [3,6,8,10,4]
# num.sort(reverse= True)
# print(num)

orderd_num=sorted(num)
print(num)

nums2 = nums.copy()
nums3 = list(nums)
nums4 = nums[:]
nums[0] = 100
print(nums4 , nums)


# tuples

classes = tuple(('c' , 'html' , 'css'))
print(type(classes))

scores = (1, 2,3, 4,5)
print(type(scores))

if classes.count("c++") > 0 :
    print( classes.index('c++'))

for c in classes :
    print(c)

#unpacking
c1 , *c2,c3 = scores
print(c1 , c2,c3)

#dictionary
student = {
    "name" : "sarvin",
    "classes" : ["c" , "html"],
    "score" : 10
}


student2 = dict(name = "mina" , score = 100)

print(len(student) , len(student2))


print(student["name"])
print(student.get("score"))

print("fullname" in student)

student["name"] = "sarvin tabatabaie"

print(student)

student.update({"birthdate" : 1979})

student.pop("name")
print(student)

student.popitem()
print(student)


#student.clear()
print(student)

student_copy = student.copy()
student2 = dict(student)

student.update({"name" : "ali"})
print(student , student2 , student_copy)

# nested dictionary

user = { 
    "name" : "sarvin",
    "role" : "admin"
}

user2 =  { 
    "name" : "mina",
    "role" : "user"
}

user3 =  { 
    "name" : "ali",
    "role" : "admin"
}


office = {
    "user1" : user,
    "user2" : user2,
    "user3" : user3
}

print("\n" , office)


#set 
scores = {1,2,3,4,5}
scores2 = set((1,2,3,4))

print(scores , scores2 , type(scores2))

print(len(scores))
scores.add(8)
scores.add(5)
print(scores)

newset = { True , 2, 1 , 0 , 5 , False}
print(newset)

print ( 1 in scores) 

newScore = {2,5,8 , 9}

scores.update(newScore)
print(scores)


one = { 1,2,3}
two ={1,3,6,7}

new_set = one.union(two)
print(new_set)

new_set = one.intersection(two)
print(new_set)

new_set = one.symmetric_difference(two)
print(new_set)













