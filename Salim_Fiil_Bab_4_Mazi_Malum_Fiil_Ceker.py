

# Salim fiillerin 4. babinin kiplere gore mazi malum cekimini yapan program

import aaa1_tanimlar as ta
import aaa3_Bablarina_ve_Aksam_i_seba_ya_gore_fiiller as b6a7


#todo Fiiller class inin ismi degismeli mi ornek: Salim fiiller ya da salim fiil birinc bab fiilleri gibi


class Fiiller:
    """
    Fiiler classi sunu yapar
    """
    def __init__(self, fii):
        """
            Fiiller objesi olusturma fonksiyonu, kok fiilin her cekimini yapiyor
        :param fii: Kok fiil, kendi harekeleriyle geliyordu ama artık harekesiz geliyor
        """
        self.fiil = fii
        self.salim_fiil_bab_4_mazi_malum_gaib = self.salim_fiil_bab_4_mazi_malum_gaib_ceker()
        self.salim_fiil_bab_4_mazi_malum_gaiban = self.salim_fiil_bab_4_mazi_malum_gaiban_ceker()
        self.salim_fiil_bab_4_mazi_malum_gaibun = self.salim_fiil_bab_4_mazi_malum_gaibun_ceker()
        self.salim_fiil_bab_4_mazi_malum_gaibe = self.salim_fiil_bab_4_mazi_malum_gaibe_ceker()
        self.salim_fiil_bab_4_mazi_malum_gaibetan = self.salim_fiil_bab_4_mazi_malum_gaibetan_ceker()
        self.salim_fiil_bab_4_mazi_malum_gaibat = self.salim_fiil_bab_4_mazi_malum_gaibat_ceker()
        self.salim_fiil_bab_4_mazi_malum_muhatab = self.salim_fiil_bab_4_mazi_malum_muhatab_ceker()
        self.salim_fiil_bab_4_mazi_malum_muhataban = self.salim_fiil_bab_4_mazi_malum_muhataban_ceker()
        self.salim_fiil_bab_4_mazi_malum_muhatabun = self.salim_fiil_bab_4_mazi_malum_muhatabun_ceker()
        self.salim_fiil_bab_4_mazi_malum_muhataba = self.salim_fiil_bab_4_mazi_malum_muhataba_ceker()
        self.salim_fiil_bab_4_mazi_malum_muhatabetan = self.salim_fiil_bab_4_mazi_malum_muhatabetan_ceker()
        self.salim_fiil_bab_4_mazi_malum_muhatabat = self.salim_fiil_bab_4_mazi_malum_muhatabat_ceker()
        self.salim_fiil_bab_4_mazi_malum_mutekellim = self.salim_fiil_bab_4_mazi_malum_mutekellim_ceker()
        self.salim_fiil_bab_4_mazi_malum_mutekelliman = self.salim_fiil_bab_4_mazi_malum_mutekelliman_ceker()
        self.salim_fiil_bab_4_mazi_malum_mutekellimun = self.salim_fiil_bab_4_mazi_malum_mutekellimun_ceker()
        self.salim_fiil_bab_4_mazi_malum_mutekellime = self.salim_fiil_bab_4_mazi_malum_mutekellime_ceker()
        self.salim_fiil_bab_4_mazi_malum_mutekellimetan = self.salim_fiil_bab_4_mazi_malum_mutekellimetan_ceker()
        self.salim_fiil_bab_4_mazi_malum_mutekellimat = self.salim_fiil_bab_4_mazi_malum_mutekellimat_ceker()

    def salim_fiil_bab_4_mazi_malum_gaib_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + \
              ta.KESRA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_bab_4_mazi_malum_gaiban_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + \
            ta.KESRA + self.fiil[2] + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_gaibun_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + \
            ta.KESRA + self.fiil[2] + ta.DAMME + ta.VAV + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_gaibe_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + \
            ta.KESRA + self.fiil[2] + ta.FETHA + ta.TE + ta.CEZIM
        return tmp

    def salim_fiil_bab_4_mazi_malum_gaibetan_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.FETHA + ta.TE + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_gaibat_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.NUN + ta.FETHA
        return tmp

    def salim_fiil_bab_4_mazi_malum_muhatab_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
              self.fiil[2] + ta.CEZIM + ta.TE + ta.FETHA
        return tmp

    def salim_fiil_bab_4_mazi_malum_muhataban_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.TE + ta.DAMME + \
            ta.MIM + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_muhatabun_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.TE + ta.DAMME + \
            ta.MIM + ta.CEZIM
        return tmp

    def salim_fiil_bab_4_mazi_malum_muhataba_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
              self.fiil[2] + ta.CEZIM + ta.TE + ta.KESRA
        return tmp

    def salim_fiil_bab_4_mazi_malum_muhatabetan_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.TE + ta.DAMME + \
            ta.MIM + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_muhatabat_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.TE + ta.DAMME + \
            ta.DAMME + ta.NUN + ta.SEDDE + ta.FETHA
        return tmp

    def salim_fiil_bab_4_mazi_malum_mutekellim_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
              self.fiil[2] + ta.CEZIM + ta.TE + ta.DAMME
        return tmp

    def salim_fiil_bab_4_mazi_malum_mutekelliman_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.NUN + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_mutekellimun_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.NUN + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_mutekellime_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
              self.fiil[2] + ta.CEZIM + ta.TE + ta.DAMME
        return tmp

    def salim_fiil_bab_4_mazi_malum_mutekellimetan_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.NUN + ta.FETHA + ta.ELIF
        return tmp

    def salim_fiil_bab_4_mazi_malum_mutekellimat_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.KESRA + \
            self.fiil[2] + ta.CEZIM + ta.NUN + ta.FETHA + ta.ELIF
        return tmp

    def yazdir(self):
        print(f"Fiilimiz : {self.fiil}")
        print(f"Fiilimizin mazi malum çekimleri aşağıdaki gibidir: \
        \n{self.salim_fiil_bab_4_mazi_malum_gaib} \
        \n{self.salim_fiil_bab_4_mazi_malum_gaiban} \
        \n{self.salim_fiil_bab_4_mazi_malum_gaibun} \
        \n{self.salim_fiil_bab_4_mazi_malum_gaibe} \
        \n{self.salim_fiil_bab_4_mazi_malum_gaibetan} \
        \n{self.salim_fiil_bab_4_mazi_malum_gaibat} \
        \n{self.salim_fiil_bab_4_mazi_malum_muhatab} \
        \n{self.salim_fiil_bab_4_mazi_malum_muhataban} \
        \n{self.salim_fiil_bab_4_mazi_malum_muhatabun} \
        \n{self.salim_fiil_bab_4_mazi_malum_muhataba} \
        \n{self.salim_fiil_bab_4_mazi_malum_muhatabetan} \
        \n{self.salim_fiil_bab_4_mazi_malum_muhatabat} \
        \n{self.salim_fiil_bab_4_mazi_malum_mutekellim} \
        \n{self.salim_fiil_bab_4_mazi_malum_mutekelliman} \
        \n{self.salim_fiil_bab_4_mazi_malum_mutekellimun} \
        \n{self.salim_fiil_bab_4_mazi_malum_mutekellime} \
        \n{self.salim_fiil_bab_4_mazi_malum_mutekellimetan} \
        \n{self.salim_fiil_bab_4_mazi_malum_mutekellimat}")


if __name__ == '__main__':
    fiiller_havuzu = list()
    for fiil in b6a7.salim_fiil_bab_4_fiil_havuzu:
        fiil_bir = Fiiller(fiil)
        fiil_bir.yazdir()
        fiiller_havuzu.append(fiil_bir)




