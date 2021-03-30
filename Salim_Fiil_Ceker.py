# Salim mazi malum fiillerin 6 babinin kiplere gore cekimini yapan program


import fiil_deposu_1 as fd1
import Aksam_i_Seba as aseba
from salim_fiil_ifal_babi import salim_fiil_ifal_babi as sfifalb
from Salim_Fiil_Bab_1_Mazi_Malum_Fiil_Ceker import Fiiller as sfb1mmfc

class Fiiller:
    """
    Fiiler classi sunu yapar
    """
    def __init__(self, fii):
        """
            Fiiller objesi olusturma fonksiyonu, kok fiilin her cekimini yapiyor
        :param fii: Kok fiil, kendi harekeleriyle geliyor
        """
        self.fiil = fii
        self.bab = self.sulasi_bab_bul(fii)
        #todo self fiil turu
        # self.fiil_turu = tanimlardan salim fiil formulu cagir
        # todo bir ust satirdaki formul nasil olacak. havuzdaki fiilin salim olup olmadigi
        #  anlasiliyor ama olmayan bir fiilin formulu nasil olacak cozemedim
        self.fiil_turu = aseba.fiil_turu_bul(fii)

        # todo self.fiil_turu formulu hazirlanmali
        # todo salimfiil bablara gore cekimleri ayri bir sayfada formule etmeli
        if self.fiil_turu == 'Salim_Fiil':
            self.salim_fiil_ifal_babi_cekimleri = sfifalb(fii)
            self.salim_fiil_mazi_malum_fiil_cekimleri = self.baba_gore_cek(fii, self.bab)
        else:
            print("Bu fiil salim fiil degildir. Programimizin bu kismi hala gelistirme asamsinda.")

    def baba_gore_cek(self, fiil, bab):
        if bab == 1:
            return sfb1mmfc(fiil)

    def sulasi_bab_bul(self, fiil):
        print("Bab kontrol", fiil)
        bab = fd1.sulasi_fiil_bab_havuzu_dict.get(fiil)
        if not bab:
            command = input("Bu fiilin babi bab havuzumuzda gozukmuyor. Eklemek icin ekle yaziniz.")
            if command == 'ekle':
                pass # ekleme fonksiyonunu calistir
            else:
                print("Sen bilirsin")
        print("bab :", bab)
        return bab


    def yazdir(self):
        print(self.fiil)
        print(self.fiil_turu)
        print(self.bab, '. Bab')
        self.salim_fiil_mazi_malum_fiil_cekimleri.yazdir()
        self.salim_fiil_ifal_babi_cekimleri.yazdir()



if __name__ == '__main__':
    fiiller_havuzu = list()
    # todo for fiil in fd1.salim_fiil_bab_111111111????????/
    # todo sadece bab 1 den degil bab ikiden de nasil cagiracagiz ayni anda
    # todo or yazinca bab 1 den cagiriyor and yazinca bab 2 den cagiriyor
    for fiil in fd1.sulasi_fiil_havuzu_list:
        fiil_bir = Fiiller(fiil)
        fiil_bir.yazdir()



