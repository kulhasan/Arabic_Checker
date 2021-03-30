# 1- Fiil havuzundan bir fiil secilir
# 2- Bu fiil kullaniyica gosterilir
# 3- Her tur rastgele bir zamir kullaniciya gosterilir
# 4- Dogru cevabi vermesi beklenir.


from random import randint
from Salim_Fiil_Ceker import Fiiller
import fiil_deposu_1 as fd1
import tanimlar as ta

asil_salim_fiil_havuzu_harekesiz = list()
for kok_fiil in fd1.fiil_havuzu:
    cekimli_fiil = Fiiller(kok_fiil)
    asil_salim_fiil_havuzu_harekesiz.append(cekimli_fiil)


# print(fd.salim_fiil_havuzu_harekesiz)

for Fiil in asil_salim_fiil_havuzu_harekesiz:
    print(Fiil.yazdir())
    # print(Fiil.salim_mazi_malum_muhatab)
    # print(asil_salim_fiil_havuzu_harekesiz)

working_asil_salim_fiil_havuzu_harekesiz = asil_salim_fiil_havuzu_harekesiz.copy()

zamir_havuzu = {
                'gaib' : 'هو',
                'gaiban' : 'هما(مذكر)',
                'gaibun': 'هم',

                'gaibe' : 'هي',
                'gaibetan' : 'هما(مؤنس)',
                'gaibat' : 'هنّ',

                'muhatab' : 'أنتَ',
                'muhataban' : 'أنتما(مذكر)',
                'muhatabun' : 'أنتم',

                'muhataba' : 'أنتِ',
                'muhatabetan' : 'أنتما(مؤنس)',
                'muhatabat' : 'أنتنّ',

                'mutekellim' : 'أنا(مذكر)',
                'mutekelliman' : 'نحن(مثنّى-مذكر)',
                'mutekellimun' : 'نحن(جمع-مذكر)',

                'mutekellime' : 'أنا(مؤنس)',
                'mutekellimetan' : 'نحن(مثنّى-مؤنس)',
                'mutekellimat' :'نحن(جمع-مؤنس)'
}

rastgele_fiil_nosu = randint(0, len(working_asil_salim_fiil_havuzu_harekesiz) - 1)


rastgele_fiil = working_asil_salim_fiil_havuzu_harekesiz[rastgele_fiil_nosu]
command = ''
fiil_soru_sayisi = 3


tur = 0


while True:
    # while true ne dmek: asagidaki islemi devam ettir. surekli calistir demek.
    # biz bitir komutu verene kadar calistir.
    print(f"Bu turdaki fiiliniz {rastgele_fiil.fiil}")
    rastgele_zamir_nosu = randint(0, len(zamir_havuzu) - 1)
    zamir_tmp = list(zamir_havuzu.keys())
    print(f"Lutfen yukaridaki fiili su zamire gore\
     mazi kipinde cekiniz: {zamir_havuzu[zamir_tmp[rastgele_zamir_nosu]]}")
    command = input("Girdiniz ne olacak? (kapatmak icin 'cikartik' yazin)\nCevap: ")
    # TODO Ogrencilere coktan secmeli 4 sik sunma - dogru secerlerse dogru deme
    tur += 1
    if tur == len(fd1.fiil_havuzu) * fiil_soru_sayisi:
        print(f"Şimdiye kadar {tur} tane soru cevapladiniz. Aferin... ")
        print('Yeter gaari.')
        break

    # fiil_soru_sayisi adedince soru cevaplandiginda fiil otomatik olarak degistiriliyor
    if tur % fiil_soru_sayisi == 0:
        working_asil_salim_fiil_havuzu_harekesiz.remove(rastgele_fiil)
        rastgele_fiil_nosu = randint(0, len(working_asil_salim_fiil_havuzu_harekesiz) - 1)
        rastgele_fiil = working_asil_salim_fiil_havuzu_harekesiz[rastgele_fiil_nosu]

    if command == 'cikartik':
        print("Programimizi kullanip Arapca ogrendiginiz icin bize tesekkur edin!")
        print(f"Şimdiye kadar {tur} tane soru cevapladiniz. Aferin... ")
        break


if __name__ == '__main__':
    print('a')