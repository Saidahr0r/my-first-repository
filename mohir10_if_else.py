# son = int(input("Istalgan juft son kiriting\n>>>"))
# if (son % 2) == 0:
#     print("Rahmat")
# else:
#     print("Juft son kiriting")





# yosh = int(input("Yoshingiz nechada?\n>>>"))
# if yosh < 4 or yosh > 60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# elif yosh >= 18:
#     narh = 20000

# print(f"Bilet siz uchun {narh} so'm")





# print("Ikkita istalgan son kiriting!")

# son1 = float(input('1-son:\n>>>'))
# son2 = float(input('2-son:\n>>>'))

# if son1 > son2:
#     print("1-son katta")
# elif son1 < son2:
#     print("2-son katta")
# else:
#     print('ikkala son bir-biriga teng')





# mahsulotlar = ['pomidor', 'sabzi', 'kartoshka', 'qovoq', 'go\'sht',
#                 'makaron', 'bodring', 'tarvuz', 'qovun', 'piyoz']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'Do\'konimizda {mahsulot} bor')
#     else:
#         print(f'Do\'konimizda {mahsulot} yo\'q ')





# mahsulotlar = ['pomidor', 'sabzi', 'kartoshka', 'qovoq', 'go\'sht',
#                 'makaron', 'bodring', 'tarvuz', 'qovun', 'piyoz']
# savat = []
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         yoq_mahsulotlar.append(mahsulot)

# print(f'Siz so\'ragan barcha mahsulotlar {bor_mahsulotlar} do\'konimizda bor')
# print(f'Quyidagi mahsulotlar {yoq_mahsulotlar} do\'konimizda yo\'q')






# foydalanuvchilar = ['shomil', 'sardor', 'muzaf', 'rustam', 'said']
# new_login = input('Login kiriting:    ')

# if new_login.lower() in foydalanuvchilar:
#     print("Login band! Yangi login tanlang")
# else:
#     print(f'Xush kelibsiz {new_login}!')







son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")