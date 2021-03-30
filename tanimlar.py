
# Gaib = Gaib, Muzekker, Mufred = Huve = هو
# Gaiban = Gaib, Muzekker, Musenna = Huma(Muzekker) = هما(مذكر)
# Gaibun = Gaib, Muzekker, Cemi = Hum = هم
# Gaibe = Gaib, Muennes, Mufred = Hiye = هي
# Gaibetan = Gaib, Muennes, Musenna = Huma(Muennes) = هما(مؤنس)
# Gaibat = Gaib, Muennes, Cemi = Hunne = هنّ
# Muhatab = Muhatab, Muzekker, Mufred = Ente = أنتَ
# Muhataban = Muhatab, Muzekker, Musenna = Entuma(Muzekker) = أنتما(مذكر)
# Muhatabun = Muhatab, Muzekker, Cemi = Entum = أنتم
# Muhataba = Muhatab, Muennes, Mufred = Enti = أنتِ
# Muhatabetan = Muhatab, Muennes, Musenna = Entuma = أنتما(مؤنس)
# Muhatabat = Muhatab, Muennse, Cemi = Entunne = أنتنّ
# Mutekellim = Mutekellim, Muzekker, Mufred = Ene(Muzekker) = أنا(مذكر)
# Mutekelliman = Mutekellim, Muzekker, Musenna = Nahnu(Muzekker-Musenna) نحن(مثنّى-مذكر)
# Mutekellimun = Mutekellim, Muzekker, Cemi = Nahnu(Muzekker-Cemi) = نحن(جمع-مذكر)
# Mutekellime = Mutekellim, Muennes, Mufred = Ene(Muennes) = أنا(مؤنس)
# Mutekellimetan = Mutekellim, Muennes, Musenna = Nahnu(Muennes-Musenna) = نحن(مثنّى-مؤنس)
# Mutekellimat = Mutekellim, Muennes, Cemi =Nahnu(Muennes-Cemi) = نحن(جمع-مؤنس)





# Kipler

gaib = 'gaib_muzekker_mufred'
gaiban = 'gaib_muzekker_musenna'
gaibun = 'gaib_muzekker_cemi'
gaibe = 'gaib_muennes_mufred'
gaibetan = 'gaib_muennes_musenna'
gaibat = 'gaib_muennes_cemi'
muhatab = 'muhatab_muzekker_mufred'
muhataban = 'muhatab_muzekker_musenna'
muhatabun = 'muhatab_muzekker_cemi'
muhataba = 'muhatab_muennes_mufred'
muhatabetan = 'muhatab_muennes_musenna'
muhatabat = 'muhatab_muennes_cemi'
mutekellim = 'mutekellim_muzekker_mufred'
mutekelliman = 'mutekellim_muzekker_musenna'
mutekellimun = 'mutekellim_muzekker_cemi'
mutekellime = 'mutekellim_muennes_mufred'
mutekellimetan = 'mutekellim_muennes_musenna'
mutekellimat = 'mutekellim_muennes_cemi'





# Munfasil Zamirler


HUVE = 'هو'
HUMA_MUZEKKER_MUNFASIL = 'هما'
HUM_MUNFASIL = 'هم'
HIYE = 'هي'
HUMA_MUENNES_MUNFASIL = 'هما'
HUNNE_MUNFASIL = 'هنّ'
ENTE = 'أنتَ'
ENTUMA_MUZEKKER = 'أنتما'
ENTUM = 'أنتم'
ENTI = 'أنتِ'
ENTUMA_MUENNES = 'أنتما'
ENTUNNE = 'أنتنّ'
ENE_MUZEKKER = 'أنا'
NAHNU_MUZEKKER_MUSENNA = 'نحن'
NAHNU_MUZEKKER_CEMI = 'نحن'
ENE_MUENNES = 'أنا'
NAHNU_MUENNES_MUSENNA = 'نحن'
NAHNU_MUENNES_CEMI = 'نحن'

MUNFASIL_ZAMIRLER = [HUVE or HUMA_MUZEKKER_MUNFASIL or HUM_MUNFASIL or
                     HIYE or HUMA_MUENNES_MUNFASIL or HUNNE_MUNFASIL or
                     ENTE or ENTUMA_MUZEKKER or ENTUM or
                     ENTI or ENTUMA_MUENNES or ENTUNNE or
                     ENE_MUZEKKER or NAHNU_MUZEKKER_MUSENNA or NAHNU_MUZEKKER_CEMI or
                     ENE_MUENNES or NAHNU_MUENNES_MUSENNA or NAHNU_MUENNES_CEMI]



# Muttasil Zamirler

HU = 'ه'
HUMA_MUZEKKER_MUTTASIL = 'هما'
HUM_MUTTASIL = 'هم'
HA_ZAMIR = 'ها'
HUMA_MUENNES_MUTTASIL = 'هما'
HUNNE_MUTTASIL = 'هنّ'
KE = 'َك'
KUMA_MUZEKKER = 'كما'
KUM = 'كم'
KI = 'ِك'
KUMA_MUENNES = 'كما'
KUNNE = 'كنّ'
YA_MUZEKKER = 'ى'
NA_MUZEKKER_MUSENNA = 'نا'
NA_MUZEKKER_CEMI = 'نا'
YA_MUENNES = 'ى'
NA_MUENNES_MUSENNA = 'نا'
NA_MUENNES_CEMI = 'نا'

MUTTASIL_ZAMIRLER = [HU or HUMA_MUZEKKER_MUTTASIL or HUM_MUTTASIL or
                     HA_ZAMIR or HUMA_MUENNES_MUTTASIL or HUNNE_MUTTASIL or
                     KE or KUMA_MUZEKKER or KUM or
                     KI or KUMA_MUENNES or KUNNE or
                     YA_MUZEKKER or NA_MUZEKKER_MUSENNA or NA_MUZEKKER_CEMI or
                     YA_MUENNES or NA_MUENNES_MUSENNA or NA_MUENNES_CEMI]

'''
# todo: lazim olursa zamirler gruplandirilabilir.

mufred munfasil zamirler
musenna munfasil xamirler
cemi munfasil zamirler




'''


# Hareke ve isaretler
FETHA = 'َ'
KESRA = 'ِ'
DAMME = 'ُ'
CEZIM = 'ْ'
SEDDE = 'ّ'
TENVIN_FETHA = 'ً'
TENVIN_KESRA = 'ٍ'
TENVIN_DAMME = 'ٌ'

# Arapca Harfler
ELIF = 'ا'
ELIF_MEDLI = 'آ'
BE = 'ب'
TE = 'ت'
TE_KAPALI = 'ة'
SE = 'ث'
CIM = 'ج'
HA = 'ح'
HI = 'خ'
DAL = 'د'
ZEL = 'ذ'
RA = 'ر'
ZE = 'ز'
SIN = 'س'
SHIN = 'ش'
SAD = 'ص'
DAT = 'ض'
TI = 'ط'
ZI = 'ظ'
AYIN = 'ع'
GAYIN = 'غ'
FE = 'ف'
QAF = 'ق'
KEF = 'ك'
LAM = 'ل'
MIM = 'م'
NUN = 'ن'
VAV = 'و'
HE = 'ه'
YE = 'ى'
YE_NOKTALI = 'ي'
HEMZE_YALNIZ = 'ء'
HEMZE_ELIF_USTUNDE = 'أ'
HEMZE_ELIF_ALTINDA = 'إ'
HEMZE_VAV_USTUNDE = 'ؤ'
HEMZE_YE_USTUNDE = 'ئ'


ILLET_HARFI = ELIF + VAV + YE_NOKTALI + YE
harf = ELIF
if harf in ILLET_HARFI:
    print("yes")
HEMZE = HEMZE_YALNIZ + HEMZE_ELIF_USTUNDE + HEMZE_ELIF_ALTINDA + HEMZE_VAV_USTUNDE + HEMZE_YE_USTUNDE

GAYR_SALIM = ILLET_HARFI + HEMZE + SEDDE



# todo aasar karakterinin tanimi yapilmali. klavyedeki yeri neresi
AASAR = ''



# todo salim fiil 6 babin tanimlari yapilmali

fiil_havuzu_harekeli_100 = [
    'نَصَرَ-يَنْصُرُ', 'جَلَسَ-يَجْلِسُ', 'فَتَحَ-يَفْتَحُ',
    'عَلِمَ-يَعْلَمُ', 'حَسُنَ-يَحْسُنُ', 'حَسِبَ-يَحْسِبُ']

sulasi_fiil_bab_1_havuzu = []
sulasi_fiil_bab_2_havuzu = []
sulasi_fiil_bab_3_havuzu = []
sulasi_fiil_bab_4_havuzu = []
sulasi_fiil_bab_5_havuzu = []
sulasi_fiil_bab_6_havuzu = []

sulasi_fiil_bab_1_mazi_fiil_havuzu = []
sulasi_fiil_bab_2_mazi_fiil_havuzu = []
sulasi_fiil_bab_3_mazi_fiil_havuzu = []
sulasi_fiil_bab_4_mazi_fiil_havuzu = []
sulasi_fiil_bab_5_mazi_fiil_havuzu = []
sulasi_fiil_bab_6_mazi_fiil_havuzu = []

sulasi_fiil_bab_1_muzari_fiil_havuzu = []
sulasi_fiil_bab_2_muzari_fiil_havuzu = []
sulasi_fiil_bab_3_muzari_fiil_havuzu = []
sulasi_fiil_bab_4_muzari_fiil_havuzu = []
sulasi_fiil_bab_5_muzari_fiil_havuzu = []
sulasi_fiil_bab_6_muzari_fiil_havuzu = []

for fiil in fiil_havuzu_harekeli_100:
    if fiil[3] == FETHA and fiil[12] == DAMME:
        sulasi_fiil_bab_1_havuzu.append(fiil)
        sulasi_fiil_bab_1_mazi_fiil_havuzu.append(fiil[0] + fiil[1] + fiil[2] + fiil[3] + fiil[4] + fiil[5])
        sulasi_fiil_bab_1_muzari_fiil_havuzu.append(fiil[7] + fiil[8] + fiil[9] + \
        fiil[10] + fiil[11] + fiil[12] + fiil[13] + fiil[14])

    if fiil[3] == FETHA and fiil[12] == KESRA:
        sulasi_fiil_bab_2_havuzu.append(fiil)
        sulasi_fiil_bab_2_mazi_fiil_havuzu.append(fiil[0] + fiil[1] + fiil[2] + fiil[3] + fiil[4] + fiil[5])
        sulasi_fiil_bab_2_muzari_fiil_havuzu.append(fiil[7] + fiil[8] + fiil[9] + \
        fiil[10] + fiil[11] + fiil[12] + fiil[13] + fiil[14])

    if fiil[3] == FETHA and fiil[12] == FETHA:
        sulasi_fiil_bab_3_havuzu.append(fiil)
        sulasi_fiil_bab_3_mazi_fiil_havuzu.append(fiil[0] + fiil[1] + fiil[2] + fiil[3] + fiil[4] + fiil[5])
        sulasi_fiil_bab_3_muzari_fiil_havuzu.append(fiil[7] + fiil[8] + fiil[9] + \
        fiil[10] + fiil[11] + fiil[12] + fiil[13] + fiil[14])

    if fiil[3] == KESRA and fiil[12] == FETHA:
        sulasi_fiil_bab_4_havuzu.append(fiil)
        sulasi_fiil_bab_4_mazi_fiil_havuzu.append(fiil[0] + fiil[1] + fiil[2] + fiil[3] + fiil[4] + fiil[5])
        sulasi_fiil_bab_4_muzari_fiil_havuzu.append(fiil[7] + fiil[8] + fiil[9] + \
        fiil[10] + fiil[11] + fiil[12] + fiil[13] + fiil[14])

    if fiil[3] == DAMME and fiil[12] == DAMME:
        sulasi_fiil_bab_5_havuzu.append(fiil)
        sulasi_fiil_bab_5_mazi_fiil_havuzu.append(fiil[0] + fiil[1] + fiil[2] + fiil[3] + fiil[4] + fiil[5])
        sulasi_fiil_bab_5_muzari_fiil_havuzu.append(fiil[7] + fiil[8] + fiil[9] + \
        fiil[10] + fiil[11] + fiil[12] + fiil[13] + fiil[14])

    if fiil[3] == KESRA and fiil[12] == KESRA:
        sulasi_fiil_bab_6_havuzu.append(fiil)
        sulasi_fiil_bab_6_mazi_fiil_havuzu.append(fiil[0] + fiil[1] + fiil[2] + fiil[3] + fiil[4] + fiil[5])
        sulasi_fiil_bab_6_muzari_fiil_havuzu.append(fiil[7] + fiil[8] + fiil[9] + \
        fiil[10] + fiil[11] + fiil[12] + fiil[13] + fiil[14])


if __name__ == '__main__':
    print(sulasi_fiil_bab_1_havuzu)
    print(sulasi_fiil_bab_2_havuzu)
    print(sulasi_fiil_bab_3_havuzu)
    print(sulasi_fiil_bab_4_havuzu)
    print(sulasi_fiil_bab_5_havuzu)
    print(sulasi_fiil_bab_6_havuzu)
    print(sulasi_fiil_bab_1_mazi_fiil_havuzu)
    print(sulasi_fiil_bab_2_mazi_fiil_havuzu)
    print(sulasi_fiil_bab_3_mazi_fiil_havuzu)
    print(sulasi_fiil_bab_4_mazi_fiil_havuzu)
    print(sulasi_fiil_bab_5_mazi_fiil_havuzu)
    print(sulasi_fiil_bab_6_mazi_fiil_havuzu)
    print(sulasi_fiil_bab_1_muzari_fiil_havuzu)
    print(sulasi_fiil_bab_2_muzari_fiil_havuzu)
    print(sulasi_fiil_bab_3_muzari_fiil_havuzu)
    print(sulasi_fiil_bab_4_muzari_fiil_havuzu)
    print(sulasi_fiil_bab_5_muzari_fiil_havuzu)
    print(sulasi_fiil_bab_6_muzari_fiil_havuzu)
    print(ILLET_HARFI)
    print(GAYR_SALIM)
    print(HEMZE_YALNIZ)






