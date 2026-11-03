"""13-amaliy. DDT/LAT: TODO 1–6 ni to‘ldiring. Faqat Python 3.10+.
Sun’iy 4-bitli S-bloklar, real DES/AES kalitlarini tiklash emas.
"""
import importlib.util
from pathlib import Path
_spec = importlib.util.spec_from_file_location('lab_data', Path(__file__).with_name('A13. 4 bitli S-blok uchun DDT va LAT jadvallarini hisoblash - Lab ma’lumotlari.py'))
_lab = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_lab)
PRESENT, P, VARIANTLAR = _lab.PRESENT, _lab.P, _lab.VARIANTLAR

def parity(x: int) -> int:
    """TODO 1: x dagi o‘rnatilgan bitlar soni mod 2 (0 yoki 1)."""
    raise NotImplementedError

def ddt_table(sbox):
    """TODO 2: DDT[a][b] = #{x: S(x)^S(x^a)=b}; 16×16 sonli jadval."""
    raise NotImplementedError

def lat_table(sbox):
    """TODO 3: LAT[alpha][beta] = tenglik_soni - 8; WALSH EMAS."""
    raise NotImplementedError

def check_tables(sbox, ddt, lat):
    """TODO 4: bijektivlik; har DDT qatori 16; DDT[0][0]=16;
    a!=0 uchun DDT[a][0]=0; LAT[0][0]=8;
    har LAT qatorida kvadrat yig‘indi 64. Xato bo‘lsa ValueError.
    To‘g‘ri bo‘lsa True qaytaring.
    """
    raise NotImplementedError

def analyze_variant(label):
    """TODO 5: individual variant uchun ddt/lat tuzing; tekshiring;
    quyidagi kalitlar bilan natija lug‘atini qaytaring:
    variant, ddt_count, diff_probability, lat_value,
    linear_probability, signed_bias, max_diff_probability, max_abs_bias.
    Maxlarda trivial a=0 yoki alpha=0,beta=0 ni hisoblamang.
    """
    raise NotImplementedError

def mini_spn_difference(x, x2):
    """TODO 6: ikki PRESENT S-bloki parallel: S(x>>4), S(x&15),
    so‘ng P[i] kirish bitining CHIQISH pozitsiyasi; (kirish_farqi,
    s_qatlam_farqi, p_qatlam_farqi) ni qaytaring.
    """
    raise NotImplementedError

if __name__ == '__main__':
    print('1-misol: DDT[1][7]=', ddt_table(PRESENT)[1][7])
    print('1-misol: LAT[1][5]=', lat_table(PRESENT)[1][5])
    print('A varianti:', analyze_variant('A'))
    print('mini-SPN:', mini_spn_difference(0x60,0x70))
