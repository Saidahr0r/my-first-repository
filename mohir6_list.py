#  ---- 6-dars. List ----

# mevalar = ['olma', 'aNjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print(mevalar[1].upper())
# print(mevalar[1].title())
# print(mevalar[1].lower())
# print(mevalar[1].capitalize())
# print(mevalar[-1]) # ro'yxatni oxiridagi qiymatni olish uchun -1 ni terib [-1] olsa ham bo'ladi

# narxlar = [10900, 20000, 12000, 18000] # sonlar ro'yxati
# # son = ['bir', 'ikki', 3, 4, 5]  # aralash ro'yxatlar
# # ismlar = []   # bo'sh ro'yxat
# # print(narxlar[-2])
# print(narxlar[1] + narxlar[2])

# narxlar[0] = 'anjir'  # listni ichidagi elementlarni o'zgartirish 
# print(narxlar)



#               -----.append ------
#  .append buyrug'i har doim ro'yxatni oxiriga qiymat qo'shadi
# mevalar = ['olma', 'anor', 'nok']
# mevalar.append('kiwi') # mevalarga 'kiwi' ni qo'shdi
# print(mevalar)


# #             ------.insert------
# #   .insert buyrug'i yordamida listni istalgan joyiga element qo'shishimiz mumkin
# fruits = ['apple', 'kiwi', 'banana', 'peach', 'grapefruit']
# fruits.insert(2, 'grape')
# print(fruits)
# fruits.insert(0, 'carrot')
# print(fruits)

# cars = []
# cars.append('Malibu')
# cars.append('Tico')
# cars.append('Damas')
# cars.append('Gentra')
# print(cars)

# del cars[1]  # --- del --- buyrug'i yordamida ro'yxatni ichidagi elementlarni indeksi orqali o'chiramiz
# print(cars)
# cars.insert(1, 'Lada')
# print(cars)


# cars.remove('Lada')  # --- remove --- buyrug'i orqali ro'yxatni ichidagi elementni nomi orqali o'chiramiz
# print(cars)


# hayvonlar = ['mushuk', 'it', 'zebra', 'mushuk']
# hayvonlar.remove('mushuk') # Agar ro'yxatni ichida 2ta bir xil element bo'lsa, 
# # --- remove --- buyrug'i ro'yxatni ichidagi birinchi kelgan elementni o'chiradi, hammasini o'chirish un ketma-ket o'chirib chiqish kerak
# print(hayvonlar)

# bozorlik = ["yog'", "un", "makaron", "kartoshka", "piyoz"]
# mahsulot = bozorlik.pop(2) # listni ichidagi qaysidir elementni sug'gurib olish uchun .pop buyrug'idan indeksni kiritga holda foydalanamiz.
# # ! ESLATMA: .pop buyrug'i orqali elementni sug'urib olganimizda o'sha element ro'yxatni ichidan o'chib ketadi
# print("Men bozordan", mahsulot + "ni sotib oldim")
# print("Olinmagan mahsulotlar : ", bozorlik)

# mahsulot2 = bozorlik.pop() # .pop elementidan foydalanganda hech qanday indeks kiritmasak oxirgi elementni chiqarib oladi
# print(mahsulot2)

# narxlar = [10900, 20000, 12000, 18000]
# narxlar[0] = narxlar[0] + 1100
# print(narxlar)


# # task 1.

# ismlar = ["Sirojiddin", "Sardor", "Shaxboz"]
# print(ismlar)

# # task 2.

# print("Salom", ismlar[1] + ", bugun choyxona bormi?", ismlar[0], "har galgidek bormasa kerak.", ismlar[2], "do'stim siz borasizmi?")

# # task 3.

# sonlar = [2, 3, 4, 5, -6, -7, 8.5]
# print(sonlar)
# print(sonlar[0] + sonlar[4])
# print(sonlar[2] * sonlar[3])
# print(sonlar[4] - sonlar[2])
# print(sonlar[2] / sonlar[0])

# sonlar[0] = 7
# print(sonlar)
# sonlar.insert(0, 8)
# print(sonlar)


# # task 4.


# t_shaxslar = ["Amir Temur", "Alisher Navoiy", "Hitler", "Islom Karimov"]
# a = t_shaxslar.pop(-1)
# z_shaxslar = ["Ilon Musk", "Abdukarim Mirzayev", "Saidahror Hodiev", "Putin"]
# b = z_shaxslar.pop(1)
# print("Men tarixiy shaxslardan", a, "bilan, \nzamonaviy shaxslardan esa", b, "bilan \nsuhbat qilishni xohlar edim")





# # task 5.

# friends = []
# friends.append("Sirojiddin")
# friends.append("Sardor")
# friends.append("Abbos")
# friends.append("Shaxboz")
# friends.append("Jony")
# friends.append("Jamol aka")
# print(friends)

# friends.append("Damir")
# print(friends)

# friends.insert(3, "Shaxzod")
# print(friends)


# mehmonlar = []
# mehmonlar.append(friends.pop(-3))
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(2))
# print("\nMehmonga kelgan bollar: ", mehmonlar)
