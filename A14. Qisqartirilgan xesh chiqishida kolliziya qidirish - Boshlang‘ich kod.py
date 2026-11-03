"""14-amaliy: qisqartirilgan SHA-256 kolliziyalari. TODO 1–6 ni to‘ldiring.
Faqat Python 3.10+ standart kutubxonasi; real hujjat imzolariga tegmang.
"""
import importlib.util
from pathlib import Path
_spec = importlib.util.spec_from_file_location('lab_data', Path(__file__).with_name('A14. Qisqartirilgan xesh chiqishida kolliziya qidirish - Lab ma’lumotlari.py'))
_lab = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_lab)
VARIANTLAR, TARGET = _lab.VARIANTLAR, _lab.TARGET
import hashlib
import math
import statistics


def short_digest(message: bytes, bits: int) -> int:
    """TODO 1. SHA-256 ning chapdagi `bits` bitini butun son qilib qaytaring.
    Eslatma: bits 12 yoki 20 bo‘lsa, yetarlicha baytni oling va ortiqcha
    O‘NG bitlarni surib tashlang. 8 <= bits <= 32 ni tekshiring.
    """
    raise NotImplementedError


def find_collision(bits: int, prefix: str, trial: int, max_tries=100000) -> dict:
    """TODO 2. m_i=(prefix+f'tajriba={trial}|i={i}').encode('utf-8').
    0<=i<max_tries tartibida birinchi turli xabarlar kolliziyasini toping.
    Natija: {'first':bytes, 'second':bytes, 'digest':int,'attempts':int}.
    Topilmasa RuntimeError; bir xil xabarni kolliziya deb hisoblamang.
    """
    raise NotImplementedError


def birthday_probability(bits: int, q: int) -> float:
    """TODO 3. Ideal, tekis n-bitli modelda yaqinlashuv:
    1-exp(-q*(q-1)/(2*2**bits)); q=0 yoki 1 -> 0.
    """
    raise NotImplementedError


def analyze_variant(label: str) -> dict:
    """TODO 4. 12 tajribani bajaring. Qaytaring:
    {'variant', 'bits', 'attempts':list[int], 'median_attempts':float,
     'q50_theory':float, 'p_at_median':float}.
    q50_theory=sqrt(2*ln(2)*2**bits) — yaqinlashuv.
    """
    raise NotImplementedError


def fixed_target_second_preimage(target: bytes, bits: int, max_tries=50000) -> dict:
    """TODO 5. Belgilangan target xabar digestiga mos BOSHQA xabar izlang.
    Nomzod = f'target-candidate|{i}'.encode('ascii'), i=0,1,... .
    Natija: {'target':bytes,'found':bytes,'attempts':int,'digest':int}.
    Topilmasa RuntimeError; faqat n=12 bitli nazorat uchun ishlating.
    """
    raise NotImplementedError


def report_summary(label: str) -> str:
    """TODO 6. analyze_variant() natijasidan q50, tajribaviy mediana
    va nazariy ehtimollikni ko‘rsatuvchi 1-2 satrli hisobot tuzing.
    """
    raise NotImplementedError


if __name__ == '__main__':
    print('Toy H(AB)=H(BA):',sum(b'AB')%16, sum(b'BA')%16)
    print('Sizning variantingiz: A (o‘qituvchi boshqasini biriktirishi mumkin)')
    print(report_summary('A'))
    print('Ikkinchi proobraz nazorati:',fixed_target_second_preimage(TARGET,12))
