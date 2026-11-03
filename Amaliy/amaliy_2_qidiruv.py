"""2-amaliy mashg'ulot: kichik kalit fazosida to'liq qidiruv."""
from statistics import median
from time import perf_counter


def encrypt(x, key, b):
    return (x + key) % (1 << b)


def search(x, c, b):
    if not 1 <= b <= 20:
        raise ValueError("b 1 dan 20 gacha bo'lsin")
    n = 1 << b
    if not (0 <= x < n and 0 <= c < n):
        raise ValueError("x va c 0 dan N-1 gacha bo'lsin")
    start = perf_counter()
    for key in range(n):
        if encrypt(x, key, b) == c:
            return key, key + 1, perf_counter() - start
    raise RuntimeError("Mos kalit topilmadi")


def measure(x, c, b, repeats=5):
    search(x, c, b)  # Dastlabki ishga tushirish o'lchanmaydi
    times = []
    for _ in range(repeats):
        key, attempts, elapsed = search(x, c, b)
        times.append(elapsed)
    return key, attempts, median(times)


def main():
    # Individual variant uchun faqat b, x, c ni almashtiring.
    b, x, c = 8, 42, 215
    key, attempts, seconds = measure(x, c, b)
    print(f"Namuna: k={key}, J={attempts}, t={seconds:.8f} s")
    print(f"Tekshiruv: E(x,k)={encrypt(x, key, b)}, c={c}")
    print("b; N; kalit o'rni; k; J; median_s; kalit_per_s")
    for b in (8, 12, 16):
        n, x = 1 << b, 42
        for label, fixture_key in (
            ("birinchi", 0), ("orta", n // 2), ("oxirgi", n - 1)
        ):
            # Kalit faqat tajriba ma'lumotini tayyorlash uchun.
            c = encrypt(x, fixture_key, b)
            key, attempts, seconds = measure(x, c, b)
            assert key == fixture_key and attempts == fixture_key + 1
            rate = attempts / seconds if seconds > 0 else float("inf")
            print(f"{b}; {n}; {label}; {key}; {attempts}; "
                  f"{seconds:.8f}; {rate:.1f}")


if __name__ == "__main__":
    main()
