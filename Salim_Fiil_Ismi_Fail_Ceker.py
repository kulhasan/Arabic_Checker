

import aaa1_tanimlar as ta
import aaa3_Bablarina_ve_Aksam_i_seba_ya_gore_fiiller as b6a7
import aaa2_fiil_deposu_1 as fd1

class Ism_i_Failler:
    def __init__(self, ism_i_fail):
        self.ism_i_fail = ism_i_fail
        self.salim_fiil_ism_i_fail_mufred_muzekker = self.salim_fiil_ism_i_fail_mufred_muzekker_ceker()
        self.salim_fiil_ism_i_fail_musenna_muzekker = self.salim_fiil_ism_i_fail_musenna_muzekker_ceker()
        self.salim_fiil_ism_i_fail_cemi_muzekker_salim = self.salim_fiil_ism_i_fail_cemi_muzekker_salim_ceker()
        self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_1 = self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_1_ceker()
        self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_2 = self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_2_ceker()
        self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_3 = self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_3_ceker()
        self.salim_fiil_ism_i_fail_mufred_muennes = self.salim_fiil_ism_i_fail_mufred_muennes_ceker()
        self.salim_fiil_ism_i_fail_musenna_muennes = self.salim_fiil_ism_i_fail_musenna_muennes_ceker()
        self.salim_fiil_ism_i_fail_cemi_muennes_salim = self.salim_fiil_ism_i_fail_cemi_muennes_salim_ceker()
        self.salim_fiil_ism_i_fail_cemi_mukesser_muennes = self.salim_fiil_ism_i_fail_cemi_mukesser_muennes_ceker()


    def salim_fiil_ism_i_fail_mufred_muzekker_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_fail_musenna_muzekker_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.FETHA + ta.ELIF + ta.NUN + ta.KESRA
        return tmp

    def salim_fiil_ism_i_fail_cemi_muzekker_salim_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.DAMME + ta.VAV + ta.NUN + ta.FETHA
        return tmp

    def salim_fiil_ism_i_fail_cemi_mukesser_muzekker_1_ceker(self):
        tmp = fiil[0] + ta.DAMME + fiil[1] + ta.SEDDE + ta.FETHA + ta.ELIF + fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_fail_cemi_mukesser_muzekker_2_ceker(self):
        tmp = fiil[0] + ta.DAMME + fiil[1] + ta.SEDDE + ta.FETHA + fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_fail_cemi_mukesser_muzekker_3_ceker(self):
        tmp = fiil[0] + ta.FETHA + fiil[1] + ta.FETHA + fiil[2] + ta.FETHA + ta.TE_KAPALI + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_fail_mufred_muennes_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.FETHA + ta.TE_KAPALI + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_fail_musenna_muennes_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.FETHA + \
              ta.TE + ta.FETHA + ta.ELIF + ta.NUN + ta.KESRA
        return tmp

    def salim_fiil_ism_i_fail_cemi_muennes_salim_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.FETHA + \
              ta.ELIF + ta.TE + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_ism_i_fail_cemi_mukesser_muennes_ceker(self):
        tmp = fiil[0] + ta.FETHA + ta.VAV + ta.FETHA + ta.ELIF + fiil[1] + ta.KESRA + fiil[2] + ta.DAMME
        return tmp

    def yazdir(self):
        print(f"Fiilimiz : {self.ism_i_fail}")
        print(f"Fiilimizin mazi malum çekimleri aşağıdaki gibidir: \
        \n{self.salim_fiil_ism_i_fail_mufred_muzekker} \
        \n{self.salim_fiil_ism_i_fail_musenna_muzekker} \
        \n{self.salim_fiil_ism_i_fail_cemi_muzekker_salim} \
        \n{self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_1} \
        \n{self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_2} \
        \n{self.salim_fiil_ism_i_fail_cemi_mukesser_muzekker_3} \
        \n{self.salim_fiil_ism_i_fail_mufred_muennes} \
        \n{self.salim_fiil_ism_i_fail_musenna_muennes} \
        \n{self.salim_fiil_ism_i_fail_cemi_muennes_salim} \
        \n{self.salim_fiil_ism_i_fail_cemi_mukesser_muennes}")


if __name__ == '__main__':
    ism_i_failler_havuzu = list()
    for fiil in b6a7.salim_fiil_havuzu:
        ism_i_fail_bir = Ism_i_Failler(fiil)
        ism_i_fail_bir.yazdir()
        ism_i_failler_havuzu.append(ism_i_fail_bir)




