"""Kriptotahlil elementlari: 1-amaliy mashg‘ulot (talaba uchun).
Faqat A-Z harflari siljitiladi; boshqa belgilar o‘zgarmaydi.
"""

def caesar(text: str, shift: int) -> str:
    natija = []
    for ch in text.upper():
        if "A" <= ch <= "Z":
            x = ord(ch) - ord("A")
            y = ...  # TODO 1: mod 26
            natija.append(chr(ord("A") + y))
        else:
            natija.append(ch)
    return "".join(natija)

if __name__ == "__main__":
    m, k = "HELLO", 3
    c = caesar(m, k)
    print("C =", c)
    print("M =", caesar(c, -k))
    # TODO 2: for sikli bilan barcha 26 ta (k, nomzod) ni chiqaring.
    # TODO 3: shifrlash va ochish tekshiruvi uchun assert yozing.
