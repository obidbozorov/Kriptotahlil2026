# Bu yerda shifrlangan matnni chastotali tahlil qilish uchun dastur yozilgan. Kriptotahlilda foydalaniladi
from ChastotaliAnaliz import chastota_tahlil
from SezarShifrlash import SezarShifrlash
TajribMatnFaylNomi = "MatnlarDataset.txt"  # Tajriba matn faylining nomi
try:    
    with open(TajribMatnFaylNomi, 'r', encoding='utf-8') as fayl:
        TajribMatn = fayl.read()    
except FileNotFoundError:
    print(f"Xatolik: '{TajribMatnFaylNomi}' fayli topilmadi.")
    TajribMatn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish
TajribaChastotasi=chastota_tahlil()
TestOchiqMatnFaylNomi = "TestOchiqMatn.txt"  # Test ochiq matn faylining nomi
try:
    with open(TestOchiqMatnFaylNomi, 'r', encoding='utf-8') as fayl:
        TestOchiqMatn = fayl.read()
except FileNotFoundError:
    print(f"Xatolik: '{TestOchiqMatnFaylNomi}' fayli topilmadi.")
    TestOchiqMatn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish
TestOchiqMatnShiflranganVarianti=SezarShifrlash(TestOchiqMatn, 7)  # Test ochiq matnni Sezar shifrlash bilan shifrlash
# SHifrlangan Man .txt fayliga yozish
try:
    with open("ShifrlanganMatn.txt", 'w', encoding='utf-8') as fayl:
        fayl.write(TestOchiqMatnShiflranganVarianti)
except Exception as e:
    print(f"Xatolik: Shifrlangan matnni faylga yozishda xatolik yuz berdi: {e}") 
SHifrlanganMatnFaylNomi = "ShifrlanganMatn.txt"  # Shifrlangan matn faylining nomi
try:
    with open(SHifrlanganMatnFaylNomi, 'r', encoding='utf-8') as fayl:
        ShifrlanganMatn = fayl.read()   
except FileNotFoundError:
    print(f"Xatolik: '{SHifrlanganMatnFaylNomi}' fayli topilmadi.")
    ShifrlanganMatn = ""  # Fayl topilmasa, bo'sh matn bilan davom etish
