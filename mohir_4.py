# 4-dars  STRING

# matn = "Men yangi 📱 oldim"
# print(matn)

# ism = "Sardor"
# print("Mening ismim", ism)
# ism = "Sardor"
# familiya = "Abdupattoev"
# print(ism, familiya)
# print(ism + familiya)
# print(ism + ' ' + familiya)



#  --- f-String ---- matnni orasini ochishda ishlatiladi
# va undan tashqari bir nechta matnlarni birlashtiriladi

# ism = "Sardor"
# familiya = "Abdupattoev"
# yosh = 22
# ism_sharif = f"{ism} {familiya} {yosh}"
# print(ism_sharif)
# print(f"Mening ismim {ism}")

# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}")


# print("Hello world")
# print("Hello \tworld")    #  \t (backslash t)  -- uzunroq bo'shliq (probel) qo'yadi
# print("Hello \nworld")    #  \n (backslash n)  -- matnni n qo'yilgan joyidan pastgi qatorga tushuradi

# ism = 'james'
# familiya = 'bond'
# ism_sharif = f'{ism} {familiya}'
# ism_sharif = ism_sharif.upper()
# print(ism_sharif.upper())    # upper ---  o'zgaruvchi.method ya'ni upper o'zgaruvchiga berilgan matnni hamma harflarini katta harfga o'zgartiradi
# print(ism_sharif.lower())    # lower --- o'zgaruvchini ichidagi matnni kichkinaga o'zgartirib beradi
# print(ism_sharif.title())    # title --- o'zgaruvchini ichidagi so'zlarni birinchi harflari kattaga o'zgartirib beradi
# print(ism_sharif.capitalize()) # capitalize --- o'zgaruvchini ichidagi birinchi so'zni bosh harfini kattaga o'zgartirib beradi





# meva = '    olma    '
# print("Men " + meva.lstrip() + "yaxshi ko'raman") # .lstrip  ---  matnni chap tomonidagi bo'shliqlarni olib tashlaydi
# print("Men " + meva.rstrip() + "yaxshi ko'raman") # .rstrip  --- matnni o'ng tomonidagi bo'shliqlarni olib tashlaydi
# print("Men " + meva.strip() + " yaxshi ko'raman") # .strip   --- matnni ikkala tomonidagi bo'shliqlarni olib tashlaydi
# print("Men " + meva + " yaxshi ko'raman")






# ------INPUT------
# input funksiyasi foydalanuvchidan qanaqadir ma'lumot kiritishni so'raydi

# ism = input("Ismingiz nima?")
# print("Assalomu alaykum " + ism)
# ism = input("Ismingiz nima?\n>>>")  # \n - buyoqda matnni n qo'yilgan qismidan boshlab keyingi qatorga tushiradi
# print("Assalomu alaykum, " + ism.title())  # ism.title() --- qanaqa harfda yozilishidan qat'iy nazar bosh harfda yozib beradi





# ------------UYGA VAZIFA--------------

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


# kocha = input("Kocha nomi?\n>>>")
# mahalla = input("Mahalla nomi?\n>>>")
# tuman = input("Tuman nomi?\n>>>")
# viloyat = input("Viloyat nomi?\n>>>")
# print(kocha + " ko'chasi\n" + mahalla + " mahallasi\n" + tuman + " tumani\n" + viloyat + " viloyati\n")

# manzil =f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())
# print(manzil.title())
#print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")