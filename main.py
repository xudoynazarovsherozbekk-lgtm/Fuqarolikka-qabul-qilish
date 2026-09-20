"""
Oʻzbekiston Respublikasining Fuqaroligi Toʻgʻrisidagi Qonuniga asoslangan
fuqarolikka qabul qilish tartibini aniqlovchi interaktiv dastur.
"""


class CitizenshipChecker:
    def __init__(self):
        self.user_data = {}

    def get_yes_no(self, question: str) -> bool:
        """Foydalanuvchidan 'ha' yoki 'yo'q' javobini olish uchun yordamchi funksiya."""
        while True:
            response = input(f"{question} (ha/yo'q): ").strip().lower()
            if response in ['ha', 'h', 'yes', 'y']:
                return True
            elif response in ['yo\'q', 'yoq', 'n', 'no']:
                return False
            print("Iltimos, faqat 'ha' yoki 'yo\'q' deb javob bering.")

    def run(self):
        print("=" * 60)
        print("  OʻZBEKISTON RESPUBLIKASI FUQAROLIGIGA QABUL QILISH")
        print("           TIZIMIGA HUSH KELIBSIZ (18-22 MODDALAR)")
        print("=" * 60)
        print("\nSizga beriladigan savollarga javob berib, fuqarolikka qabul")
        print("qilishning qaysi tartibiga mos kelishingizni aniqlang.\n")

        # Alohida tartib (21-modda)
        print("--- [1] ALOHIDA TARTIB (21-modda) ---")
        if self.get_yes_no("Oʻzbekiston Respublikasi Prezidenti tomonidan milliy manfaatlardan kelib chiqib fuqarolik berilishi ko'zda tutilgan shaxslar toifasiga kirasizmi?"):
            print("\nNatija: Siz 21-modda boʻyicha ALOHIDA TARTIBDA fuqarolikka qabul qilinishingiz mumkin.")
            print("Eshtama: Sizga 19 va 20-moddalarning umumiy va soddalashtirilgan talablari qoʻllanilmaydi.")
            return

        # Soddalashtirilgan tartib (20-modda)
        print("\n--- [2] SODDALASHTIRILGAN TARTIB (20-modda) ---")
        is_vatandosh = self.get_yes_no("Siz Oʻzbekiston vatandoshi (chet elda yashaydigan vatandosh) hisoblanasizmi?")
        
        if is_vatandosh:
            has_relative = self.get_yes_no("Oʻzbekistonda yashaydigan va OʻzR fuqarosi boʻlgan toʻgʻri tutashgan qarindoshingiz (ota-ona, bobo-buvi va h.k.) bormi?")
            has_achievements = False
            
            if not has_relative:
                has_achievements = self.get_yes_no("Ilm-fan, texnika, madaniyat, sport sohasida katta yutuqlarga yoki OʻzR uchun manfaatli kasb/malakaga egamisiz?")

            if has_relative or has_achievements:
                has_income = self.get_yes_no("Tirikchilikning qonuniy manbaiga egamisiz?")
                accept_const = self.get_yes_no("OʻzR Konstitutsiyasiga rioya etish majburiyatini oʻz zimmangizga olasizmi?")
                knows_lang = self.get_yes_no("Davlat tilini muloqot qilish uchun zarur darajada bilasizmi?")

                if has_income and accept_const and knows_lang:
                    print("\nNatija: Siz 20-modda boʻyicha SODDALASHTIRILGAN TARTIBDA fuqarolikka murojaat qilishingiz mumkin.")
                    print("Eslatma: Qabul qilingan qaror asosida sizga 1 yil muddatga amal qiluvchi 'Kafolat xati' beriladi.")
                    return
                else:
                    print("\nSoddalashtirilgan tartib uchun barcha shartlar (daromad, Konstitutsiya, til bilish) bajarilmadi.")

        # Umumiy tartib (19-modda)
        print("\n--- [3] UMUMIY TARTIB (19-modda) ---")
        left_other_citizenship = self.get_yes_no("Chet davlat fuqaroligidan chiqishni rasmiylashtirganmisiz (yoki fuqaroligi bo'lmagan shaxs bo'lsangiz)?")
        
        if not left_other_citizenship:
            print("\nNatija: Umumiy tartibda fuqarolikka kirish uchun chet davlat fuqaroligidan chiqish rasmiylashtirilgan boʻlishi kerak.")
            return

        is_born_here = self.get_yes_no("Oʻzbekiston Respublikasida tugʻilgan va yashab kelayotgan shaxs boʻlsangiz yoki OʻzR fuqarosi bilan nikohdan o'tib uzluksiz 3 yil birga yashaganmisiz?")
        
        if not is_born_here:
            resided_5_years = self.get_yes_no("Yashash guvohnomasi olingan kundan e'tiboran Oʻzbekistonda uzluksiz 5 yil doimiy yashab kelayotganmisiz?")
            if not resided_5_years:
                print("\nNatija: Siz Oʻzbekiston hududida uzluksiz doimiy yashash muddatiga oid talabga javob bermaysiz.")
                return
        else:
            print("-> Siz uchun 5 yillik uzluksiz yashash talabi tatbiq etilmaydi (yengillik berilgan).")

        has_income_gen = self.get_yes_no("Tirikchilikning qonuniy manbaiga egamisiz?")
        accept_const_gen = self.get_yes_no("OʻzR Konstitutsiyasiga rioya etish majburiyatini oʻz zimmangizga olasizmi?")
        knows_lang_gen = self.get_yes_no("Davlat tilini muloqot qilish uchun zarur darajada bilasizmi?")

        if has_income_gen and accept_const_gen and knows_lang_gen:
            print("\nNatija: Siz 19-modda boʻyicha UMUMIY TARTIBDA fuqarolikka qabul qilinish huquqiga egasiz.")
        else:
            print("\nNatija: Siz umumiy tartibdagi fuqarolikka qabul qilish shartlariga toʻliq mos kelmadingiz.")


if __name__ == "__main__":
    app = CitizenshipChecker()
    app.run()
