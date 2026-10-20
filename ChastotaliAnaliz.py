# Berilgan matnlarning harflari chastotasini tahlil qilish uchun dastur. Kriptotahlilda foydalaniladi
def chastota_tahlil(matn):
    # Harflar chastotasini hisoblash uchun lug'at yaratish
    chastota = {}
    ALIFBO = "abcdefghijklmnopqrstuvwxyz"  # Ingliz alifbosi harflari
    # Matndagi har bir belgini tekshirish
    for belgi in matn:
        # Agar belgi harf bo'lsa
        belgi = belgi.lower()
        if belgi in ALIFBO:
              # Kichik harflarga o'tkazish
            if belgi in chastota:
                chastota[belgi] += 1  # Agar belgi lug'atda bo'lsa, hisobni oshirish
            else:
                chastota[belgi] = 1  # Aks holda, yangi belgi qo'shish
   # TartiblanganHarfalarChastotasi=sorted(chastota_tahlil(Matn).items())
    UsibBoruvchi={}
    for harf, chastota in sorted(chastota.items(), key=lambda x: x[1], reverse=True):
        UsibBoruvchi[harf]=chastota
  
    
    return UsibBoruvchi
# Matn="Marsda doimiy yashash uchun uchta asosiy shart aytildi Insoniyat Marsda doimiy yashashi uchun Yer bilan ishonchli aloqa oʻrnatish, ikki sayyora oʻrtasida yuk tashishni yoʻlga qoʻyish va insonning tirik qolishi uchun sharoit yaratish zarur. Xitoylik tadqiqotchi Chjan Szyatszyun Qizil sayyorani oʻzlashtirishdagi uchta asosiy vazifani sanab oʻtdi. Marsda doimiy yashash uchun uchta asosiy shart aytildi © Depositphotos Naked Science nashri Global Times’ga tayanib yozishicha, Xitoy Fanlar akademiyasining Shanhay astronomiya observatoriyasi kichik ilmiy xodimi bu haqda «Nega biz Marsga yoʻl olyapmiz?» nomli maqolasida bayon qilgan. Birinchi vazifa - Yer va Mars oʻrtasida axborot almashinuvini taʼminlash. Bu kosmik apparatlar bilan aloqa qilish va ularning harakat yoʻnalishini aniq belgilash uchun muhim.Chjanning aytishicha, Shanhay astronomiya observatoriyasi rahbarligida ishlab chiqilgan radiointerferometriya tizimi Marsga yoʻl olgan apparatlar trayektoriyasini yuqori aniqlikda hisoblash va ularni orbitaga chiqarishga yordam beradi. Mazkur texnologiya «Tyanven-1» missiyasida sinovdan oʻtkazilgan."
#Matn endi .txt faylidan o'qiladi
if __name__ == "__main__":
    from pathlib import Path
    MatnFaylNomi = Path(__file__).resolve().parent / "InglizchaMatn.txt"  # Matn faylining nomi
    try:
        with open(MatnFaylNomi, 'r', encoding='utf-8') as fayl:
            Matn = fayl.read()
    except FileNotFoundError:
        print(f"Xatolik: '{MatnFaylNomi}' fayli topilmadi.")
        Matn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish
    TartiblanganHarfalarChastotasi=sorted(chastota_tahlil(Matn).items())
    # print(TartiblanganHarfalarChastotasi)
    #Berilgan matndagi harflar chastotasini kamayib boruvchi tartibda chiqarish
    for harf, chastota in sorted(chastota_tahlil(Matn).items(), key=lambda x: x[1], reverse=True):
        print(f"{harf}: {chastota}")
    print("Matndagi barcha harflar soni:", sum(chastota_tahlil(Matn).values()))
    print("Matndagi harflar chastotasi tahlili yakunlandi.")