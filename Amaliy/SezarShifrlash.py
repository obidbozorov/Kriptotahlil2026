def SezarShifrlash(Matn, Kalit):
    ShifrlanganMatn = ""
    Matn = Matn.lower()  # Matnni kichik harflarga o'tkazish
    for harf in Matn:
        if harf in "abcdefghijklmnopqrstuvwxyz":
            if harf.islower():
                ShifrlanganHarf = chr((ord(harf) - 97 + Kalit) % 26 + 97)
            else:
                ShifrlanganHarf = chr((ord(harf) - 97 + Kalit) % 26 + 97)
            ShifrlanganMatn += ShifrlanganHarf
        else:
            ShifrlanganMatn += harf
    return ShifrlanganMatn
def SezarDeshifrlash(ShifrMatn, Kalit):
    DeshifrlanganMatn = ""
    ShifrMatn = ShifrMatn.lower()  # Matnni kichik harflarga o'tkazish
    for harf in ShifrMatn:
        if harf in "abcdefghijklmnopqrstuvwxyz":
            if harf.islower():
                DeshifrlanganHarf = chr((ord(harf) - 97 - Kalit) % 26 + 97)
            else:
                DeshifrlanganHarf = chr((ord(harf) - 97 - Kalit) % 26 + 97)
            DeshifrlanganMatn += DeshifrlanganHarf
        else:
            DeshifrlanganMatn += harf
    return DeshifrlanganMatn
