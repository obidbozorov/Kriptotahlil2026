"""3-amaliy: entropiya va mutlaqo maxfiylik — sintetik OTP modeli.
Python 3.10+. Tashqi kutubxona talab qilinmaydi.
TODO vazifalarni yakunlang; natijalarni matematik jihatdan izohlang.
"""
from math import log2

def otp_xor(m: int, k: int, bits: int = 4) -> int:
    """0 <= m,k < 2**bits. Shifrlash ham, deshifrlash ham XOR."""
    assert 1 <= bits <= 8
    assert 0 <= m < (1 << bits) and 0 <= k < (1 << bits)
    # TODO 1: bitma-bit XOR natijasini qaytaring.
    return ...

def shannon_entropy(probs: list[float]) -> float:
    """Diskret taqsimotning H(X) entropiyasi, bitlarda."""
    assert probs and all(p >= 0 for p in probs)
    assert abs(sum(probs) - 1.0) < 1e-9
    # TODO 2: p=0 hadni tashlab, -sum(p*log2(p)) ni hisoblang.
    return ...

def conditional_cipher_prob(m: int, c: int, key_probs: list[float]) -> float:
    """P(C=c | M=m) = P(K=m XOR c) (qat'iy n bitli OTP)."""
    n = len(key_probs)
    assert n >= 2 and n & (n - 1) == 0
    assert 0 <= m < n and 0 <= c < n
    # TODO 3: berilgan m,c ga mos YAGONA kalit ehtimolini qaytaring.
    return ...

def posterior_given_cipher(prior: list[float], key_probs: list[float], c: int) -> list[float]:
    """P(M=m | C=c), Bayes bo'yicha; 0 ehtimolli C ni qabul qilmang."""
    assert len(prior) == len(key_probs) and abs(sum(prior)-1)<1e-9
    weights = [prior[m] * conditional_cipher_prob(m, c, key_probs)
               for m in range(len(prior))]
    total = sum(weights)
    assert total > 0
    # TODO 4: weights ni total ga bo'lib normallashtiring.
    return ...

def recover_second(m1: int, c1: int, c2: int) -> int:
    """Kalit TAKROR qo'llanganda M1 ma'lum bo'lsa, M2 ni tiklang."""
    # TODO 5: C1 XOR C2 = M1 XOR M2 dan foydalaning.
    return ...

def uniqueness_distance(Hk: float, q: int, h: float) -> tuple[float, float, float]:
    """Alohida, IDEALLASHTIRILGAN klassik model: (r bit/belgi,R ulush,U belgi)."""
    assert q >= 2 and Hk >= 0 and 0 <= h < log2(q)
    # TODO 6: r=log2(q)-h; R=r/log2(q); U=Hk/r.
    return ...

if __name__ == '__main__':
    m1, k, m2 = 0b1011, 0b0110, 0b0011  # faqat umumiy namuna
    c1, c2 = otp_xor(m1,k), otp_xor(m2,k)
    print('C1:',format(c1,'04b'),'C2:',format(c2,'04b'))
    print('M1:',format(otp_xor(c1,k),'04b'))
    print("M2 (M1 ma’lum):",format(recover_second(m1,c1,c2),'04b'))
    # TODO 7: barcha 16 ta m,c uchun uniform kalitda P(C=c|M=m)=1/16 ekanini tekshiring.
    # TODO 8: prior=[0.1,0.2,0.3,0.4], uniform key=[0.25]*4, c=0 bo'lsa posterior=prior.
    # TODO 9: prior=[0.25]*4, biased key=[0.5,0.25,0.125,0.125], c=0 uchun posterior.
    # TODO 10: H(K), H_min(K), r, R, U natijasini birliklari bilan chiqaring.
    # TODO 11: o'z variantingizning M1,C1,C2 uchligidan K va M2 ni aniqlang.
