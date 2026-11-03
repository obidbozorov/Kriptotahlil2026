"""11-amaliy | Talaba kodi: TODO qismlarini to'ldiring. Python 3.10+.
Faqat o'qituvchi taqdim etgan kichik sintetik RSA misollari.
"""
from math import gcd, isqrt
import importlib.util
from pathlib import Path
_spec = importlib.util.spec_from_file_location('lab_data', Path(__file__).with_name('A11. RSA umumiy modul va Viner hujumlarini kichik parametrli misollarda tayyor andoza bilan bajarish - Lab ma’lumotlari.py'))
_lab = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_lab)
VARIANTLAR = _lab.VARIANTLAR


def extended_gcd(a, b):
    """TODO 1: (g,x,y) qaytaring; a*x+b*y=g=gcd(a,b), g>=0."""
    raise NotImplementedError


def signed_mod_power(value, exponent, modulus):
    """TODO 2: exponent<0 bo'lsa inversni tekshirib pow() dan foydalaning.
    modulus>1, 0<=value<modulus; teskari yo'q bo'lsa ValueError.
    """
    raise NotImplementedError


def common_modulus(n, e1, e2, c1, c2):
    """TODO 3: gcd(e1,e2)==1 va invers shartlari; (m,a,b) qaytaring.
    Diqqat: bir xil m ishlatilgani berilgan vaziyat SHARTI, ochiq kalitdan
    yoki c1,c2 dan mustaqil isbotlab bo'lmaydi.
    """
    raise NotImplementedError


def continued_fraction(num, den):
    """TODO 4: num/den oddiy zanjir kasrning butun koeffitsiyentlari ro'yxati."""
    raise NotImplementedError


def convergents(coeffs):
    """TODO 5: zanjir kasr yaqinlashuvlarini (k,d) juftliklar ro'yxati qiling."""
    raise NotImplementedError


def wiener_attack(e, n):
    """TODO 6: e/n zanjir kasr yaqinlashuvlari bo'yicha tekshiring.
    To'g'ri bo'lsa (d,p,q) (p<=q); bo'lmasa None qaytaring.
    Kandidat k=0 ni o'tkazing. phi=(e*d-1)//k;
    s=n-phi+1; delta=s*s-4*n; delta mukammal kvadrat bo'lishi shart.
    p*q=n va e*d mod phi=1 ni QAYTA TEKSHIRING.
    """
    raise NotImplementedError


def demonstrate(letter='A'):
    """TODO 7: tanlangan variantni ikkala usul bilan ochib, tekshiruvlarni chiqaring."""
    raise NotImplementedError


if __name__=='__main__':
    demonstrate('A')
