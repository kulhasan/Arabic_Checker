
import aaa1_tanimlar as ta
import aaa2_fiil_deposu_1 as fd1


# fiil_deposu_2 sayfasındaki dict.listte bulunan sülasi fiiller
# aşağıda sülasi mücerred 6 baba göre listelenmiştir.
sulasi_fiil_bab_1_fiil_havuzu = []
sulasi_fiil_bab_2_fiil_havuzu = []
sulasi_fiil_bab_3_fiil_havuzu = []
sulasi_fiil_bab_4_fiil_havuzu = []
sulasi_fiil_bab_5_fiil_havuzu = []
sulasi_fiil_bab_6_fiil_havuzu = []
sulasi_mucerred_fiil_havuzu = []
rubai_mucerred_fiil_havuzu = []

for key, value in fd1.fiil_havuzu_dict.items():
    if value == 1:
        sulasi_fiil_bab_1_fiil_havuzu.append(key)

    if value == 2:
        sulasi_fiil_bab_2_fiil_havuzu.append(key)

    if value == 3:
        sulasi_fiil_bab_3_fiil_havuzu.append(key)

    if value == 4:
        sulasi_fiil_bab_4_fiil_havuzu.append(key)

    if value == 5:
        sulasi_fiil_bab_5_fiil_havuzu.append(key)

    if value == 6:
        sulasi_fiil_bab_6_fiil_havuzu.append(key)

    if value != 44:
        sulasi_mucerred_fiil_havuzu.append(key)

    if value == 44:
        rubai_mucerred_fiil_havuzu.append(key)

# AKSAM-I SEB'A
# Yukarıda 6 baba göre listelenen sülasi mücerred fiiller
# aşağıda kendi içinde aksam-ı seb'aya göre yeniden listelenmiştir.
# A) Sahih fiiller
# A1) Salim Fiil
# Salim fiiller bablara göre listelenmiştir.
salim_fiil_bab_1_fiil_havuzu = []
salim_fiil_bab_2_fiil_havuzu = []
salim_fiil_bab_3_fiil_havuzu = []
salim_fiil_bab_4_fiil_havuzu = []
salim_fiil_bab_5_fiil_havuzu = []
salim_fiil_bab_6_fiil_havuzu = []

# Salim fiiller listelenmiştir.
salim_fiil_havuzu = []

# A2) Sahih Muzaaf Fiil
# Sahih muzaaf fiiller bablara göre listelenmiştir.
sahih_muzaaf_fiil_bab_1_fiil_havuzu = []
sahih_muzaaf_fiil_bab_2_fiil_havuzu = []
sahih_muzaaf_fiil_bab_4_fiil_havuzu = []


# Sahih muzaaf fiiller listelenmiştir.
sahih_muzaaf_fiil_havuzu = []

# A3) Sahih Mehmuz Fiil
# Sahih mehmuzu'l_fa fiiller bablara göre listelenmiştir.
sahih_mehmuz_ul_fa_fiil_bab_1_fiil_havuzu = []
sahih_mehmuz_ul_fa_fiil_bab_2_fiil_havuzu = []
sahih_mehmuz_ul_fa_fiil_bab_4_fiil_havuzu = []
sahih_mehmuz_ul_fa_fiil_bab_5_fiil_havuzu = []

# Sahih mehmuzu'l_fa fiiller listelenmiştir.
sahih_mehmuz_ul_fa_fiil_havuzu = []

# Sahih mehmuzu'l_ayn fiiller bablara göre listelenmiştir.
sahih_mehmuz_ul_ayn_fiil_bab_2_fiil_havuzu = []
sahih_mehmuz_ul_ayn_fiil_bab_3_fiil_havuzu = []
sahih_mehmuz_ul_ayn_fiil_bab_4_fiil_havuzu = []
sahih_mehmuz_ul_ayn_fiil_bab_5_fiil_havuzu = []

# Sahih mehmuzu'l_ayn fiiller listelenmiştir.
sahih_mehmuz_ul_ayn_fiil_havuzu = []

# Sahih mehmuzu'l_lam fiiller bablara göre listelenmiştir.
sahih_mehmuz_ul_lam_fiil_bab_2_fiil_havuzu = []
sahih_mehmuz_ul_lam_fiil_bab_3_fiil_havuzu = []
sahih_mehmuz_ul_lam_fiil_bab_4_fiil_havuzu = []
sahih_mehmuz_ul_lam_fiil_bab_5_fiil_havuzu = []

# Sahih mehmuzu'l_lam fiiller listelenmiştir.
sahih_mehmuz_ul_lam_fiil_havuzu = []

# Sahih mehmuz fiiller listelenmiştir.
sahih_mehmuz_fiil_havuzu = []

# Sahih fiiller listelenmiştir.
sahih_fiil_havuzu = []


# B) İlletli Fiiller
# B1) Misal Fiil
# Misal Vavi fiiller bablara göre listelenmiştir.
misal_vavi_fiil_bab_2_fiil_havuzu = []
misal_vavi_fiil_bab_3_fiil_havuzu = []
misal_vavi_fiil_bab_4_fiil_havuzu = []
misal_vavi_fiil_bab_5_fiil_havuzu = []
misal_vavi_fiil_bab_6_fiil_havuzu = []

# Misal Vavi fiiller listelenmiştir.
misal_vavi_fiil_havuzu = []

# Misal Yai fiiller bablara göre listelenmiştir.
misal_yai_fiil_bab_2_fiil_havuzu = []
misal_yai_fiil_bab_3_fiil_havuzu = []
misal_yai_fiil_bab_4_fiil_havuzu = []
misal_yai_fiil_bab_5_fiil_havuzu = []
misal_yai_fiil_bab_6_fiil_havuzu = []

# Misal Yai fiiller listelenmiştir.
misal_yai_fiil_havuzu = []

# Misal fiiller listelenmiştir.
misal_fiil_havuzu = []

# B2) Ecvef Fiil
# Ecvef Vavi fiiller bablara göre listelenmiştir.
ecvef_vavi_fiil_bab_1_fiil_havuzu = []
ecvef_vavi_fiil_bab_4_fiil_havuzu = []

# Ecvef Vavi fiiller listelenmiştir.
ecvef_vavi_fiil_havuzu = []

# Ecvef Yai fiiller bablara göre listelenmiştir.
ecvef_yai_fiil_bab_2_fiil_havuzu = []
ecvef_yai_fiil_bab_4_fiil_havuzu = []

# Ecvef Yai fiiller listelenmiştir.
ecvef_yai_fiil_havuzu = []

# Ecvef fiiller listelenmiştir.
ecvef_fiil_havuzu = []


# B3) Nakıs Fiil
# Nakıs fiiller bablara göre listelenmiştir.
nakis_fiil_bab_1_fiil_havuzu = []
nakis_fiil_bab_2_fiil_havuzu = []
nakis_fiil_bab_3_fiil_havuzu = []
nakis_fiil_bab_4_fiil_havuzu = []
nakis_fiil_bab_5_fiil_havuzu = []

# Nakıs fiiller listelenmiştir.
nakis_fiil_havuzu = []


# B4) Lefif Fiil
# B4a) Lefif-i Mefruk Fiil
# Lefif-i Mefruk fiiller bablara göre listelenmiştir.
lefif_i_mefruk_fiil_bab_2_fiil_havuzu = []
lefif_i_mefruk_fiil_bab_4_fiil_havuzu = []
lefif_i_mefruk_fiil_bab_6_fiil_havuzu = []

# Lefif-i Mefruk fiiller listelenmiştir.
lefif_i_mefruk_fiil_havuzu = []

# B4b) Lefif-i Makrun Fiil
# Lefif-i Makrun fiiller bablara göre listelenmiştir.
lefif_i_makrun_fiil_bab_2_fiil_havuzu = []
lefif_i_makrun_fiil_bab_4_fiil_havuzu = []

# Lefif-i Makrun fiiller listelenmiştir.
lefif_i_makrun_fiil_havuzu = []

# Lefif fiiller listelenmiştir.
lefif_fiil_havuzu = []

# Mu'tel fiiller listelenmiştir.
mutel_fiil_havuzu = []


# AKSAM-I SEB'A FORMULLERİ
# Salim fiil 1. bab formülü
for fiil in sulasi_fiil_bab_1_fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_bab_1_fiil_havuzu.append(fiil)

# Salim fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_bab_2_fiil_havuzu.append(fiil)

# Salim fiil 3. bab formülü
for fiil in sulasi_fiil_bab_3_fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_bab_3_fiil_havuzu.append(fiil)

# Salim fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_bab_4_fiil_havuzu.append(fiil)

# Salim fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_bab_5_fiil_havuzu.append(fiil)

# Salim fiil 6. bab formülü
for fiil in sulasi_fiil_bab_6_fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_bab_6_fiil_havuzu.append(fiil)

# Salim fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_havuzu.append(fiil)
        if len(fiil) != 3:
            salim_fiil_havuzu.remove(fiil)



# Sahih Muzaaf fiil 1. bab formülü
for fiil in sulasi_fiil_bab_1_fiil_havuzu:
    if (fiil[0] not in ta.ILLET_HARFI) and \
     (fiil[1] not in ta.ILLET_HARFI) and \
     (fiil[2] == ta.SEDDE):
        sahih_muzaaf_fiil_bab_1_fiil_havuzu.append(fiil)

# Sahih Muzaaf fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if (fiil[0] not in ta.ILLET_HARFI) and \
     (fiil[1] not in ta.ILLET_HARFI) and \
     (fiil[2] == ta.SEDDE):
        sahih_muzaaf_fiil_bab_2_fiil_havuzu.append(fiil)

# Sahih Muzaaf fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if (fiil[0] not in ta.ILLET_HARFI) and \
     (fiil[1] not in ta.ILLET_HARFI) and \
     (fiil[2] == ta.SEDDE):
        sahih_muzaaf_fiil_bab_4_fiil_havuzu.append(fiil)

# Sahih Muzaaf fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if (fiil[0] not in ta.ILLET_HARFI) and \
            (fiil[1] not in ta.ILLET_HARFI) and \
            (fiil[2] == ta.SEDDE):
        sahih_muzaaf_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Fa fiil 1. bab formülü
for fiil in sulasi_fiil_bab_1_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[0] in ta.HEMZE:
        sahih_mehmuz_ul_fa_fiil_bab_1_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Fa fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[0] in ta.HEMZE:
        sahih_mehmuz_ul_fa_fiil_bab_2_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Fa fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[0] in ta.HEMZE:
        sahih_mehmuz_ul_fa_fiil_bab_4_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Fa fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[0] in ta.HEMZE:
        sahih_mehmuz_ul_fa_fiil_bab_5_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Fa fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[0] in ta.HEMZE:
        sahih_mehmuz_ul_fa_fiil_havuzu.append(fiil)


# Sahih Mehmuzu'l-Ayn fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[1] in ta.HEMZE:
        sahih_mehmuz_ul_ayn_fiil_bab_2_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Ayn fiil 3. bab formülü
for fiil in sulasi_fiil_bab_3_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[1] in ta.HEMZE:
        sahih_mehmuz_ul_ayn_fiil_bab_3_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Ayn fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[1] in ta.HEMZE:
        sahih_mehmuz_ul_ayn_fiil_bab_4_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Ayn fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[1] in ta.HEMZE:
        sahih_mehmuz_ul_ayn_fiil_bab_5_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Ayn fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[2] not in ta.HEMZE and \
     fiil[1] in ta.HEMZE:
        sahih_mehmuz_ul_ayn_fiil_havuzu.append(fiil)



# Sahih Mehmuzu'l-Lam fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] in ta.HEMZE:
        sahih_mehmuz_ul_lam_fiil_bab_2_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Lam fiil 3. bab formülü
for fiil in sulasi_fiil_bab_3_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] in ta.HEMZE:
        sahih_mehmuz_ul_lam_fiil_bab_3_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Lam fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] in ta.HEMZE:
        sahih_mehmuz_ul_lam_fiil_bab_4_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Lam fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] in ta.HEMZE:
        sahih_mehmuz_ul_lam_fiil_bab_5_fiil_havuzu.append(fiil)

# Sahih Mehmuzu'l-Lam fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
     fiil[0] not in ta.HEMZE and \
     fiil[1] not in ta.HEMZE and \
     fiil[2] in ta.HEMZE:
        sahih_mehmuz_ul_lam_fiil_havuzu.append(fiil)

# Sahih Mehmuz fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] not in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI and \
            (fiil[0] in ta.HEMZE or fiil[1] in ta.HEMZE or fiil[2] in ta.HEMZE):
        sahih_mehmuz_fiil_havuzu.append(fiil)

# Misal Vavi fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] == ta.VAV and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_vavi_fiil_bab_2_fiil_havuzu.append(fiil)

# Misal Vavi fiil 3. bab formülü
for fiil in sulasi_fiil_bab_3_fiil_havuzu:
    if fiil[0] == ta.VAV and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_vavi_fiil_bab_3_fiil_havuzu.append(fiil)

# Misal Vavi fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] == ta.VAV and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_vavi_fiil_bab_4_fiil_havuzu.append(fiil)

# Misal Vavi fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if fiil[0] == ta.VAV and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_vavi_fiil_bab_5_fiil_havuzu.append(fiil)

# Misal Vavi fiil 6. bab formülü
for fiil in sulasi_fiil_bab_6_fiil_havuzu:
    if fiil[0] == ta.VAV and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_vavi_fiil_bab_6_fiil_havuzu.append(fiil)

# Misal Vavi fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] == ta.VAV and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_vavi_fiil_havuzu.append(fiil)

# Misal Yai fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] == ta.YE_NOKTALI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_yai_fiil_bab_2_fiil_havuzu.append(fiil)

# Misal Yai fiil 3. bab formülü
for fiil in sulasi_fiil_bab_3_fiil_havuzu:
    if fiil[0] == ta.YE_NOKTALI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_yai_fiil_bab_3_fiil_havuzu.append(fiil)

# Misal Yai fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] == ta.YE_NOKTALI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_yai_fiil_bab_4_fiil_havuzu.append(fiil)

# Misal Yai fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if fiil[0] == ta.YE_NOKTALI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_yai_fiil_bab_5_fiil_havuzu.append(fiil)

# Misal Yai fiil 6. bab formülü
for fiil in sulasi_fiil_bab_6_fiil_havuzu:
    if fiil[0] == ta.YE_NOKTALI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_yai_fiil_bab_6_fiil_havuzu.append(fiil)

# Misal Yai fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] == ta.YE_NOKTALI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_yai_fiil_havuzu.append(fiil)

# Misal fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if (fiil[0] == ta.YE_NOKTALI or fiil[0] == ta.VAV) and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_fiil_havuzu.append(fiil)


# Ecvef Vavi fiil 1. bab formülü
for fiil in sulasi_fiil_bab_1_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI:
        ecvef_vavi_fiil_bab_1_fiil_havuzu.append(fiil)

# Ecvef Vavi fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI and \
            fiil[5] == ta.VAV:
        ecvef_vavi_fiil_bab_4_fiil_havuzu.append(fiil)

# Ecvef Vavi fiil formülü
for fiil in ecvef_vavi_fiil_bab_1_fiil_havuzu:
    if fiil:
        ecvef_vavi_fiil_havuzu.append(fiil)
        for fiil in ecvef_vavi_fiil_bab_4_fiil_havuzu:
            ecvef_vavi_fiil_havuzu.append(fiil)

# Ecvef Yai fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
     fiil[1] in ta.ILLET_HARFI and \
     fiil[2] not in ta.ILLET_HARFI:
        ecvef_yai_fiil_bab_2_fiil_havuzu.append(fiil)

# Ecvef Yai fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI and \
            fiil[5] == ta.YE:
        ecvef_yai_fiil_bab_4_fiil_havuzu.append(fiil)

# Ecvef Yai fiil formülü
for fiil in ecvef_yai_fiil_bab_2_fiil_havuzu:
    if fiil:
        ecvef_yai_fiil_havuzu.append(fiil)
        for fiil in ecvef_yai_fiil_bab_4_fiil_havuzu:
            ecvef_yai_fiil_havuzu.append(fiil)

# Ecvef fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        ecvef_fiil_havuzu.append(fiil)


# Nakıs fiil 1. bab formülü
for fiil in sulasi_fiil_bab_1_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_bab_1_fiil_havuzu.append(fiil)

# Nakıs fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_bab_2_fiil_havuzu.append(fiil)

# Nakıs fiil 3. bab formülü
for fiil in sulasi_fiil_bab_3_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_bab_3_fiil_havuzu.append(fiil)

# Nakıs fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_bab_4_fiil_havuzu.append(fiil)

# Nakıs fiil 5. bab formülü
for fiil in sulasi_fiil_bab_5_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_bab_5_fiil_havuzu.append(fiil)

# Nakıs fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_havuzu.append(fiil)

# Lefif-i Mefruk fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_mefruk_fiil_bab_2_fiil_havuzu.append(fiil)

# Lefif-i Mefruk fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_mefruk_fiil_bab_4_fiil_havuzu.append(fiil)

# Lefif-i Mefruk fiil 6. bab formülü
for fiil in sulasi_fiil_bab_6_fiil_havuzu:
    if fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_mefruk_fiil_bab_6_fiil_havuzu.append(fiil)

# Lefif-i Mefruk fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_mefruk_fiil_havuzu.append(fiil)


# Lefif-i Makrun fiil 2. bab formülü
for fiil in sulasi_fiil_bab_2_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_makrun_fiil_bab_2_fiil_havuzu.append(fiil)

# Lefif-i Makrun fiil 4. bab formülü
for fiil in sulasi_fiil_bab_4_fiil_havuzu:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_makrun_fiil_bab_4_fiil_havuzu.append(fiil)

# Lefif-i Makrun fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_makrun_fiil_havuzu.append(fiil)

# Lefif fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if (fiil[0] in ta.ILLET_HARFI and
        fiil[1] not in ta.ILLET_HARFI and
        fiil[2] in ta.ILLET_HARFI) or \
            (fiil[0] not in ta.ILLET_HARFI and
             fiil[1] in ta.ILLET_HARFI and
             fiil[2] in ta.ILLET_HARFI):
        lefif_fiil_havuzu.append(fiil)

# Mu'tel fiil formülü
for fiil in fd1.fiil_havuzu_list:
    if fiil[0] in ta.ILLET_HARFI or \
            fiil[1] in ta.ILLET_HARFI or \
            fiil[2] in ta.ILLET_HARFI:
        mutel_fiil_havuzu.append(fiil)


# KARIŞIK FİİLLER
# Aşağıda aksam-ı seb'anın iki farklı özelliğine sahip fiiller sıralanacaktır.
# Bu fiillerin neler olduğunu ne kadar olduğunu henüz tam bilmiyorum.
# Bu yüzden bu kısım zamanla artabilir.
# Şimdilik sadece bildiklerimi yazıyorum.


if __name__ == '__main__':
    print('Fiil havuzu (bab açıklamalı):\n ', fd1.fiil_havuzu_dict)
    print('Fiil havuzu:\n ', fd1.fiil_havuzu_list)

    print('Sülasi fiil birinci bab fiil havuzu:\n ', sulasi_fiil_bab_1_fiil_havuzu)
    print('Sülasi fiil ikinci bab fiil havuzu:\n ', sulasi_fiil_bab_2_fiil_havuzu)
    print('Sülasi fiil üçüncü bab fiil havuzu:\n ', sulasi_fiil_bab_3_fiil_havuzu)
    print('Sülasi fiil dördüncü bab fiil havuzu:\n ', sulasi_fiil_bab_4_fiil_havuzu)
    print('Sülasi fiil beşinci bab fiil havuzu:\n ', sulasi_fiil_bab_5_fiil_havuzu)
    print('Sülasi fiil altıncı bab fiil havuzu:\n ', sulasi_fiil_bab_6_fiil_havuzu)

    print("Sülasi Mücerred fiil havuzu:\n ", sulasi_mucerred_fiil_havuzu)
    print("Rubai Mücerred fiil havuzu:\n ", rubai_mucerred_fiil_havuzu)

    print('Salim fiil birinci bab fiil havuzu:\n ', salim_fiil_bab_1_fiil_havuzu)
    print('Salim fiil ikinci bab fiil havuzu:\n ', salim_fiil_bab_2_fiil_havuzu)
    print('Salim fiil üçüncü bab fiil havuzu:\n ', salim_fiil_bab_3_fiil_havuzu)
    print('Salim fiil dördüncü bab fiil havuzu:\n ', salim_fiil_bab_4_fiil_havuzu)
    print('Salim fiil beşinci bab fiil havuzu:\n ', salim_fiil_bab_5_fiil_havuzu)
    print('Salim fiil altıncı bab fiil havuzu:\n ', salim_fiil_bab_6_fiil_havuzu)
    print('Salim fiil havuzu:\n ', salim_fiil_havuzu)

    print('Sahih Muzaaf fiil birinci bab fiil havuzu:\n ', sahih_muzaaf_fiil_bab_1_fiil_havuzu)
    print('Sahih Muzaaf fiil ikinci bab fiil havuzu:\n ', sahih_muzaaf_fiil_bab_2_fiil_havuzu)
    print('Sahih Muzaaf fiil dördüncü bab fiil havuzu:\n ', sahih_muzaaf_fiil_bab_4_fiil_havuzu)
    print('Sahih Muzaaf fiil havuzu:\n ', sahih_muzaaf_fiil_havuzu)

    print('Sahih Mehmuzu-l-Fa fiil birinci bab fiil havuzu:\n ', sahih_mehmuz_ul_fa_fiil_bab_1_fiil_havuzu)
    print('Sahih Mehmuzu-l-Fa fiil ikinci bab fiil havuzu:\n ', sahih_mehmuz_ul_fa_fiil_bab_2_fiil_havuzu)
    print('Sahih Mehmuzu-l-Fa fiil dördüncü bab fiil havuzu:\n ', sahih_mehmuz_ul_fa_fiil_bab_4_fiil_havuzu)
    print('Sahih Mehmuzu-l-Fa fiil beşinci bab fiil havuzu:\n ', sahih_mehmuz_ul_fa_fiil_bab_5_fiil_havuzu)
    print("Sahih Mehmuzu'l-Fa fiil havuzu:\n ", sahih_mehmuz_ul_fa_fiil_havuzu)

    print('Sahih Mehmuzu-l-Ayn fiil ikinci bab fiil havuzu:\n ', sahih_mehmuz_ul_ayn_fiil_bab_2_fiil_havuzu)
    print('Sahih Mehmuzu-l-Ayn fiil üçüncü bab fiil havuzu:\n ', sahih_mehmuz_ul_ayn_fiil_bab_3_fiil_havuzu)
    print('Sahih Mehmuzu-l-Ayn fiil dördüncü bab fiil havuzu:\n ', sahih_mehmuz_ul_ayn_fiil_bab_4_fiil_havuzu)
    print('Sahih Mehmuzu-l-Ayn fiil beşinci bab fiil havuzu:\n ', sahih_mehmuz_ul_ayn_fiil_bab_5_fiil_havuzu)
    print("Sahih Mehmuzu'l-Ayn fiil havuzu:\n ", sahih_mehmuz_ul_ayn_fiil_havuzu)

    print('Sahih Mehmuzu-l-Lam fiil ikinci bab fiil havuzu:\n ', sahih_mehmuz_ul_lam_fiil_bab_2_fiil_havuzu)
    print('Sahih Mehmuzu-l-Lam fiil üçüncü bab fiil havuzu:\n ', sahih_mehmuz_ul_lam_fiil_bab_3_fiil_havuzu)
    print('Sahih Mehmuzu-l-Lam fiil dördüncü bab fiil havuzu:\n ', sahih_mehmuz_ul_lam_fiil_bab_4_fiil_havuzu)
    print('Sahih Mehmuzu-l-Lam fiil beşinci bab fiil havuzu:\n ', sahih_mehmuz_ul_lam_fiil_bab_5_fiil_havuzu)
    print("Sahih Mehmuzu'l-Lam fiil havuzu:\n ", sahih_mehmuz_ul_lam_fiil_havuzu)
    print("Sahih Mehmuz fiil havuzu:\n ", sahih_mehmuz_fiil_havuzu)


    print('Misal Vavi fiil ikinci bab fiil havuzu:\n ', misal_vavi_fiil_bab_2_fiil_havuzu)
    print('Misal Vavi fiil üçüncü bab fiil havuzu:\n ', misal_vavi_fiil_bab_3_fiil_havuzu)
    print('Misal Vavi fiil dördüncü bab fiil havuzu:\n ', misal_vavi_fiil_bab_4_fiil_havuzu)
    print('Misal Vavi fiil beşinci bab fiil havuzu:\n ', misal_vavi_fiil_bab_5_fiil_havuzu)
    print('Misal Vavi fiil altıncı bab fiil havuzu:\n ', misal_vavi_fiil_bab_6_fiil_havuzu)
    print("Misal Vavi fiil havuzu:\n ", misal_vavi_fiil_havuzu)

    print('Misal Yai fiil ikinci bab fiil havuzu:\n ', misal_yai_fiil_bab_2_fiil_havuzu)
    print('Misal Yai fiil üçüncü bab fiil havuzu:\n ', misal_yai_fiil_bab_3_fiil_havuzu)
    print('Misal Yai fiil dördüncü bab fiil havuzu:\n ', misal_yai_fiil_bab_4_fiil_havuzu)
    print('Misal Yai fiil beşinci bab fiil havuzu:\n ', misal_yai_fiil_bab_5_fiil_havuzu)
    print('Misal Yai fiil altıncı bab fiil havuzu:\n ', misal_yai_fiil_bab_6_fiil_havuzu)
    print("Misal Yai fiil havuzu:\n ", misal_yai_fiil_havuzu)
    print("Misal fiil havuzu:\n ", misal_fiil_havuzu)

    print('Ecvef Vavi fiil birinci bab fiil havuzu:\n ', ecvef_vavi_fiil_bab_1_fiil_havuzu)
    print('Ecvef Vavi fiil dördüncü bab fiil havuzu:\n ', ecvef_vavi_fiil_bab_4_fiil_havuzu)
    print("Ecvef Vavi fiil havuzu:\n ", ecvef_vavi_fiil_havuzu)

    print('Ecvef Yai fiil ikinci bab fiil havuzu:\n ', ecvef_yai_fiil_bab_2_fiil_havuzu)
    print('Ecvef Yai fiil dördüncü bab fiil havuzu:\n ', ecvef_yai_fiil_bab_4_fiil_havuzu)
    print("Ecvef Yai fiil havuzu:\n ", ecvef_yai_fiil_havuzu)
    print("Ecvef fiil havuzu:\n ", ecvef_fiil_havuzu)

    print('Nakıs fiil birinci bab fiil havuzu:\n ', nakis_fiil_bab_1_fiil_havuzu)
    print('Nakıs fiil ikinci bab fiil havuzu:\n ', nakis_fiil_bab_2_fiil_havuzu)
    print('Nakıs fiil üçüncü bab fiil havuzu:\n ', nakis_fiil_bab_3_fiil_havuzu)
    print('Nakıs fiil dördüncü bab fiil havuzu:\n ', nakis_fiil_bab_4_fiil_havuzu)
    print('Nakıs fiil beşinci bab fiil havuzu:\n ', nakis_fiil_bab_5_fiil_havuzu)
    print("Nakıs fiil havuzu:\n ", nakis_fiil_havuzu)

    print('Lefif-i Mefruk fiil ikinci bab fiil havuzu:\n ', lefif_i_mefruk_fiil_bab_2_fiil_havuzu)
    print('Lefif-i Mefruk fiil dördüncü bab fiil havuzu:\n ', lefif_i_mefruk_fiil_bab_4_fiil_havuzu)
    print('Lefif-i Mefruk fiil altıncı bab fiil havuzu:\n ', lefif_i_mefruk_fiil_bab_6_fiil_havuzu)
    print("Lefif-i Mefruk fiil havuzu:\n ", lefif_i_mefruk_fiil_havuzu)

    print('Lefif-i Makrun fiil ikinci bab fiil havuzu:\n ', lefif_i_makrun_fiil_bab_2_fiil_havuzu)
    print('Lefif-i Makrun fiil dördüncü bab fiil havuzu:\n ', lefif_i_makrun_fiil_bab_4_fiil_havuzu)
    print("Lefif-i Makrun fiil havuzu:\n ", lefif_i_makrun_fiil_havuzu)
    print("Lefif fiil havuzu:\n ", lefif_fiil_havuzu)
    print("Mu'tel fiil havuzu:\n ", mutel_fiil_havuzu)





# todo karışık fiiller için ayrı listeler olmalı
#  mesela: misal_vavi_muzaaf_fiil_bab_2_fiil_havuzu


'''
Bu fiiller zaten diğer listelerde var.
 o listelerden exeption larla çıkarmadan 
 ayrı bir liste oluşturulursa mükerrer liste olur.
 diğer listelerden alıarak yapılacak fiil çekimleri de yanlış olur.
 yani
 1) diğer listelerden çıkarılmalı
 2) ayrı liste oluşturulmalı
 3) daha sonra bu liste diğer liste ile birleştirilmeli.
 çünkü diğer liste eksik kalacak.
 vedde fiilinin çekimi misal fiil gibi değil.
 ama misal fiil listesinde de olması gerekiyor.

mehmuz_ul_fa_ve_ecvef_vavi_fiil_bab_1_fiil_havuzu = [آب] ee be
mehmuz_ul_fa_ve_nakis_fiil_bab_2_fiil_havuzu = [أتى] eta
mehmuz_ul_ayn_ve_nakis_fiil_bab_3_fiil_havuzu = [رأى] ra ee
mehmuz_ul_lam_ve_ecvef_yai_fiil_bab_2_fiil_havuzu = [جاء] cae
mehmuz_ul_fa_ve_lefif_i_makrun_fiil_bab_2_fiil_havuzu = [أوى] eva
mehmuz_ul_ayn_ve_lefif_i_mefruk_fiil_bab_2_fiil_havuzu = [وأى] ve ee


muzaaf_misal_vavi_fiil_bab_123456_fiil_havuzu = ['ودّ']
dorduncu bab olmasi lazim vedide yevdedu



'''








