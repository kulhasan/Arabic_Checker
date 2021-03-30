# Gerekli paketleri alalim
import pandas as pd

# dataframe excel tablosu gibi olan python veri turu
# dataframe in temel yapitasi sutunlar
irab_alametleri_df = pd.DataFrame()

irab_alametleri_df['Kelime Cesidi']=['Mufred Isim', 'Musenna Isim', 'Cem-i Muzekker Salim', 'Cem-i Muennes Salim', 'Cem-i Mukesser']
irab_alametleri_df['Ref'] = ['Damme', 'Elif', 'Vav', 'Damme', 'Damme']
irab_alametleri_df['Nasb'] = ['Fetha', 'Ya', 'Ya', 'Kesra', 'Fetha']
irab_alametleri_df['Cer'] = ['Kesra', 'Ya', 'Ya', 'Kesra', 'Kesra']
print(irab_alametleri_df)
# set_index metodu dataframe icin bir tane birinci sutun seciyor.
# inplace argumani direk dataframe uzerinde degisiklik yapilmasini sagliyor
# dataframeler ile calisirken normalde dataframein hic degistirilmemesi beklenir
# Asagidaki iki satir ayni islevi goruyor
# irab_alametleri_df = irab_alametleri_df.set_index("Kelime Cesidi")
irab_alametleri_df.set_index("Kelime Cesidi", inplace=True)
print(irab_alametleri_df)

# to_excel metodu dataframe i excele yazdirir, ilk arguman excel dosyasinin adi.
# header argunmani sutun basliklarini excel icin de baslik olarak kabul ediyor.
# index=False argumani eklenirse, index sutunu excel dosyasina yazilmaz, Ornek yazim:
# irab_alametleri_df.to_excel('irab_alametleri.xls', header = True, index = False)
irab_alametleri_df.to_excel('irab_alametleri.xls', header = True)



