"""6-amaliy: takroriy gamma va CTR nonce tahlili.
Faqat sun’iy, o‘qituvchi bergan shifrmatnlar. Python 3.10+, tashqi paket yo‘q.
6-amaliy_individual_variantlar.txt faylidan O‘Z variantingizni kiriting.
Haqiqiy AES-CTR/ChaCha20 amalga oshirilmagan; HMAC asosidagi toy model.
"""
import hashlib
import hmac

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """Teng uzunlikli ikki bayt satrining XORi; farq bo‘lsa ValueError."""
    # TODO 1
    raise NotImplementedError

def toy_pad(key: bytes, nonce: bytes, counter: int, size: int) -> bytes:
    """O‘QUV MODELI: HMAC-SHA256(key, nonce||counter_be32)[:size].
    size: 1..32, counter: 0..2**32-1. Ishlab chiqarishda shifr EMAS.
    """
    # TODO 2. hmac.new(..., hashlib.sha256).digest() dan foydalaning.
    raise NotImplementedError

def observed_xor(c1: bytes, c2: bytes) -> bytes:
    # TODO 3. Faqat mos uzunlikdagi shifrmatnlarda C1 xor C2.
    raise NotImplementedError

def recover_known(c1: bytes, c2: bytes, known_p1: bytes, offset: int=0) -> bytes:
    """P1 ning [offset:offset+len(known_p1)] baytlari ma’lum.
    Aynan shu pozitsiyadagi P2 bo‘lagini qaytaradi; ortiqcha bayt YO‘Q.
    """
    # TODO 4. offset, bo‘lak uzunligi va indeks chegaralarini tekshiring.
    raise NotImplementedError

if __name__ == '__main__':
    # TODO 5. Qo‘lda yechilgan bir bayt: A=0x41, B=0x42, Z=0x20;
    #         C1=0x61, C2=0x62, D=0x03 ni assert bilan tekshiring.
    # TODO 6. P1=b'SALOM DUNYO', P2=b'BUGUN SALOM'; sintetik Z bilan
    #         C1,C2,D hosil qiling; b'SALOM' cribini 0-offsetda tekshiring.
    # TODO 7. Bir xil key, nonce, counter=0 bo‘lsa Z1=Z2;
    #         counter=1 bo‘lsa Z o‘zgarishini sinang.
    # TODO 8. O‘z variantingiz C1,C2 va P1 prefiksini bytes.fromhex/
    #         .encode('ascii') bilan kiriting, P2 prefiksini tiklang.
    # TODO 9. Tanlangan xabar b'HELLO' ning C birinchi bitini o‘zgartiring;
    #         autentifikatsiyasiz dekodlash o‘zgarishini izohlang.
    # TODO 10. Boshqa nonce yoki counter uchun tenglikning ishlamasligini,
    #          bitta D qiymatidan ikki P ni noyob topib bo‘lmasligini yozing.
