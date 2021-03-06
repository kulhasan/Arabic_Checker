'''


import tanimlar as ta
import Aksam_i_Seba as aseba


class salim_fiil_tefil_babi:
    def __init__(self, fii):
        self.fiil = fii
        self.salim_fiil_tefil_babi_mazi_malum_gaib = self.salim_fiil_tefil_babi_mazi_malum_gaib_ceker()
        self.salim_fiil_tefil_babi_muzari_malum_gaib = self.salim_fiil_tefil_babi_muzari_malum_gaib_ceker()
        self.salim_fiil_tefil_babi_ismi_fail = self.salim_fiil_tefil_babi_ismi_fail_ceker()
        self.salim_fiil_tefil_babi_emri_hazir = self.salim_fiil_tefil_babi_emri_hazir_ceker()
        self.salim_fiil_tefil_babi_mastar = self.salim_fiil_tefil_babi_mastar_ceker()
        self.salim_fiil_tefil_babi_mazi_mechul_gaib = self.salim_fiil_tefil_babi_mazi_mechul_gaib_ceker()
        self.salim_fiil_tefil_babi_muzari_mechul_gaib = self.salim_fiil_tefil_babi_muzari_mechul_gaib_ceker()
        self.salim_fiil_tefil_babi_ismi_meful = self.salim_fiil_tefil_babi_ismi_meful_ceker()

    def salim_fiil_tefil_babi_mazi_malum_gaib_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.SEDDE + ta.FETHA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_tefil_babi_muzari_malum_gaib_ceker(self):
        tmp = ta.YE_NOKTALI + ta.DAMME + self.fiil[0] + ta.FETHA + self.fiil[1] + ta.SEDDE + ta.KESRA + self.fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_tefil_babi_ismi_fail_ceker(self):
        tmp = ta.MIM + ta.DAMME + self.fiil[0] + ta.FETHA + self.fiil[1] + ta.SEDDE + ta.KESRA + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_tefil_babi_emri_hazir_ceker(self):
        tmp = self.fiil[0] + ta.FETHA + self.fiil[1] + ta.SEDDE + ta.KESRA + self.fiil[2] + ta.CEZIM
        return tmp

    def salim_fiil_tefil_babi_mastar_ceker(self):
        tmp = ta.TE + ta.FETHA + self.fiil[0] + ta.CEZIM + self.fiil[1] + ta.KESRA + ta.YE_NOKTALI + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def salim_fiil_tefil_babi_mazi_mechul_gaib_ceker(self):
        tmp = self.fiil[0] + ta.DAMME + self.fiil[1] + ta.SEDDE + ta.KESRA + self.fiil[2] + ta.FETHA
        return tmp

    def salim_fiil_tefil_babi_muzari_mechul_gaib_ceker(self):
        tmp = ta.YE_NOKTALI + ta.DAMME + self.fiil[0] + ta.FETHA + self.fiil[1] + ta.SEDDE + ta.FETHA + self.fiil[2] + ta.DAMME
        return tmp

    def salim_fiil_tefil_babi_ismi_meful_ceker(self):
        tmp = ta.MIM + ta.DAMME + self.fiil[0] + ta.FETHA + self.fiil[1] + ta.SEDDE + ta.FETHA + self.fiil[2] + ta.TENVIN_DAMME
        return tmp

    def yazdir(self):
        print(f'Fiilimizin sulasi mucerred koku: {self.fiil}')
        print(f'Fiilimizin tefil babi cekimleri su sekildedir: \
        \n{"Mazi Malum    : "} {self.salim_fiil_tefil_babi_mazi_malum_gaib} \
        \n{"Muzari Malum  : "} {self.salim_fiil_tefil_babi_muzari_malum_gaib} \
        \n{"??sm-i Fail    : "} {self.salim_fiil_tefil_babi_ismi_fail} \
        \n{"??sm-i Meful   : "} {self.salim_fiil_tefil_babi_emri_hazir} \
        \n{"Masdar        : "} {self.salim_fiil_tefil_babi_mastar} \
        \n{"Mazi Me??hul   : "} {self.salim_fiil_tefil_babi_mazi_mechul_gaib} \
        \n{"Muzari Me??hul : "} {self.salim_fiil_tefil_babi_muzari_mechul_gaib} \
        \n{"??sm-i Meful   : "} {self.salim_fiil_tefil_babi_ismi_meful}')


if __name__ == '__main__':
    fiiller_havuzu = list()
    for fiil in aseba.salim_fiil_havuzu:
        fiil_bir = salim_fiil_tefil_babi(fiil)
        fiil_bir.yazdir()
        fiiller_havuzu.append(fiil_bir)

'''
