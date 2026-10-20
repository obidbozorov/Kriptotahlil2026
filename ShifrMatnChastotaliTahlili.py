from pathlib import Path
from ChastotaliAnaliz import chastota_tahlil
from SezarShifrlash import SezarShifrlash

PAPKA = Path(__file__).resolve().parent


def chastotali_tahlil_va_tiklash(TajribaChastotasi, ShifrlanganMatn):
    """Harflarni chastota tartibi orqali taxminiy moslash."""
    shifr_chastotasi = chastota_tahlil(ShifrlanganMatn)
    if not TajribaChastotasi or not shifr_chastotasi:
        raise ValueError("Ikkala matnda ham a-z harflari bo'lishi kerak.")
    tajriba_harflari = sorted(TajribaChastotasi, key=TajribaChastotasi.get, reverse=True)
    tajriba_harflari += [h for h in "abcdefghijklmnopqrstuvwxyz" if h not in TajribaChastotasi]
    shifr_harflari = sorted(shifr_chastotasi, key=shifr_chastotasi.get, reverse=True)
    almashtirish = dict(zip(shifr_harflari, tajriba_harflari))
    return "".join(almashtirish.get(h.lower(), h) for h in ShifrlanganMatn)


def main():
    try:
        tajriba_matni = (PAPKA / "MatnlarDataset.txt").read_text(encoding="utf-8-sig")
        ochiq_matn = (PAPKA / "TestOchiqMatn.txt").read_text(encoding="utf-8-sig")
        tajriba_chastotasi = chastota_tahlil(tajriba_matni)
        shifrlangan_matn = SezarShifrlash(ochiq_matn, 7)
        natija = chastotali_tahlil_va_tiklash(tajriba_chastotasi, shifrlangan_matn)
        (PAPKA / "ShifrlanganMatn.txt").write_text(shifrlangan_matn, encoding="utf-8")
        (PAPKA / "TiklanganOchiqMatn.txt").write_text(natija, encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as xato:
        print(f"Xatolik: {xato}")
        return 1
    print("Tahlil yakunlandi. Natijalar:")
    print(PAPKA / "ShifrlanganMatn.txt")
    print(PAPKA / "TiklanganOchiqMatn.txt")
    print("Eslatma: chastotali tiklash taxminiy natija beradi.")
    return 0
# Tizimfa tavsiya: agar sizga kerak bo'lsa, tajriba matnini o'zgartiring yoki boshqa shifrlash usullarini sinab ko'ring.


if __name__ == "__main__":
    raise SystemExit(main())

