# Ko'p alifboli shifrlasr (Vijiner shifri) uchun Kaztitskiy testini amalga oshirish. Bunda chastotali tahlil usuli qo'llaniladi.
from ChastotaliAnaliz import chastota_tahlil
try:
    with open("MatnlarDataset.txt", 'r', encoding='utf-8') as fayl:
        Matnlar = fayl.read()
except FileNotFoundError:
    print(f"Xatolik: 'MatnlarDataset.txt' fayli topilmadi.")
    Matnlar = ""  # Fayl topilmasa, bo'sh matn bilan davom etish
chastota_ochiq_matnlar=chastota_tahlil(Matnlar)
SummaHarflarSonlari=sum(chastota_ochiq_matnlar.values())
# Chastotani normallashtirish
chatotaniNormallashtirish = {harf: chastota / SummaHarflarSonlari for harf, chastota in chastota_ochiq_matnlar.items()}
#print("Chastotani normallashtirish:", chatotaniNormallashtirish) 
