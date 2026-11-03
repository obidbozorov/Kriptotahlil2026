"""12-amaliy: haqiqiy RSA-PSS API namoyishi; bu PSS hujumi emas.
Kutubxona: pip install cryptography (mavjud bo‘lmasa import xabari chiqadi).
"""
try:
    from cryptography.hazmat.primitives.asymmetric import rsa,padding
    from cryptography.hazmat.primitives import hashes
    from cryptography.exceptions import InvalidSignature
except ImportError as exc:
    raise SystemExit('cryptography kutubxonasi kerak: pip install cryptography') from exc

def test_pss():
    private = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    public = private.public_key()
    pad = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32)
    message = b'Universitet: laboratoriya 12'
    signature = private.sign(message,pad,hashes.SHA256())
    def valid(data, sig):
        try:
            public.verify(sig,data,pad,hashes.SHA256())
            return True
        except InvalidSignature:
            return False
    result={'asl':valid(message,signature), 'ozgargan':valid(message+b'!',signature),
            'buzilgan_imzo':valid(message,signature[:-1]+bytes([signature[-1]^1]))}
    assert result=={'asl':True,'ozgargan':False,'buzilgan_imzo':False}
    print('RSA-PSS:',result,'| modul biti:',private.key_size)
    return result

if __name__=='__main__':test_pss()
