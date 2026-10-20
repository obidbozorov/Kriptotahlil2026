# Berilgan shifrmatnni tahlil qilish. Bunda Chastotali tahlil usuli qo'llaniladi. Shifrlash uchun Sezar shifrlash usuli ishlatiladi.
from zipfile import Path

from ChastotaliAnaliz import chastota_tahlil
from SezarShifrlash import SezarDeshifrlash, SezarShifrlash
UrgatuvchiMatnlarChastotsi={}
UrgatuvchiMatnFaylNomi = "MatnlarDataset.txt"  # Matn faylining nomi
try:
    with open(UrgatuvchiMatnFaylNomi, 'r', encoding='utf-8') as fayl:
        Matn = fayl.read()
except FileNotFoundError:
    print(f"Xatolik: '{UrgatuvchiMatnFaylNomi}' fayli topilmadi.")
    Matn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish    
UrgatuvchiMatnlarChastotsi=chastota_tahlil(Matn)
#print("Namunaviy matnlar(O'zbekcha)", UrgatuvchiMatnlarChastotsi)
# TestOchiqMatn.txt faylida berilgan matnni Sezar shifrlash usuli bilan shifrlash va natijani chiqarish
TestOchiqMatnFaylNomi = "TestOchiqMatn.txt"  # Test ochiq matn faylining nomi
try:    
    with open(TestOchiqMatnFaylNomi, 'r', encoding='utf-8') as fayl:
        TestOchiqMatn = fayl.read()
except FileNotFoundError:
    print(f"Xatolik: '{TestOchiqMatnFaylNomi}' fayli topilmadi.")
    TestOchiqMatn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish  
SHifrmatn=SezarShifrlash(TestOchiqMatn, 3)  # Sezar shifrlash usuli bilan shifrlash (Kalit=3)
# Natijani faylga yozish
NatijaFaylNomi = "ShifrMatn.txt"  # Natija faylining nomi
try:    
    with open(NatijaFaylNomi, 'w', encoding='utf-8') as fayl:
        fayl.write(SHifrmatn)
except Exception as e:
    print(f"Xatolik: '{NatijaFaylNomi}' fayliga yozishda xatolik yuz berdi: {e}")
ShifrmatnFaylNomi = "ShifrMatn.txt"  # Shifr matn faylining nomi
try:
    with open(ShifrmatnFaylNomi, 'r', encoding='utf-8') as fayl:
        ShifrMatn = fayl.read()
except FileNotFoundError:
    print(f"Xatolik: '{ShifrmatnFaylNomi}' fayli topilmadi.")
    ShifrMatn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish
ShifrmatnChastotasi=chastota_tahlil(ShifrMatn)
# Ehtimoliy shifrmatnga mos ochiq matnlarni, kamayib borishida chiqaramiz
ShifrmatnChastotasiList=sorted(ShifrmatnChastotasi.items(), key=lambda x: x[1], reverse=True)
UrgatuvchiMatnlarChastotsiList=sorted(UrgatuvchiMatnlarChastotsi.items(), key=lambda x: x[1], reverse=True)
ALIFBO = "abcdefghijklmnopqrstuvwxyz"
print(type(ALIFBO))
for i in range(len(ALIFBO)):
    print(f"{i}: SM '{ShifrmatnChastotasiList[i]}' : O'M: {UrgatuvchiMatnlarChastotsiList[i]}")
for i in range(len(ALIFBO)):
    EhtimoliyKalit=( ord(ShifrmatnChastotasiList[0][0]) - ord(UrgatuvchiMatnlarChastotsiList[i][0]) ) % 26
    print(f"{i}-Ehtimoliy Kalit: {EhtimoliyKalit}: {SezarDeshifrlash(ShifrMatn, EhtimoliyKalit)[:50]}...")
