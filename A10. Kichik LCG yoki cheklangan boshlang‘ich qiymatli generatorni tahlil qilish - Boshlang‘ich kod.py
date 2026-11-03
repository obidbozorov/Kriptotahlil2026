"""10-amaliy: TODO bo'limlarini talaba to'ldiradi; faqat sintetik o'quv misollari."""
from math import gcd
import random
import secrets
import importlib.util
from pathlib import Path
_spec = importlib.util.spec_from_file_location('lab_data', Path(__file__).with_name('A10. Kichik LCG yoki cheklangan boshlang‘ich qiymatli generatorni tahlil qilish - Lab ma’lumotlari.py'))
_lab = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_lab)
VARIANTLAR, WEAK_M, WEAK_A, WEAK_C = _lab.VARIANTLAR, _lab.WEAK_M, _lab.WEAK_A, _lab.WEAK_C


def lcg_step(x, a, c, m):
    """TODO 1: X_(n+1) = (a*X_n+c) mod m. m>1 shartini tekshiring."""
    raise NotImplementedError


def recover_params(m, x1, x2, x3):
    """TODO 2: x1,x2,x3 dan (a,c) ni qaytaring.
    gcd((x2-x1) mod m, m) != 1 bo'lsa ValueError chiqaring:
    bu holda ushbu oddiy teskari-element usuli YETARLI EMAS.
    """
    raise NotImplementedError


def predict_next(m, x1, x2, x3):
    """TODO 3: (a,c,x4) ni qaytaring; x2, x3 ni qayta tekshiring."""
    raise NotImplementedError


def recover_weak_seeds(first, second, seed_range=range(32)):
    """TODO 4: ma'lum WEAK_A/C/M bilan seed nomzodlarini sanang.
    Ikki kuzatuvga mos butun sonli seedlar ro'yxatini qaytaring.
    """
    raise NotImplementedError


def bit_balance(bits):
    """TODO 5: faqat '0'/'1' satri uchun (n0,n1,absolute_difference) qaytaring;
    boshqa belgilar va bo'sh satrni ValueError bilan rad eting.
    Bu NIST SP 800-22 test to'plami EMAS.
    """
    raise NotImplementedError


def demonstrate(letter='A'):
    """TODO 6: individual variant, seed, balans va random/secrets farqini chiqaring."""
    raise NotImplementedError

if __name__ == '__main__':
    demonstrate('A')
