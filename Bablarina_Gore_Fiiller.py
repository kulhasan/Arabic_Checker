
# Bu sayfanın hedefi: Fiilleri, bablarına göre listelemek.

import tanimlar as ta
import fiil_deposu_1 as fd1
import fiil_deposu_2 as fd2



salim_fiil_bab_1_havuzu = []
salim_fiil_bab_2_havuzu = []
salim_fiil_bab_3_havuzu = []
salim_fiil_bab_4_havuzu = []
salim_fiil_bab_5_havuzu = []
salim_fiil_bab_6_havuzu = []

salim_fiil_bab_havuzu_listesi = \
    salim_fiil_bab_1_havuzu + \
    salim_fiil_bab_2_havuzu + \
    salim_fiil_bab_3_havuzu + \
    salim_fiil_bab_4_havuzu + \
    salim_fiil_bab_5_havuzu + \
    salim_fiil_bab_6_havuzu


for key, value in fd2.salim_fiil_bab_havuzu_dict.items():
    if value == 1:
        salim_fiil_bab_1_havuzu.append(key)
        #print(salim_fiil_bab_1_havuzu)

    if value == 2:
        salim_fiil_bab_2_havuzu.append(key)
        #print(salim_fiil_bab_2_havuzu)


# todo gecici bir uygulama:
# todo program duzelene kadar salim fiil bab 1 mazi malum fiil ceker sayfasundaki fonksiyonun hata vermemesi icin
# todo alttaki liste kullanilacak.
# todo bablarina gorefiiller listesi hallolunca bu liste silinecek.

#salim_fiil_bab_1_havuzu = ['كتب']
#salim_fiil_bab_2_havuzu = ['جلس']

# todo ustteki iki liste gecicidir


'''


fiilturusalim = []


for key in salim_fiil_bab_havuzu:
    if key == fiilturusalim:
        salim_fiil_bab_1_havuzu.append(key)

'''

if __name__ == '__main__':
    print('Salim fiil birinci bab havuzu:\n ', salim_fiil_bab_1_havuzu)
    print('Salim fiil ikinci bab avuzu:\n ', salim_fiil_bab_2_havuzu)

