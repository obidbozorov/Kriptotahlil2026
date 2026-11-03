"""12-amaliy: faqat kichik sun’iy RSA! TODOlarni to‘ldiring. Python 3.10+."""
from math import gcd
import importlib.util
from pathlib import Path
_spec = importlib.util.spec_from_file_location('lab_data', Path(__file__).with_name('A12. To‘ldirishsiz RSA imzosini qalbakilashtirishning o‘quv misoli - Lab ma’lumotlari.py'))
_lab = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_lab)
VARIANTLAR = _lab.VARIANTLAR

def verify_raw(message, signature, e, n):
    """TODO 1: 0<=message,signature<n oraliq va s**e mod n == m."""
    raise NotImplementedError

def forge_without_oracle(chosen_sig, e, n):
    """TODO 2: yopiq kalitsiz yangi (m,s) juftligi; (m,s) qaytaring."""
    raise NotImplementedError

def create_blinded_query(target, r, e, n):
    """TODO 3: gcd(target,n)=gcd(r,n)=1 ni tekshiring; m' ni qaytaring."""
    raise NotImplementedError

def recover_signature(oracle_sig, r, n):
    """TODO 4: r teskari elementi orqali maqsadli imzoni tiklang."""
    raise NotImplementedError

def analyze_variant(label):
    """TODO 5: m' ni oldindan berilgan oracle_query bilan tekshiring;
    oracle_sig ni aynan m' uchun tekshiring, m uchun tiklangan imzoni
    tekshiring; natijalar lug‘atini qaytaring.
    """
    raise NotImplementedError

if __name__ == '__main__':
    print(analyze_variant('A'))
