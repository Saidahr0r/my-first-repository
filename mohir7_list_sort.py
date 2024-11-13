# cars = ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']
# cars.sort() # .sort()  buyrug'i list ichidagi elementlarni sortlab beradi (alifbo tartibida)
# print(cars)

# cars = ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']
# # cars.sort(reverse=True)  # .sort(reverse=True) - listni teskarisiga ketma ket o'girib beradi
# # print(cars)

# print(sorted(cars)) # sorted methodi yordamida asl ro'yxatga tegmagan holda elementlarni bir boshidan alifbo tartibida chiqarishimiz mumkin

# print(sorted(cars, reverse=True)) # sorted methodidan foyadalanganda list elementlari listni ichida avvalgidek turaveradi, ammo terminalda aksincha

# sonlar = [3, 5, 7, 2, 0, 5, -9, -1, -4]
# # print(sorted(sonlar))
# # print(sorted(sonlar, reverse=True))

# # sonlar.sort()
# # print(sonlar)
# # sonlar.sort(reverse=True)
# # print(sonlar)


# # sonlar.reverse() # ushbu reverse listni ichidagi elementlarni teskari qb beradi
# # print(sonlar)


# cars = ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']
# print(len(cars))
#   # ---- len ---- methodi listni ichidagi elementlarni sanaydi
# sonlar = [3, 5, 7, 2, 0, 5, -9, -1, -4] 
# uzunlik = len(sonlar)
# print(uzunlik)


# ---- range ------ methodi ma'lum bir oraliqdagi sonlarni qaytaradi
# !  rangedan foydalanganimizda e'tiborli bo'lishimiz kerak. Chunki range berilgan qiymatgacha bo'lgan sonlarni qaytaradi

# sonlar = list(range(0, 10))
# print(sonlar) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# sonlar = list(range(21, 30))
# print(sonlar)

# toq_sonlar = list(range(1, 20, 2)) # 2 tadan keyingisini chiqar degan buyruq berdik hozir
# print(toq_sonlar)

# juft_sonlar =list(range(0, 20, 2))
# print(juft_sonlar)

# sanash = list(range(0, 100, 10))
# print(sanash)

# narxlar = [2000, 3200, 20000, 40500, 32000]
# print(min(narxlar)) # min - listni ichidagi eng kichkina qiymatni olib beradi
# print(max(narxlar)) # max - listni ichidagi eng katta qiymatni olib beradi
# print(sum(narxlar)) # sum - listni ichidagi barcha sonlarni qo'shib beradi

# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon: ", arzon, "\nEng qimmat: ", qimmat, "\nJami: ", jami)

# print(narxlar[0:3])  # listni ichidagi ma'lum elementlarni olish uchun qaysi elementdan boshlab qaysinisi kerak bo'lsa shu elementlar
#                      # tartib raqamini  kiritamiz. Bundan chiqarish xuddi range nikidek

# print(narxlar[:2]) # bunda royxatni 0 dan boshlab kesadi

# print(narxlar[1:]) # bunda ro'yxatni oxirigacha kesib boradi sababi biz qayerda tugashini kiritmadik


# cars = ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']

# my_cars = cars  # Bunda cars bilan my_cars listini elementlari bir xil bop qoladi
# print(my_cars)  #   ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']

# my_cars.remove('Dodge')
# print(my_cars)  #   ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Cadillac']

# my_cars[2] = 'Mercedez benz'
# print(my_cars)  #  ['Malibu', 'BMW', 'Mercedez benz', 'Toyota', 'Ford', 'Cadillac']

# my_cars = cars[ : ] # bu buyruq cars listini ichidagi elementlarni boshidan oxirigacha my_cars listiga nusxalaydi
# my_cars.remove('BMW')
# print(my_cars) #   ['Malibu', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']
# print(cars)   #    ['Malibu', 'BMW', 'Tesla', 'Toyota', 'Ford', 'Dodge', 'Cadillac']


#                   -----"TUPLE"------  O'zgarmas qiymat. Tupleni ichiga qiymat berib bo'lmaydi

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[2:4])
# print(toys[3:])

# toys = list(toys) # tuple ga o'zgartirish kiritish uchun uni list (oddiy ro'yxat)ga aylantirib olamiz
# print(toys)  #  ['bus', 'car', 'bear', 'dino', 'snake', 'lizard']

# toys.append('monkey')
# print(toys)   #   ['bus', 'car', 'bear', 'dino', 'snake', 'lizard', 'monkey']

# toys = tuple(toys)  # o'zgarishdan so'ng yana qaytarib tuple o'zgartirib qo'yamiz
# print(toys)  #   ('bus', 'car', 'bear', 'dino', 'snake', 'lizard', 'monkey')












# # ------ HOMETASKS -----

# davlatlar = ['USA', 'UK', 'Italy', 'Canada', 'Uzbekistan', 'Turkey']
# print(davlatlar)

# print(len(davlatlar))

# print(sorted(davlatlar))

# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)

# davlatlar.sort()
# print(davlatlar)

# davlatlar.sort(reverse=True)
# print(davlatlar)


# juft_sonlar = list(range(120, 1200, 2))
# print(juft_sonlar)

# print(sum(juft_sonlar))

# kichik = min(juft_sonlar)
# katta = max(juft_sonlar)
# print("Ro'yxatdagi eng katta va \neng kichkina son ayirmasi: ", katta - kichik, "ga teng")

# uzunlik = len(juft_sonlar)
# print("Ro'yxatda jami", uzunlik, "ta son ishtirok etgan")

# print(juft_sonlar[:20])
# print(juft_sonlar[270:290])
# print(juft_sonlar[520:540])


# taomlar = ['osh', 'manti', 'somsa', 'dimlama', 'norin']
# nonushta = taomlar[ : ]
# nonushta.remove('osh')
# nonushta.remove('dimlama')
# nonushta.append('qaymoq')
# nonushta.append('asal')
# nonushta.append('sariyog')
# print(nonushta)
# print(taomlar)

# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"
# print(nonushta)