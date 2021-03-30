
'''

import tanimlar as ta
import Aksam_i_Seba as aseba

class salim_fiil_istifal_babi:
    def __init__(self, fii):
        self.fiil = fii
        self.salim_fiil_istifal_babi_mazi_malum_gaib = self.salim_fiil_istifal_babi_mazi_malum_gaib_ceker()
        self.salim_fiil_istifal_babi_muzari_malum_gaib = self.salim_fiil_istifal_babi_muzari_malum_gaib_ceker()
        self.salim_fiil_istifal_babi_ismi_fail = self.salim_fiil_istifal_babi_ismi_fail_ceker()
        self.salim_fiil_istifal_babi_emri_hazir = self.salim_fiil_istifal_babi_emri_hazir_ceker()
        self.salim_fiil_istifal_babi_mastar = self.salim_fiil_istifal_babi_mastar_ceker()
        self.salim_fiil_istifal_babi_mazi_mechul_gaib = self.salim_fiil_istifal_babi_mazi_mechul_gaib_ceker()
        self.salim_fiil_istifal_babi_muzari_mechul_gaib = self.salim_fiil_istifal_babi_muzari_mechul_gaib_ceker()
        self.salim_fiil_istifal_babi_ismi_meful = self.salim_fiil_istifal_babi_ismi_meful_ceker()

    def salim_fiil_istifal_babi_mazi_malum_gaib_ceker(self):
        tmp = ta.ELIF + ta.KESRA + ta.SIN + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_istifal_babi_muzari_malum_gaib_ceker(self):
        tmp = ta.YE_NOKTALI + ta.FETHA + ta.SIN + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_istifal_babi_ismi_fail_ceker(self):
        tmp = ta.MIM + ta.DAMME + ta.SIN + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_istifal_babi_emri_hazir_ceker(self):
        tmp = ta.ELIF + ta.KESRA + ta.SIN + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.CEZIM
        return tmp

    def salim_fiil_istifal_babi_mastar_ceker(self):
        tmp = ta.ELIF + ta.KESRA + ta.SIN + ta.CEZIM + ta.TE + ta.KESRA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.FETHA + ta.ELIF + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_istifal_babi_mazi_mechul_gaib_ceker(self):
        tmp = ta.ELIF + ta.DAMME + ta.SIN + ta.CEZIM + ta.TE + ta.DAMME + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.KESRA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_istifal_babi_muzari_mechul_gaib_ceker(self):
        tmp = ta.YE_NOKTALI + ta.DAMME + ta.SIN + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_istifal_babi_ismi_meful_ceker(self):
        tmp = ta.MIM + ta.DAMME + ta.SIN + ta.CEZIM + ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.FETHA + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def yazdir(self):
        print(f'Fiilimizin sulasi mucerred koku: {self.fiil}')
        print(f'Fiilimizin istifal babi cekimleri su sekildedir: \
        \n{self.salim_fiil_istifal_babi_mazi_malum_gaib} \
        \n{self.salim_fiil_istifal_babi_muzari_malum_gaib} \
        \n{self.salim_fiil_istifal_babi_ismi_fail} \
        \n{self.salim_fiil_istifal_babi_emri_hazir} \
        \n{self.salim_fiil_istifal_babi_mastar} \
        \n{self.salim_fiil_istifal_babi_mazi_mechul_gaib} \
        \n{self.salim_fiil_istifal_babi_muzari_mechul_gaib} \
        \n{self.salim_fiil_istifal_babi_ismi_meful}')


if __name__ == '__main__':
    fiiller_havuzu = list()
    for fiil in aseba.salim_fiil_havuzu:
        fiil_bir = salim_fiil_istifal_babi(fiil)
        fiil_bir.yazdir()
        fiiller_havuzu.append(fiil_bir)

'''
