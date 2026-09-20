import streamlit as st

st.set_page_config(page_title="Oʻzbekiston Fuqaroligiga Qabul Qilish", page_icon="🇺🇿", layout="centered")

st.title("🇺🇿 Oʻzbekiston Respublikasi Fuqaroligiga Qabul Qilish Tizimi")
st.caption("Oʻzbekiston Respublikasining 'Fuqarolik toʻgʻrisida'gi Qonunining 18-22 moddalari asosida")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Alohida tartib (21-modda)", "Soddalashtirilgan tartib (20-modda)", "Umumiy tartib (19-modda)"])

with tab1:
    st.header("Alohida tartib (21-modda)")
    p21 = st.checkbox("Oʻzbekiston Respublikasi Prezidenti tomonidan milliy manfaatlardan kelib chiqib fuqarolik berilishi ko'zda tutilgan shaxslar toifasiga kirasizmi?")
    
    if p21:
        st.success("Siz 21-modda boʻyicha ALOHIDA TARTIBDA fuqarolikka qabul qilinishingiz mumkin.")
        st.info("Eslatma: Sizga 19 va 20-moddalarning umumiy va soddalashtirilgan talablari qoʻllanilmaydi.")

with tab2:
    st.header("Soddalashtirilgan tartib (20-modda)")
    is_vatandosh = st.radio("Siz Oʻzbekiston vatandoshi (chet elda yashaydigan vatandosh) hisoblanasizmi?", ["Tanlang...", "Ha", "Yo'q"])
    
    if is_vatandosh == "Ha":
        has_relative = st.radio("Oʻzbekistonda yashaydigan va OʻzR fuqarosi boʻlgan toʻgʻri tutashgan qarindoshingiz bormi?", ["Tanlang...", "Ha", "Yo'q"])
        has_achievements = "Yo'q"
        
        if has_relative == "Yo'q":
            has_achievements = st.radio("Ilm-fan, texnika, madaniyat, sport sohasida katta yutuqlarga yoki OʻzR uchun manfaatli kasbga egamisiz?", ["Tanlang...", "Ha", "Yo'q"])
        
        if has_relative == "Ha" or has_achievements == "Ha":
            c1 = st.checkbox("Tirikchilikning qonuniy manbaiga egaman")
            c2 = st.checkbox("OʻzR Konstitutsiyasiga rioya etish majburiyatini olaman")
            c3 = st.checkbox("Davlat tilini muloqot qilish uchun zarur darajada bilaman")
            
            if c1 and c2 and c3:
                st.success("Siz 20-modda boʻyicha SODDALASHTIRILGAN TARTIBDA fuqarolikka murojaat qilishingiz mumkin.")
                st.info("Eslatma: Qaror asosida sizga 1 yil muddatga amal qiluvchi 'Kafolat xati' beriladi.")
            else:
                st.warning("Soddalashtirilgan tartib uchun barcha shartlar bajarilishi kerak.")

with tab3:
    st.header("Umumiy tartib (19-modda)")
    left_cit = st.radio("Chet davlat fuqaroligidan chiqishni rasmiylashtirganmisiz (yoki fuqaroligi bo'lmagan shaxsmisiz)?", ["Tanlang...", "Ha", "Yo'q"])
    
    if left_cit == "Ha":
        is_born = st.radio("Oʻzbekistonda tugʻilgan va yashab kelayotgan shaxsmisiz yoki OʻzR fuqarosi bilan nikohda uzluksiz 3 yil yashaganmisiz?", ["Tanlang...", "Ha", "Yo'q"])
        
        resided_5 = "Ha"
        if is_born == "Yo'q":
            resided_5 = st.radio("Yashash guvohnomasi olingan kundan e'tiboran uzluksiz 5 yil doimiy yashab kelayotganmisiz?", ["Tanlang...", "Ha", "Yo'q"])
        
        if is_born == "Ha" or resided_5 == "Ha":
            gc1 = st.checkbox("Tirikchilikning qonuniy manbaiga egaman ", key="gc1")
            gc2 = st.checkbox("OʻzR Konstitutsiyasiga rioya etish majburiyatini olaman ", key="gc2")
            gc3 = st.checkbox("Davlat tilini muloqot qilish uchun zarur darajada bilaman ", key="gc3")
            
            if gc1 and gc2 and gc3:
                st.success("Siz 19-modda boʻyicha UMUMIY TARTIBDA fuqarolikka qabul qilinish huquqiga egasiz.")
            else:
                st.warning("Umumiy tartib shartlarini to'liq belgilang.")
        elif resided_5 == "Yo'q":
            st.error("Uzluksiz 5 yil yashash talabi bajarilmadi.")
    elif left_cit == "Yo'q":
        st.error("Umumiy tartibda fuqarolikka kirish uchun chet davlat fuqaroligidan chiqish talab etiladi.")
