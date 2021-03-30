
# Bu sayfada aksam-i seba konusu formule edilmistir


import tanimlar as ta
import fiil_deposu_1 as fd1
import fiil_deposu_2 as fd2


salim_fiil_havuzu = []
sahih_mehmuz_fiil_havuzu = []
sahih_muzaaf_fiil_havuzu = []
misal_fiil_havuzu = []
ecvef_fiil_havuzu = []
nakis_fiil_havuzu = []
lefif_i_makrun_fiil_havuzu = []
lefif_i_mefruk_fiil_havuzu = []


for fiil in fd1.fiil_havuzu:
    if (fiil[0] not in ta.GAYR_SALIM) and \
            (fiil[1] not in ta.GAYR_SALIM) and \
            (fiil[2] not in ta.GAYR_SALIM):
        salim_fiil_havuzu.append(fiil)

    elif (fiil[0] not in ta.ILLET_HARFI) and \
            (fiil[1] not in ta.ILLET_HARFI) and \
            (fiil[2] == ta.SEDDE):
        sahih_muzaaf_fiil_havuzu.append(fiil)

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI and \
            (fiil[0] in ta.HEMZE or fiil[1] in ta.HEMZE or fiil[2] in ta.HEMZE):
        sahih_mehmuz_fiil_havuzu.append(fiil)

    elif fiil[0] in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        misal_fiil_havuzu.append(fiil)

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] not in ta.ILLET_HARFI:
        ecvef_fiil_havuzu.append(fiil)

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] not in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        nakis_fiil_havuzu.append(fiil)

    elif fiil[0] not in ta.ILLET_HARFI and \
            fiil[1] in ta.ILLET_HARFI and \
            fiil[2] in ta.ILLET_HARFI:
        lefif_i_makrun_fiil_havuzu.append(fiil)

    elif fiil[0] in ta.ILLET_HARFI and \
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
    print('Salim Fiiller: ',
          #todo satir atlatmamiz gerekiyor.
          salim_fiil_havuzu)
    print('Sahih Mehmuz Fiiller',
          sahih_mehmuz_fiil_havuzu)
    print('Sahih Muzaaf Fiiller: ',
          sahih_muzaaf_fiil_havuzu)
    print('Misal Fiiller: ',
          misal_fiil_havuzu)
    print('Ecvef Fiiller: ',
          ecvef_fiil_havuzu)
    print('Nakıs Fiiller: ',
          nakis_fiil_havuzu)
    print('Lefif-i Makrun Fiiller: ',
          lefif_i_makrun_fiil_havuzu)
    print('Lefif-i Mefruk Fiiller: ',
          lefif_i_mefruk_fiil_havuzu)
