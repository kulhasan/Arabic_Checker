

import aaa1_tanimlar as ta
import aaa3_Bablarina_ve_Aksam_i_seba_ya_gore_fiiller as b6a7
import aaa2_fiil_deposu_1 as fd1

class Ism_i_Mefuller:
    def __init__(self, ism_i_meful):
        self.ism_i_meful = ism_i_meful
        self.salim_fiil_ism_i_meful_mufred_muzekker = self.salim_fiil_ism_i_meful_mufred_muzekker_ceker()
        self.salim_fiil_ism_i_meful_musenna_muzekker = self.salim_fiil_ism_i_meful_musenna_muzekker_ceker()
        self.salim_fiil_ism_i_meful_cemi_muzekker_salim = self.salim_fiil_ism_i_meful_cemi_muzekker_salim_ceker()
        self.salim_fiil_ism_i_meful_cemi_mukesser_muzekker_1 = self.salim_fiil_ism_i_meful_cemi_mukesser_muzekker_1_ceker()
        self.salim_fiil_ism_i_meful_mufred_muennes = self.salim_fiil_ism_i_meful_mufred_muennes_ceker()
        self.salim_fiil_ism_i_meful_musenna_muennes = self.salim_fiil_ism_i_meful_musenna_muennes_ceker()
        self.salim_fiil_ism_i_meful_cemi_muennes_salim = self.salim_fiil_ism_i_meful_cemi_muennes_salim_ceker()


    def salim_fiil_ism_i_meful_mufred_muzekker_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.CEZIM + fiil[1] + ta.DAMME + ta.VAV + \
              fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_meful_musenna_muzekker_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.CEZIM + fiil[1] + ta.DAMME + ta.VAV + \
              fiil[2] + ta.FETHA + ta.ELIF + ta.NUN + ta.KESRA
        return tmp

    def salim_fiil_ism_i_meful_cemi_muzekker_salim_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.CEZIM + fiil[1] + ta.DAMME + ta.VAV + \
              fiil[2] + ta.DAMME + ta.VAV + ta.NUN + ta.FETHA
        return tmp

    def salim_fiil_ism_i_meful_cemi_mukesser_muzekker_1_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + ta.YE_NOKTALI + \
              fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_ism_i_meful_mufred_muennes_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.CEZIM + fiil[1] + ta.DAMME + ta.VAV + \
              fiil[2] + ta.FETHA + ta.TE_KAPALI + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_meful_musenna_muennes_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.CEZIM + fiil[1] + ta.DAMME + ta.VAV + \
              fiil[2] + ta.FETHA + ta.TE + ta.ELIF + ta.NUN + ta.KESRA
        return tmp

    def salim_fiil_ism_i_meful_cemi_muennes_salim_ceker(self):
        tmp = ta.MIM + ta.FETHA + fiil[0] + ta.CEZIM + fiil[1] + ta.DAMME + ta.VAV + \
              fiil[2] + ta.FETHA + ta.ELIF + ta.TE + ta.TENVIN_DAMME
        return tmp

    def yazdir(self):
        print(f"Fiilimiz : {self.ism_i_meful}")
        print(f"Fiilimizin mazi malum çekimleri aşağıdaki gibidir: \
        \n{self.salim_fiil_ism_i_meful_mufred_muzekker} \
        \n{self.salim_fiil_ism_i_meful_musenna_muzekker} \
        \n{self.salim_fiil_ism_i_meful_cemi_muzekker_salim} \
        \n{self.salim_fiil_ism_i_meful_cemi_mukesser_muzekker_1} \
        \n{self.salim_fiil_ism_i_meful_mufred_muennes} \
        \n{self.salim_fiil_ism_i_meful_musenna_muennes} \
        \n{self.salim_fiil_ism_i_meful_cemi_muennes_salim}")


if __name__ == '__main__':
    ism_i_mefuller_havuzu = list()
    for fiil in b6a7.salim_fiil_havuzu:
        ism_i_meful_bir = Ism_i_Mefuller(fiil)
        ism_i_meful_bir.yazdir()
        ism_i_mefuller_havuzu.append(ism_i_meful_bir)




