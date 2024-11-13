# a = 20  # int (integer) - butun son
# b = 5.5 # float - sonning o'nlik qismini ko'rsatadi
# temp = 36.6
# print(type(temp))

# aholi_soni = 7_594_376_467 # _ - pastki chiziq bilan ajratib yozilsada, terminalda sonni qoshib chiqaradi ya'ni 7594376467 deb
# print("Aholi soni: ", aholi_soni)

# x, y, z = 10, 5.5, -50  # bitta qatorda bir nechta o'zgaruvchi yozsa bo'ladi
# # agar biz arifmetik amal bajarganimizda bitta son butun bo'lib, ikkinchisi o'nlik bo'lsa, natija doim o'nlik son bo'ladi!

# c = a * b 
# print(c)
# print(type(c))


# d = 100/2
# print(d)
# print(type(d))

# c = 100//2
# print(c)
# print(type(c))


# ---------Constant qiymatlar (o'zgarmas qiymatlar)------
# constant qiymatlarni doim katta harflar bilan yozamiz. Ularni kodimizda o'zgartirish mumkin emas

# radius = 20
# PI = 3.14159
# diametr = radius * 2
# print("Aylana uzunligi: ", PI * diametr)

# ism = "Sardor"
# yosh = 22
# yosh = str(yosh) # - str funksiyasi ichiga berilgan qiymatdan matn qaytaradi. Odatda bunday qilish yaxshi emas.
#                  # sababi biz yosh o'zgaruvchisidan yana foydalanishimiz mukin
# xabar = ism + ' ' + yosh + ' yoshda'   # string bn sonlarni to'g'ridan to'g'ri bir-biriga qo'shib bo'lmaydi. Uni qo'shish uchun (str) funksiyasidan foydalanamiz
# print(xabar)

# ism = "Sardor"
# yosh = 22
# xabar = 'Sardor' + ' ' + str(yosh) + ' ' + 'yoshda'  # shu variant eng to'g'risi
# print(xabar)

# t_yil = int(input("Tug'ilgan yilingizni kiriting: ")) # input funksiyasi foydalanuvchi tomonidan kiritilgan har qanday sonni string -
# # - ko'rinishida saqlaydi. ---int--- funksiyasi inputni son qilib beradi
# yosh = 2024 - t_yil
# print("Siz", yosh, "yoshda ekansiz!")

# a = int('10')
# b = float(10)
# temp = str(36.6)



# ----- Homework -------
# 1. Istalgan sonning kvadrati va kubini hisoblaydigan dastur yaratish
# any_number = int(input('Input any number as you want\n>>>'))
# square = any_number ** 2
# cube = any_number ** 3
# print('Square of the number is equal to', square, '\nCube of the number is equal to', cube)


# age = int(input('How old are you?\n>>>'))
# birth_year = 2024 - age
# print('You were born in', birth_year)

first_numb = float(input("Input your first number: "))
second_numb = float(input("Input your second number: "))
# func_plus = first_numb + second_numb
# func_minus = first_numb - second_numb
# func_times = first_numb * second_numb
# func_divide = first_numb / second_numb
# print(f"{func_plus}   {func_minus}   {func_times}   {func_divide}")

print(f"{first_numb} + {second_numb} =", first_numb + second_numb)
print(f"{first_numb} - {second_numb} =", first_numb - second_numb)
print(f"{first_numb} * {second_numb} =", first_numb * second_numb)
print(f"{first_numb} / {second_numb} =", first_numb / second_numb)