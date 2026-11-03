"""5-amaliy: Vijener kalitini tiklash (faqat o‘quv shifrmatnlari).
Python 3.10+. "5-amaliy_individual_variantlar.txt" dan o‘z C satringizni ko‘chiring.
TODO larni to‘ldiring. Oddiy inglizcha A–Z modeli; o‘zbek tiliga ko‘chirmang.
"""
from collections import Counter, defaultdict
from math import gcd
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENGLISH_WEIGHTS = (8.17,1.49,2.78,4.25,12.70,2.23,2.02,6.09,6.97,0.15,0.77,4.03,2.41,6.75,7.51,1.93,0.10,5.99,6.33,9.06,2.76,0.98,2.36,0.15,1.97,0.07)
P = tuple(x/sum(ENGLISH_WEIGHTS) for x in ENGLISH_WEIGHTS)  # oldindan belgilangan model

def normalize(text: str) -> str:
    # TODO 1. Faqat A–Z ni qoldiring; UPPERCASE ga o‘tkazing.
    raise NotImplementedError

def vigenere(text: str, key: str, decrypt: bool=False) -> str:
    # TODO 2. C_i = (P_i + K_(i mod L)) mod 26; ochish uchun ayirish.
    # Matn va kalit tozalangan hamda bo‘sh emasligini tekshiring.
    raise NotImplementedError

def ic(text: str) -> float:
    # TODO 3. n>=2 talab qiling; Σ f_j(f_j-1) / n(n-1).
    raise NotImplementedError

def repeats(text: str, n: int=6) -> dict[str,list[int]]:
    # TODO 4. n-grammalarni boshlanish indekslari bilan jamlang;
    # faqat kamida ikki marta uchraganlarini qaytaring.
    raise NotImplementedError

def mean_column_ic(cipher: str, length: int) -> float:
    # TODO 5. cipher[j::length] ustunlari IC qiymatining o‘rtachasi.
    # Har bir ustun kamida 2 belgidan iborat bo‘lsin.
    raise NotImplementedError

def chi2_score(text: str) -> float:
    # TODO 6. Har bir A–Z uchun E_j = len(text)*P[j] va Σ(O-E)^2/E.
    # Bu SARALASH BALLI; statistik p-qiymat emas.
    raise NotImplementedError

def recover_key(cipher: str, length: int) -> tuple[str,str]:
    # TODO 7. Har bir j ustunda 26 ta ochish siljishini chi2 bo‘yicha
    # saralang, eng kichik ballli siljishlardan K ni tuzing va C ni oching.
    raise NotImplementedError

if __name__ == '__main__':
    print('Namuna: ATTACKATDAWN + LEMON => LXFOPVEFRNHR')
    # TODO 8. Namuna shifrlash/ochish, IC("AABBC")=0.2 ni assert bilan tekshiring.
    # TODO 9. P="ATTACKNOWXATTACKATDAWNXXXATTACK", K="LEMON":
    #         6 belgili LXFOPV bo‘lagining boshlanishlarini, masofalarni
    #         va masofalar EKUBini hisoblang. EKUB = 5 — nomzod, ISBOT EMAS.
    # TODO 10. O‘z variantingiz C ni fayldan oling; L=2..12 uchun o‘rtacha IC
    #          jadvalini tuzing; Kaziski bilan L ni asoslang.
    # TODO 11. K va M ni toping; vigenere(M,K)==C ni assert qiling.
    # TODO 12. M[:120] ni o‘qing, barcha 26 siljishdan faqat bittasi nega
    #          avtomatik to‘g‘ri bo‘lmasligini va L karrasi ICsini izohlang.
