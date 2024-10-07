# lambda functions
# Higher order function
# list comprehension

def sum (a):
    return a + a 


sumfunc = lambda x , y  : x + y
#print(sumfunc(10 , 5))

def function_builder (x) :
   return lambda y : x + y


add10 = function_builder(10)
add20 = function_builder(20)

print(add10(5))
print(add20(2))


# sort

scores = [ 4,1,5,7,9,2]
classScores = [ ("mina" , 3) , 
               ("ali" , 5),
               ("saeed" , 10 ),
               ("sara" , 2)]
scores.sort()

classScores.sort(key= lambda item : item[1])
print(classScores)

# map 
result = map(lambda item : item[1] , classScores)
print(list(result))

result = map(lambda item : (item[0] , item[1] > 5) , classScores)
print(list(result))



# filter

result = filter(lambda item : item[1] > 3 , classScores)
print(list(result))

########## list comprehension
#[ expresssion for item in list ]

result = map(lambda item : item[1] , classScores)
result = [item[1] for item in classScores]

print(result)

result = filter(lambda item : item[1] > 3 , classScores)
result = [ item for item in classScores if   item[1] > 3]
print(result)

result = [ item **2 if item % 2 == 0 else item for item in scores ]
print(result)
