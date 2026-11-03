"""4-amaliy: monoalifboli shifrning chastotaviy tahlili.
4 belgili SUN'IY o'quv modeli (haqiqiy o'zbek tili emas).
Python 3.10+; tashqi kutubxona talab qilinmaydi.
TODO funksiyalarni to'ldiring va o'z variantingizni sinang.
"""
from collections import Counter
from hashlib import sha256
from math import gcd

ABC = "ABCD"
P = dict(zip(ABC, (0.4, 0.3, 0.2, 0.1)))  # mustaqil etalon model

def normalize(text: str) -> str:
    """FAQAT A-D belgilarini qoldiring; boshqa belgilar modelga kirmaydi."""
    # TODO 1: text.upper() dan ABC ga kiradigan belgilarni birlashtiring.
    return ...

def shift(text: str, k: int) -> str:
    """To'rt belgili Sezar shifri: k mod 4; text allaqachon A-D."""
    assert text and all(ch in ABC for ch in text)
    # TODO 2: indeksni (indeks+k) % 4 ga almashtiring.
    return ...

def chi2_score(text: str) -> float:
    """χ² saralash BALLI, p-qiymat emas. Etalon P o'zgartirilmaydi."""
    assert text and all(ch in ABC for ch in text)
    obs = Counter(text)
    n = len(text)
    # TODO 3: sum((obs[ch] - n*P[ch])**2/(n*P[ch]) for ch in ABC)
    return ...

def rank_caesar(cipher: str) -> list[tuple[float, int, str]]:
    """(ball, shifrlash kaliti, nomzod matn) kichik balldan saralansin."""
    assert cipher and all(ch in ABC for ch in cipher)
    # TODO 4: k=0..3, ochish uchun shift(cipher,-k).
    return ...

def affine(text: str, a: int, b: int, decrypt: bool = False) -> str:
    """4 harfli affin shifr: a faqat 1 yoki 3 (mod 4)."""
    assert text and all(ch in ABC for ch in text)
    if gcd(a, 4) != 1:
        raise ValueError("a va 4 o'zaro tub bo'lishi shart")
    # TODO 5: shifrlash y=(a*x+b)%4, ochish x=a^{-1}*(y-b)%4.
    return ...

def pattern_match(cipher_fragment: str, plain_guess: str) -> bool:
    """Bir qiymatli almashtirishga moslik (KALIT ISBOTI EMAS)."""
    if len(cipher_fragment) != len(plain_guess):
        return False
    # TODO 6: ikkala yo'nalish uchun moslik lug'ati tuzing.
    return ...

if __name__ == "__main__":
    sample = "A"*8 + "B"*5 + "C"*5 + "D"*2
    sample_cipher = shift(sample, 1)
    print("Namuna kutilgan: eng kichik χ² ≈ 0.4167 va k = 1")
    # TODO 7: namuna uchun 4 kalitning χ² balini chiqaring.
    # TODO 8: A/B/C/D...H ichidan O'Z variantingiz shifrmatnini kiriting.
    # TODO 9: birinchi nomzodning SHA-256 dastlabki 12 hex belgisi
    #          variant jadvalidagi nazorat kodi bilan mosligini tekshiring.
    #          Bu nazorat kodi O'QUV tekshiruv vositasi; real hujum oracle'i emas.
    # TODO 10: qisqa teng-chastotali "AABBCCDD" da k=0..3 bir xil
    #           χ² berishini ko'rsating; nega kalitni ajratib bo'lmaydi?
    # TODO 11: affine("ABCD", 3, 1) va teskari amalni tekshiring.
    # TODO 12: "ASSALOM" ning takror naqshini qanday saqlanishini yozing;
    #           4 harfli model bilan real o'zbekchani aralashtirmang.
