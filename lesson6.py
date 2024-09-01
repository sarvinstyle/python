# #functions

# # def greeting(name , count) : #parameter
# #     print("*" * count)
# #     print("Hello " + name)
# #     print("*" * count)


# # def get_greeting(name):
# #     return  "Helllo " + name



# # greeting("ali" , 20) #argument
# # greeting("sarvin" , 5)

# # print(get_greeting("mina"))

# def sum (x  , y =0 , z = 10) :
#     return x + y

# result = sum ( 10 , 20 , 9)
# #print(result)

# # xarg

# def multiply (*number) :
#     # print(type(number))
#     # print(number)
#     result = 1
#     for n in number :
#         result = result * n
    
#     return result

# #print(multiply(2,5,8,1))

# # xxarg

# def multiply_xx (**data) :
#     # print(data)
#     # print(type(data))
#     #print(data['name'])
#     for d in data :
#        print(d , data[d])


# #multiply_xx(name = 'sarvin' , birth_data = "1979" , score = 4.9)


# # recursion

# def add_one (num) :
#     if(num >= 10) :
#         return num
#     total = num + 1
#     print(total)
#     return add_one(total)

# # result = add_one(0)
# # print(result)


# Scope

#global
# name = "sarvin global"

# def greeting () :
#     #local
#     global name
#     name = "Sarvin"
#     print( " greenting "  + name)


# def function1 () : 
#     #name = "ali"
#     print( " function 1 " + name)

# greeting()
# function1()
# print(name)

# nonlocal

# def function1 ():
#     name = "john"
#     def function2 ():
#         nonlocal name
#         name = "ali"
#     function2()
#     return name


# result =function1()
# print(result)

# closure

def parent_func (player) :
    coins = 3

    def play_game() : 
        nonlocal coins
        coins -= 1
        print(f"{player} has {coins} coins left")
    
    return play_game


user1 = parent_func("mina")

user1()
user1()

user2 = parent_func ("ali")
user2()
user2()

user1()
