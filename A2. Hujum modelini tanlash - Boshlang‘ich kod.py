"""2-amaliy: Hujum modellari va kichik kalit fazosida to‘liq qidiruv.
FAQAT o‘quv XOR modeli. Haqiqiy servislar va begona ma’lumotlarda sinamang.
Python 3.10+; tashqi paketlar kerak emas.
"""
from statistics import median
from time import perf_counter_ns


def xor_encrypt(m: int, k: int, bits: int = 8) -> int:
    """0 <= m,k < 2**bits bo‘lishi kerak."""
    assert 1 <= bits <= 16
    assert 0 <= m < (1 << bits) and 0 <= k < (1 << bits)
    # TODO 1: m va k ni XOR yordamida birlashtiring.
    return ...


def exhaustive_search(m: int, c: int, bits: int = 8) -> tuple[list[int], int]:
    """BARCHA kalitlarni tekshiring; (mos kalitlar, sinovlar soni) qaytaring."""
    matches = []
    trials = 0
    # TODO 2: 0 dan 2**bits-1 gacha barcha kalitlarni tekshiring.
    # TODO 3: trials ni hisoblang va mos kalitni matches ga qo‘shing.
    return matches, trials


def benchmark(bits: int, repeats: int = 5) -> tuple[int, float]:
    """To‘liq skan uchun median vaqtni millisekundda qaytaring."""
    m = 0x53 & ((1 << bits) - 1)
    k = 0xA7 & ((1 << bits) - 1)
    c = xor_encrypt(m, k, bits)
    times_ms = []
    for _ in range(repeats):
        start = perf_counter_ns()
        _, trials = exhaustive_search(m, c, bits)
        times_ms.append((perf_counter_ns() - start) / 1_000_000)
    return trials, median(times_ms)


if __name__ == "__main__":
    m = 0x53
    k_teacher_demo = 0xA7  # FAQAT umumiy namuna; individual variant kalitini kodga yozmang.
    c = xor_encrypt(m, k_teacher_demo)
    found, trials = exhaustive_search(m, c)
    print(f"O‘quv misol: M=0x{m:02X}, C=0x{c:02X}")
    print(f"Mos kalitlar: {[hex(v) for v in found]}; sinovlar: {trials}")
    # TODO 4: kalitni arifmetik, ya’ni XOR orqali bevosita tiklab tekshiring.
    # TODO 5: bits = 4, 8, 12, 16 uchun N, sinovlar va median vaqt jadvalini chiqaring.
    # TODO 6: mustaqil variant uchun M va C ni kiriting, k ni natijadan toping.
