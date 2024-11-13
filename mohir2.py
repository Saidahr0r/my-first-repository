import math
#  2-dars PRINT() funksiyasi haqida

print('Men "Del" markasidagi kompyuter sotib oldim')


# \ - Backslash -- 2ta qo'shtirnoq ishlatilganda birinchi va oxirgi qo'shtirnoqdan oldin ishlatiladi 
#  mana bunday --- print("Something \"smth\" bla bla")
print("Men \"Del\" markasidagi kompyuter sotib oldim")
print("Something \"smth\" bla bla")


# MATNNI 2GA BO'LISH USULLARI
# yozayotgan matnimiz yoki codimizni 2ta qatorga chiqarish uchun biz 3ta """ yoki 3ta''' belgilaridan foydalanamiz

print(""" Odami ersang demagil odamiy,
 Oniki, yo'q xalq g'amidin g'ami""")

# matnni 2ga bo'lish uchun biz \n belgisidan ham foydalansak bo'ladi
print("Odami ersang, demagil odamiy, \nOniki, yo'q xalq g'amidin g'ami")
print("Odami ersang, demagil odamiy, \nOniki, yo'q xalq\ g'amidin g'ami")

print(2 + 4 * 2)
print(19 / 5)
print(20 / 5)
# Sonni bo'lganda o'nlik qism qolib ketadi. Masalan 16ni 5 ga bo'lganda 3.2 qoldiq chiqadi
# Ammo consoleda faqat 3 ni o'zi chiqadi
print(16 // 4)
print(16 // 5)
print(16 / 5)

print(2 ** 4)
print("To'qqizning kvadrati", 9 ** 2, " ga teng")
print("3 x 3 = ", 3 * 3)

# % - Bo'linmaning qoldig'ini olish uchun ishlatiladi
# 16 ni 5 ga bo'lganda 1 qoldiq qoladi
print(16%5)


# MASHQLAR

print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")

print("5 ning 4-darajasi toping.  Javob: ", 5 ** 4)
print("22 ni 4 ga bo'lganda qancha qoldiq qoladi?, Javob: ", 22%4)
print("Tomonlari 125ga teng kvadratning yuzi va perimetrini toping, \n Perimetr formulasi P=4xa,  Yuza formulasi S=a^2 \n Perimetr=",4 * 125, "Yuza=", 125 ** 2)
print("Diametrdan radiusni topish formulasi: r=d/2, Yuzani topish: S=pr^2", "Yuza= ", 3.14*6**2)
print("Gipotenuza ", math.sqrt(6**2+7**2), " ga teng")

