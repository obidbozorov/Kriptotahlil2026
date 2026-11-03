"""9-amaliy: talaba to'ldiradigan kod; faqat mahalliy o'quv muhiti."""
from collections import Counter
from time import perf_counter
import importlib.util
from pathlib import Path
_spec = importlib.util.spec_from_file_location('lab_data', Path(__file__).with_name('A9. ECB takrorlarini aniqlash - Lab ma’lumotlari.py'))
_lab = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_lab)
VARIANTLAR, oracle, authenticated_oracle = _lab.VARIANTLAR, _lab.oracle, _lab.authenticated_oracle

BLOCK = 4  # haqiqiy AES blok o'lchami EMAS!

def split_blocks(cipher_hex):
    """TODO 1. Hex matnni BLOCK baytli bloklarga ajrating; noto'g'ri uzunlikni rad eting."""
    raise NotImplementedError

def repetition_report(cipher_hex):
    """TODO 2. Takroriy bloklar soni va indeks juftliklarini chiqaring.
    Qaytarish: (takroriy_juftlar_soni, [(i,j), ...]).
    """
    raise NotImplementedError

def xor_bytes(a, b):
    """TODO 3. Teng uzunlikli baytlar uchun XOR; teng bo'lmasa ValueError."""
    raise NotImplementedError

def recover_last_byte(letter):
    """TODO 4. FAQAT birinchi blokning OXIRGI paddinglangan baytini tiklang.
    v=0..255 orqali IV[-1] qiymatini sinang; IV[-2] ni XOR 1 va XOR 2 qilib
    ikki marta so'rang (pad=2 yoki 3 tasodifiy mosligini bartaraf etish).
    Padding 0x01 bo'lganda: P[-1] = v XOR asl_IV[-1] XOR 1.
    Natija: (oxirgi_bayt, oracle_so'rovlari_soni, sinovda_topilgan_v).
    """
    raise NotImplementedError

def demonstrate(letter='A'):
    """TODO 5. ECB bloklari, oracle va autentifikatsiya nazoratini solishtiring."""
    raise NotImplementedError

if __name__ == '__main__':
    demonstrate('A')
