"""10-amaliy. O'qituvchi tayyorlagan SINTETIK variantlar. Haqiqiy kalitlar yo'q."""
VARIANTLAR = {
    'A': {'m': 257, 'x1': 29, 'x2': 104, 'x3': 72, 'weak_y1': 21, 'weak_y2': 106},
    'B': {'m': 257, 'x1': 64, 'x2': 92, 'x3': 232, 'weak_y1': 36, 'weak_y2': 181},
    'C': {'m': 257, 'x1': 113, 'x2': 63, 'x3': 227, 'weak_y1': 51, 'weak_y2': 0},
    'D': {'m': 257, 'x1': 202, 'x2': 225, 'x3': 221, 'weak_y1': 66, 'weak_y2': 75},
    'E': {'m': 257, 'x1': 22, 'x2': 100, 'x3': 86, 'weak_y1': 81, 'weak_y2': 150},
    'F': {'m': 257, 'x1': 149, 'x2': 46, 'x3': 94, 'weak_y1': 96, 'weak_y2': 225},
    'G': {'m': 257, 'x1': 1, 'x2': 116, 'x3': 245, 'weak_y1': 111, 'weak_y2': 44},
    'H': {'m': 257, 'x1': 170, 'x2': 164, 'x3': 26, 'weak_y1': 126, 'weak_y2': 119},
}
# Alohida zaif-seed modeli: X_{n+1} = (5*X_n + 1) mod 256; seed 0..31.
WEAK_M, WEAK_A, WEAK_C = 256, 5, 1
