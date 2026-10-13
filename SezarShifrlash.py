def SezarShifrlash(Matn, Kalit):
    ShifrlanganMatn = ""
    Matn = Matn.lower()  # Matnni kichik harflarga o'tkazish
    for harf in Matn:
        if harf.isalpha():
            if harf.islower():
                ShifrlanganHarf = chr((ord(harf) - 97 + Kalit) % 26 + 65)
            else:
                ShifrlanganHarf = chr((ord(harf) - 97 + Kalit) % 26 + 97)
            ShifrlanganMatn += ShifrlanganHarf
        else:
            ShifrlanganMatn += harf
    return ShifrlanganMatn
