# # 1.Գրի ֆունկցիա, որը կստանա փոփոխական և կտպի դրա տիպը։
# def type(varibel):
#     Number = True
#     Simvol = True
#     string = True
#     Char = True
#     Number_flout = True

#     for i in varibel:
#         if ('0'  <= i <=  '9'):
#             if len(varibel) == 1 :
#                 print("Inputed is number:")
#             else:
#                 print("Inputed is number_array:")
#                 break
            
#         elif (('a'  <= i <=  'z') or ('A'  <= i <=  'Z')):
#             if len(varibel) == 1 :
#                 print("Inputed is character:")
#             else:
#                 print("Inputed is array:")
#                 break
                
# while (True):
#     varibel = input ("input variebal - ")
#     type(varibel)





# 2. Թիվը զույգ է թե կենտ

# number = int(input("Enter number - "))

# if number % 2 == 0:
#     print("zuyg e")
# elif (number % 2 != 0):
#     print("kent")



# 3 Ցիկլով գումարում


# a = [2, 4, 6, 8]
# s=0
# for i in a:
#     s+=i
# print(s)



# 4 1-ից n թվերի քառակուսիներ


# number = int(input("Enter number - "))
# for i in range(1, number):
#     print(i, "^ 2 = ", i * i)



# 5 Ցիկլով բառերի հաշվարկ

# words = ["devops", "linux", "python", "docker", "git"]
# for i in words:
#     print(i, " =", len(i))



# 6 Թվերի ֆիլտր
# nums = [10, 15, 20, 25, 30, 35]
# print("բաժանվում են 5-ի վրա և միաժամանակ զույգ են")
# for i in nums:
#     if (i % 5 == 0 and i % 2 ==0):
#         print(i)



# nums = [10, 15, 20, 25, 30, 35]
# for i in nums:
#     for j in str(i):
#         print(j, end=" ")




# 7 Բառի հակադարձում

# string = input(str())
# # print(string[::-1])

# for i in range(len(string) -1, -1, -1):
#         print(string[i], end = " ")



# 8 Հաշվել բառերի քանակը նախադասության մեջ

# words = str(input())

# print(words.split())

































# Խնդիր 1 — Թվերի գումարում մինչև “0”

# Գրի ծրագիր, որը օգտվողից անընդհատ կվերցնի թիվ, մինչև նա մուտքագրի 0։
# Վերջում պետք է տպի բոլոր մուտքագրված թվերի գումարը։

# q = 0
# while True:
#     numbers = int(input("Enter number - "))
#     q += numbers 
#     if numbers == 0:
#         break

# print("The sum = ", q)







# Խնդիր 2 — Ամենաերկար բառը ցուցակում

# Տրված է ցուցակ՝ Գրի ծրագիր, որը կգտնի և կտպի ամենաերկար բառը։

# words = ["devops", "linux", "docker", "monitoring", "git"]

# long = words[0]

# # for i in range(1,len(words)):                     #  range - index    
# #     if len(words[i]) > len(long):             
# #         long = words[i]

# for i in words:
#     if len(i) > len(long):
#         long = i
# print(long)






# 🧩 Խնդիր 3 — Տվյալների դասավորություն dictionary-ում

# Օգտվողը մուտքագրում է իր անունը և տարիքը։
# Ծրագիրը պահում է դրանք dictionary-ում այսպես՝

# dicct = {}
# name = input("name - ")
# age = input("age - ")
# dicct[name] = [age]
# print("Your name is ", name, " and age ", age)




# 🧩 Խնդիր 4 — Թվերի քառակուսիներ ցուցակում

# Օգտվողը մուտքագրում է թիվ n, ծրագիրը պետք է կազմի ցուցակ, որտեղ կլինեն
#  բոլոր թվերի քառակուսիները 1-ից մինչև n։

# number = int(input("number - "))
# lst = []
# for i in range(1, number):
#     lst.append(i * i)

# # for i in lst:
# print(lst)





# 🧩 Խնդիր 5 — Գուշակիր գաղտնաբառը

# Գրի ծրագիր, որը կպահի գաղտնաբառ (օրինակ՝ "admin123") և օգտվողը պետք է գուշակի այն։
# Մինչև ճիշտ չգրի, ծրագիրը կշարունակի հարցնել։


# while True:
#     password = "name12"
#     input_password = input("Enter password - ")
#     if input_password == password:
#         print("True")
#         break
#     else :
#         print("Wrong!")





# 🧩 Խնդիր 6 — Տպել միայն զույգ թվերը

# Օգտվողը ներմուծում է թվերի ցուցակ (օրինակ՝ 10, 15, 22, 31, 44)։
# Ծրագիրը պետք է տպի միայն զույգերը։

# numbers = input("Gri , - ov")
# numbers_spl = numbers.split(",") # kam bacat
# for i in numbers_spl:
#     i = int(i)
#     if i % 2 == 0:
#         print(i)






# 🧩 Խնդիր 7 — Dictionary-ների ցուցակ

# Տրված է ցուցակ՝  Գրի ծրագիր, որը կտպի բոլոր մարդկանց անունները և տարիքները 

# people = [
#     {"name": "Anna", "age": 22},
#     {"name": "John", "age": 30},
#     {"name": "Lilit", "age": 27}
# ]

# for i in people:
#     print("name -", i["name"], " age - ", i["age"])



