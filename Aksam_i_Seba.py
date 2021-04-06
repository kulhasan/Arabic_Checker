
# Bu sayfada aksam-i seba konusu formule edilmistir


import aaa1_tanimlar as ta
import aaa2_fiil_deposu_1 as fd1


salim_fiil_havuzu = []
sahih_mehmuz_fiil_havuzu = []
# sahih_mehmuz_ul_fa_fiil_havuzu = []
# sahih_mehmuz_ul_ayn_fiil_havuzu = []
# sahih_mehmuz_ul_lam_fiil_havuzu = []
sahih_muzaaf_fiil_havuzu = []
misal_fiil_havuzu = []
# sahih_misal_vavi_fiil_havuzu = []
# sahih_misal_yai_fiil_havuzu = []
ecvef_fiil_havuzu = []
#ecvef_vavi_fiil_havuzu = []
#ecvef_vavi_fiil_havuzu = []
nakis_fiil_havuzu = []
lefif_i_makrun_fiil_havuzu = []
lefif_i_mefruk_fiil_havuzu = []

# Aksam-ı Seb'a'ya göre listelemek için aşağıdaki formüller hazırlanmıştır.

for fiil in fd1.fiil_havuzu_list:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if (fiil[0] not in ta.ILLET_HARFI) and \
            (fiil[1] not in ta.ILLET_HARFI) and \
            (fiil[2] == ta.SEDDE):
        sahih_muzaaf_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI and \
            (fiil[1] not in ta.HEMZE or
             fiil[2] not in ta.HEMZE or
             fiil[0] in ta.HEMZE):
        sahih_mehmuz_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        ecvef_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_makrun_fiil_havuzu.append(fiil)

for fiil in fd1.fiil_havuzu_list:
    if fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_mefruk_fiil_havuzu.append(fiil)


def fiil_turu_bul(fiil):
    if fiil[0] not in ta.GAYR_SALIM and \
            fiil[1] not in ta.GAYR_SALIM and \
            fiil[2] not in ta.GAYR_SALIM:
        return 'Salim_Fiil'

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI and \
            (fiil[0] in ta.HEMZE or fiil[1] in ta.HEMZE or fiil[2] in ta.HEMZE):
        return 'Sahih_Mehmuz_Fiil'

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] == ta.SEDDE:
        return 'Sahih_Muzaaf_Fiil'

    elif fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        return 'Misal_Fiil'

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        return 'Ecvef_Fiil'

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        return 'Nakıs_Fiil'

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        return 'Lefif_i_Makrun_Fiil'

    elif fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        return 'Lefif_i_Mefruk_Fiil'


'''
girdi = input('Bir fiil yaz: ')
for fiil in girdi:
    if (fiil[0] and fiil[1] and fiil[2]) != ta.GAYR_SALIM:
        sahih_mehmuz_fiil_havuzu.append(fiil)

'''

if __name__ == '__main__':
    print('Salim Fiiller:\n ', salim_fiil_havuzu)
    print('Sahih Mehmuz Fiiller:\n', sahih_mehmuz_fiil_havuzu)
    print('Sahih Muzaaf Fiiller:\n ', sahih_muzaaf_fiil_havuzu)
    print('Misal Fiiller:\n ', misal_fiil_havuzu)
    print('Ecvef Fiiller:\n ', ecvef_fiil_havuzu)
    print('Nakıs Fiiller:\n ', nakis_fiil_havuzu)
    print('Lefif-i Makrun Fiiller:\n ', lefif_i_makrun_fiil_havuzu)
    print('Lefif-i Mefruk Fiiller:\n ', lefif_i_mefruk_fiil_havuzu)
