
'''



import tanimlar as ta

############## SAHIH FIILLER #################

alim_fiil_bab_1_havuzu_harekesiz = ['نصر']  # fethadan dammeye
salim_fiil_bab_2_havuzu_harekesiz = ['جلس']  # fethadan kesraya
salim_fiil_bab_3_havuzu_harekesiz = ['فتح']  # fethadan fethaya
salim_fiil_bab_4_havuzu_harekesiz = ['علم']  # kesradan fethaya
salim_fiil_bab_5_havuzu_harekesiz = ['حسن']  # dammeden dammeye
salim_fiil_bab_6_havuzu_harekesiz = ['حسب']  # kesradan kesraya


salim_fiil_bab_havuzu = {'نصر': 1,
                         'جلس': 2,
                         'فتح': 3,
                         'علم': 4,
                         'حسن': 5,
                         'حسب': 6,
                         'كتب': 1,
                         'نزل': 2,
                         'فعل': 3,
                         'شرب': 4,
                         'كبر': 5,
                         'نعم': 6,
                         'سجد': 1,
                         'صبر': 2,
                         'شرح': 3,
                         'فهم': 4,
                         'عظم': 5,
                         'خسر': 6}







# todo ehaze fiilinde istisna oldu[u icin bunun yerine baska bir ornek bulunmali
sahih_mehmuzul_fa_fiil_bab_1_havuzu_harekesiz = ['أخذ']
sahih_mehmuzul_fa_fiil_bab_2_havuzu_harekesiz = ['أسر']
sahih_mehmuzul_fa_fiil_bab_3_havuzu_harekesiz = ['أزق']
sahih_mehmuzul_fa_fiil_bab_4_havuzu_harekesiz = ['أذن']
sahih_mehmuzul_fa_fiil_bab_5_havuzu_harekesiz = ['أدب']
sahih_mehmuzul_fa_fiil_havuzu_harekesiz = \
    sahih_mehmuzul_fa_fiil_bab_1_havuzu_harekesiz + \
    sahih_mehmuzul_fa_fiil_bab_2_havuzu_harekesiz + \
    sahih_mehmuzul_fa_fiil_bab_3_havuzu_harekesiz + \
    sahih_mehmuzul_fa_fiil_bab_4_havuzu_harekesiz + \
    sahih_mehmuzul_fa_fiil_bab_5_havuzu_harekesiz
sahih_mehmuzul_ayn_fiil_bab_1_havuzu_harekesiz = ['']
sahih_mehmuzul_ayn_fiil_bab_2_havuzu_harekesiz = ['']
sahih_mehmuzul_ayn_fiil_bab_3_havuzu_harekesiz = ['سأل']
sahih_mehmuzul_ayn_fiil_bab_4_havuzu_harekesiz = ['']
sahih_mehmuzul_ayn_fiil_bab_5_havuzu_harekesiz = ['']
sahih_mehmuzul_ayn_fiil_havuzu_harekesiz = \
    sahih_mehmuzul_ayn_fiil_bab_1_havuzu_harekesiz + \
    sahih_mehmuzul_ayn_fiil_bab_2_havuzu_harekesiz + \
    sahih_mehmuzul_ayn_fiil_bab_3_havuzu_harekesiz + \
    sahih_mehmuzul_ayn_fiil_bab_4_havuzu_harekesiz + \
    sahih_mehmuzul_ayn_fiil_bab_5_havuzu_harekesiz
sahih_mehmuzul_lam_fiil_bab_1_havuzu_harekesiz = ['']
sahih_mehmuzul_lam_fiil_bab_2_havuzu_harekesiz = ['']
sahih_mehmuzul_lam_fiil_bab_3_havuzu_harekesiz = ['قرأ']
sahih_mehmuzul_lam_fiil_bab_4_havuzu_harekesiz = ['']
sahih_mehmuzul_lam_fiil_bab_5_havuzu_harekesiz = ['']
sahih_mehmuzul_lam_fiil_havuzu_harekesiz = \
    sahih_mehmuzul_lam_fiil_bab_1_havuzu_harekesiz + \
    sahih_mehmuzul_lam_fiil_bab_2_havuzu_harekesiz + \
    sahih_mehmuzul_lam_fiil_bab_3_havuzu_harekesiz + \
    sahih_mehmuzul_lam_fiil_bab_4_havuzu_harekesiz + \
    sahih_mehmuzul_lam_fiil_bab_5_havuzu_harekesiz
sahih_muzaaf_fiil_bab_1_havuzu_harekesiz = ['مدّ']
sahih_muzaaf_fiil_bab_2_havuzu_harekesiz = ['فرّ']
sahih_muzaaf_fiil_bab_4_havuzu_harekesiz = ['عضّ']
misal_vavi_fiil_bab_2_havuzu_harekesiz = ['وجد']
misal_vavi_fiil_bab_3_havuzu_harekesiz = ['وهب']
misal_vavi_fiil_bab_4_havuzu_harekesiz = ['وهل']
misal_vavi_fiil_bab_5_havuzu_harekesiz = ['وخم']
misal_vavi_fiil_bab_6_havuzu_harekesiz = ['ولع']
misal_vavi_fiil_havuzu_harekesiz = \
    misal_vavi_fiil_bab_2_havuzu_harekesiz + \
    misal_vavi_fiil_bab_3_havuzu_harekesiz + \
    misal_vavi_fiil_bab_4_havuzu_harekesiz + \
    misal_vavi_fiil_bab_5_havuzu_harekesiz + \
    misal_vavi_fiil_bab_6_havuzu_harekesiz
misal_yai_fiil_bab_2_havuzu_harekesiz = ['']
misal_yai_fiil_bab_3_havuzu_harekesiz = ['']
misal_yai_fiil_bab_4_havuzu_harekesiz = ['']
misal_yai_fiil_bab_5_havuzu_harekesiz = ['']
misal_yai_fiil_bab_6_havuzu_harekesiz = ['']
misal_yai_fiil_havuzu_harekesiz = \
    misal_yai_fiil_bab_2_havuzu_harekesiz + \
    misal_yai_fiil_bab_3_havuzu_harekesiz + \
    misal_yai_fiil_bab_4_havuzu_harekesiz + \
    misal_yai_fiil_bab_5_havuzu_harekesiz + \
    misal_yai_fiil_bab_6_havuzu_harekesiz
ecvef_vavi_fiil_bab_1_havuzu_harekesiz = ['قال']
ecvef_vavi_fiil_havuzu_harekesiz = \
    ecvef_vavi_fiil_bab_1_havuzu_harekesiz
ecvef_yai_fiil_bab_2_havuzu_harekesiz = ['باع']
ecvef_yai_fiil_bab_4_havuzu_harekesiz = ['خاف']
ecvef_yai_fiil_havuzu_harekesiz = \
    ecvef_yai_fiil_bab_2_havuzu_harekesiz + \
    ecvef_yai_fiil_bab_4_havuzu_harekesiz
nakis_fiil_bab_1_havuzu_harekesiz = ['عدا']
nakis_fiil_bab_2_havuzu_harekesiz = ['رمى']
nakis_fiil_bab_3_havuzu_harekesiz = ['سعى']
nakis_fiil_bab_4_havuzu_harekesiz = ['رضي']
nakis_fiil_bab_5_havuzu_harekesiz = ['ذكو']
lefif_makrun_fiil_bab_2_havuzu_harekesiz = ['روى']
lefif_makrun_fiil_bab_4_havuzu_harekesiz = ['سوي']
lefif_makrun_fiil_havuzu_harekesiz = \
    lefif_makrun_fiil_bab_2_havuzu_harekesiz + \
    lefif_makrun_fiil_bab_4_havuzu_harekesiz
lefif_mefruk_fiil_bab_2_havuzu_harekesiz = ['وقى']
lefif_mefruk_fiil_bab_4_havuzu_harekesiz = ['وجي']
lefif_mefruk_fiil_bab_6_havuzu_harekesiz = ['ولي']
lefif_mefruk_fiil_havuzu_harekesiz = \
    lefif_mefruk_fiil_bab_2_havuzu_harekesiz + \
    lefif_mefruk_fiil_bab_4_havuzu_harekesiz + \
    lefif_mefruk_fiil_bab_6_havuzu_harekesiz
lefif_fiil_havuzu_harekesiz = \
    lefif_makrun_fiil_havuzu_harekesiz + \
    lefif_makrun_fiil_havuzu_harekesiz


# Butun salim fiiller
salim_fiil_havuzu_harekesiz = \
    salim_fiil_bab_1_havuzu_harekesiz + \
    salim_fiil_bab_2_havuzu_harekesiz + \
    salim_fiil_bab_3_havuzu_harekesiz + \
    salim_fiil_bab_4_havuzu_harekesiz + \
    salim_fiil_bab_5_havuzu_harekesiz + \
    salim_fiil_bab_6_havuzu_harekesiz
# Butun sahih mehmuz fiiller
sahih_mehmuz_fiil_havuzu_harekesiz = \
    sahih_mehmuzul_fa_fiil_havuzu_harekesiz + \
    sahih_mehmuzul_ayn_fiil_havuzu_harekesiz + \
    sahih_mehmuzul_lam_fiil_havuzu_harekesiz
# Butun sahih muzaaf fiiller
sahih_muzaaf_fiil_havuzu_harekesiz = \
    sahih_muzaaf_fiil_bab_1_havuzu_harekesiz + \
    sahih_muzaaf_fiil_bab_2_havuzu_harekesiz + \
    sahih_muzaaf_fiil_bab_4_havuzu_harekesiz
# Butun misal fiiller
misal_fiil_havuzu_harekesiz = \
    misal_vavi_fiil_havuzu_harekesiz + \
    misal_yai_fiil_havuzu_harekesiz
# Butun ecvef fiiller
ecvef_fiil_havuzu_harekesiz = \
    ecvef_vavi_fiil_havuzu_harekesiz + \
    ecvef_yai_fiil_havuzu_harekesiz
# Butun nakis fiiller
nakis_fiil_havuzu_harekesiz = \
    nakis_fiil_bab_1_havuzu_harekesiz + \
    nakis_fiil_bab_2_havuzu_harekesiz + \
    nakis_fiil_bab_3_havuzu_harekesiz + \
    nakis_fiil_bab_4_havuzu_harekesiz + \
    nakis_fiil_bab_5_havuzu_harekesiz

# Butun sahih fiiller
sahih_fiil_havuzu_harekesiz = \
    salim_fiil_havuzu_harekesiz + \
    sahih_mehmuz_fiil_havuzu_harekesiz + \
    sahih_muzaaf_fiil_havuzu_harekesiz
# Butun mutel filler
mutel_fiil_havuzu_harekesiz = \
    misal_fiil_havuzu_harekesiz + \
    ecvef_fiil_havuzu_harekesiz + \
    nakis_fiil_havuzu_harekesiz + \
    lefif_fiil_havuzu_harekesiz

# Butun fiiller
fiil_havuzu_harekesiz = \
    sahih_fiil_havuzu_harekesiz + \
    mutel_fiil_havuzu_harekesiz


if __name__ == '__main__':
    print('Salim Filler:\n ', salim_fiil_havuzu_harekesiz)
    print('Sahih Mehmuz Fiiller:\n', sahih_mehmuz_fiil_havuzu_harekesiz)
    print('Sahih Muzaaf Filler:\n', sahih_muzaaf_fiil_havuzu_harekesiz)
    print('Misal Filler:\n', misal_fiil_havuzu_harekesiz)
    print('Ecvef Filler:\n', ecvef_fiil_havuzu_harekesiz)
    print('Nakıs Fiiller:\n', nakis_fiil_havuzu_harekesiz)
    print('Lefif Fiiller:\n', lefif_fiil_havuzu_harekesiz)
    print('Sahih Fiiller:\n', sahih_fiil_havuzu_harekesiz)
    print('Mutel Fiiller:\n', mutel_fiil_havuzu_harekesiz)
    print('Fiiller:\n', fiil_havuzu_harekesiz)




'''