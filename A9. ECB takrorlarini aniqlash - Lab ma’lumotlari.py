# 9-amaliy: faqat MAHALLIY o'quv oracle. Haqiqiy AES yoki tayyor kriptografiya EMAS.
# Laboratoriya modeli: 4 baytli bijektiv o'quv almashtirish, CBC, PKCS#7 va HMAC.
# Kod ochiq bo'lsa ham hujum tajribasida ichki kalit/ochiq matnni O'QIMANG;
# oracle(variant, iv_hex, ciphertext_hex) javobinigina kuzating.
import hashlib
import hmac

BLOCK = 4

VARIANTLAR = {
    'A': {'iv': '13bd3be8', 'cipher': 'b009a759', 'tag': 'f731f737392d883b6f3f51f78a0b02cb7ec65acd116c03823db762cd97c8ba80', 'ecb': '570e544c570e544c62195f57'},
    'B': {'iv': 'dec31e12', 'cipher': '1d42a6b9', 'tag': '8be0236b500b97a0adff9008ea8face32be15a3c8e0d04f5e75b7728bf861172', 'ecb': 'dfddc820e9e14b22dfddc820'},
    'C': {'iv': '92eca55f', 'cipher': '552d1f64', 'tag': 'b1eae071c2ef4d0cbc42a3cc158954f03e0873b88093d0581fa37cbe4e9d5f4f', 'ecb': '9a6390a21a6390a79a6390a2'},
    'D': {'iv': '29b2ee31', 'cipher': 'ce090662', 'tag': '1753d6c7b4bb889f6c3ac669fcd1388423c63f16ca815faa577227b72de625de', 'ecb': 'f1b60f58f1b60f58f3bf9654'},
    'E': {'iv': '981a8763', 'cipher': 'b7f11a0e', 'tag': 'acb13f0ba25dfec2563854b765a4bbf3343210455af0e2def514aacbfc2f39be', 'ecb': 'd2d10ccbd2d10ccb4fd88e4d'},
    'F': {'iv': '0541789e', 'cipher': '8332646d', 'tag': '106e2e4ffa95c0a5652d6209500dbd34fe74c9537ef151d0514a3f24d7138864', 'ecb': '2fbd417123bf356b2fbd4171'},
    'G': {'iv': '342eebc1', 'cipher': '6bac06f4', 'tag': '9d2a99bf32c42bd4f1d6fce8c2de300ba4d64822b238ff8b84b835a58cc5bb01', 'ecb': '5f614ed85f614ed8e2604762'},
    'H': {'iv': '7469300d', 'cipher': 'e36429cc', 'tag': 'f9954fa367ff5f6aff113a9155c1a18233422c7600a63c00cf65bfbd4751f682', 'ecb': '74dd4cd979dfcf6274dd4cd9'},
}

def _key(letter):
    return int.from_bytes(hashlib.sha256(b'lab-9-block-key/' + letter.encode()).digest()[:4], 'big')

def _mac_key(letter):
    return hashlib.sha256(b'lab-9-mac-key/' + letter.encode()).digest()

def _rotr32(x, n):
    return ((x >> n) | (x << (32-n))) & 0xffffffff

def _decrypt_block(block, letter):
    x = _rotr32(int.from_bytes(block, 'big'), 7)
    return ((x - _key(letter)) & 0xffffffff).to_bytes(4, 'big')

def _valid_pkcs7(block):
    if len(block) != BLOCK:
        return False
    p = block[-1]
    return 1 <= p <= BLOCK and block[-p:] == bytes([p]) * p

def oracle(letter, iv_hex, ciphertext_hex):
    """O'quvdagi zaif javob: padding to'g'ri bo'lsa True, aks holda False."""
    if letter not in VARIANTLAR:
        return False
    try:
        iv, cipher = bytes.fromhex(iv_hex), bytes.fromhex(ciphertext_hex)
        if len(iv) != BLOCK or len(cipher) != BLOCK:
            return False
        plain_padded = bytes(a ^ b for a, b in zip(_decrypt_block(cipher, letter), iv))
        return _valid_pkcs7(plain_padded)
    except (ValueError, TypeError):
        return False

def authenticated_oracle(letter, iv_hex, ciphertext_hex, tag_hex):
    """Faqat o'quv EtM nazorati: avval HMAC, keyin padding; bitta umumiy javob."""
    if letter not in VARIANTLAR:
        return 'REJECT'
    try:
        iv, cipher, tag = bytes.fromhex(iv_hex), bytes.fromhex(ciphertext_hex), bytes.fromhex(tag_hex)
        if len(iv) != BLOCK or len(cipher) != BLOCK or len(tag) != 32:
            return 'REJECT'
        expected = hmac.digest(_mac_key(letter), iv + cipher, 'sha256')
        if not hmac.compare_digest(tag, expected):
            return 'REJECT'
        return 'ACCEPT' if oracle(letter, iv_hex, ciphertext_hex) else 'REJECT'
    except (ValueError, TypeError):
        return 'REJECT'

if __name__ == '__main__':
    v = VARIANTLAR['A']
    print('A: asl padding mosmi?', oracle('A', v['iv'], v['cipher']))
    print("A: asli autentifikatsiyadan o\'tadimi?", authenticated_oracle('A', v['iv'], v['cipher'], v['tag']))
