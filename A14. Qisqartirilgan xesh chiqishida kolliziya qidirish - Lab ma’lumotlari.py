"""14-amaliy: faqat sintetik o‘quv xabarlari; javob kalitlari yo‘q.
N-bitli digest = SHA-256 ning ENG CHAP n biti, to‘liq SHA-256 emas.
"""
VARIANTLAR = {'A': {'bits': 12, 'prefix': 'oquv-a-2026|', 'trials': 12}, 'B': {'bits': 16, 'prefix': 'oquv-b-2026|', 'trials': 12}, 'C': {'bits': 20, 'prefix': 'oquv-c-2026|', 'trials': 12}, 'D': {'bits': 24, 'prefix': 'oquv-d-2026|', 'trials': 12}, 'E': {'bits': 12, 'prefix': 'oquv-e-2026|', 'trials': 12}, 'F': {'bits': 16, 'prefix': 'oquv-f-2026|', 'trials': 12}, 'G': {'bits': 20, 'prefix': 'oquv-g-2026|', 'trials': 12}, 'H': {'bits': 24, 'prefix': 'oquv-h-2026|', 'trials': 12}}
TARGET = b"oldindan-belgilangan-xabar"
