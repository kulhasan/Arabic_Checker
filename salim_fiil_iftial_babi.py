

import tanimlar as ta
import Aksam_i_Seba as aseba


# todo iftial babinda fiilin kokunun ilk harfi sebebiyle bazi degisiklikler olur.
#  bunlar if statementlerle formule edilmeli
class salim_fiil_iftial_babi:
    def __init__(self, fii):
        self.fiil = fii
        self.salim_fiil_iftial_babi_mazi_malum_gaib = self.salim_fiil_iftial_babi_mazi_malum_gaib_ceker()
        self.salim_fiil_iftial_babi_muzari_malum_gaib = self.salim_fiil_iftial_babi_muzari_malum_gaib_ceker()
        self.salim_fiil_iftial_babi_ismi_fail = self.salim_fiil_iftial_babi_ismi_fail_ceker()
        self.salim_fiil_iftial_babi_emri_hazir = self.salim_fiil_iftial_babi_emri_hazir_ceker()
        self.salim_fiil_iftial_babi_mastar = self.salim_fiil_iftial_babi_mastar_ceker()
        self.salim_fiil_iftial_babi_mazi_mechul_gaib = self.salim_fiil_iftial_babi_mazi_mechul_gaib_ceker()
        self.salim_fiil_iftial_babi_muzari_mechul_gaib = self.salim_fiil_iftial_babi_muzari_mechul_gaib_ceker()
        self.salim_fiil_iftial_babi_ismi_meful = self.salim_fiil_iftial_babi_ismi_meful_ceker()
# todo iftial babinin fa sinda ve ta sinda gereken de[';'kl'kler if statementlerle izah edilecek
    def salim_fiil_iftial_babi_mazi_malum_gaib_ceker(self):
        tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.TE+ ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.FETHA
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.TI + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.FETHA

        if self.fiil[0] == ta.DAL or self.fiil[0] == ta.ZEL or self.fiil[0] == ta.ZE:
            tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.DAL + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.FETHA

        if self.fiil[0] == ta.SE or self.fiil[0] == ta.VAV or self.fiil[0] == ta.YE_NOKTALI:
            tmp = ta.ELIF + ta.KESRA + ta.TE + ta.SEDDE + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_iftial_babi_muzari_malum_gaib_ceker(self):
        tmp = ta.YE_NOKTALI + ta.FETHA + self.fiil[0] + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.DAMME
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.YE_NOKTALI + ta.FETHA + self.fiil[0] + ta.CEZIM + ta.TI + ta.FETHA + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_iftial_babi_ismi_fail_ceker(self):
        tmp = ta.MIM + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.TENVIN_DAMME
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.MIM + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TI + ta.FETHA + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_iftial_babi_emri_hazir_ceker(self):
        tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.CEZIM
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.TI + ta.FETHA + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.CEZIM
        return tmp

    def salim_fiil_iftial_babi_mastar_ceker(self):
        tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.TE + ta.KESRA + self.fiil[1] + ta.FETHA + ta.ELIF + self.fiil[2] + ta.TENVIN_DAMME
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.ELIF + ta.KESRA + self.fiil[0] + ta.CEZIM + ta.TI + ta.KESRA + self.fiil[1] + ta.FETHA + ta.ELIF + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_iftial_babi_mazi_mechul_gaib_ceker(self):
        tmp = ta.ELIF + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TE+ ta.DAMME + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.FETHA
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.ELIF + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TI + ta.DAMME + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_iftial_babi_muzari_mechul_gaib_ceker(self):
        tmp = ta.YE_NOKTALI + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.DAMME
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.YE_NOKTALI + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TI + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_iftial_babi_ismi_meful_ceker(self):
        tmp = ta.MIM + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.TENVIN_DAMME
        if self.fiil[0] == ta.SAD or self.fiil[0] == ta.DAT or self.fiil[0] == ta.TI or self.fiil[0] == ta.ZI:
            tmp = ta.MIM + ta.DAMME + self.fiil[0] + ta.CEZIM + ta.TI + ta.FETHA + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def yazdir(self):
        print(f'Fiilimizin sulasi mucerred koku: {self.fiil}')
        print(f'Fiilimizin iftial babi cekimleri su sekildedir: \
        \n{self.salim_fiil_iftial_babi_mazi_malum_gaib} \
        \n{self.salim_fiil_iftial_babi_muzari_malum_gaib} \
        \n{self.salim_fiil_iftial_babi_ismi_fail} \
        \n{self.salim_fiil_iftial_babi_emri_hazir} \
        \n{self.salim_fiil_iftial_babi_mastar} \
        \n{self.salim_fiil_iftial_babi_mazi_mechul_gaib} \
        \n{self.salim_fiil_iftial_babi_muzari_mechul_gaib} \
        \n{self.salim_fiil_iftial_babi_ismi_meful}')


if __name__ == '__main__':
    fiiller_havuzu = list()
    for fiil in aseba.salim_fiil_havuzu:
        fiil_bir = salim_fiil_iftial_babi(fiil)
        fiil_bir.yazdir()
        fiiller_havuzu.append(fiil_bir)

