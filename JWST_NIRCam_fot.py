import os
import shutil               #os, shutil: Biblioteki do operacji na plikach i katalogach oraz kopiowania plików
import pprint
import numpy as np          #Biblioteka do efektywnego przetwarzania danych numerycznych
from scipy.signal import medfilt        #Moduł z biblioteki SciPy do przetwarzania sygnałów

from astropy.utils.data import download_file        #astropy tools,  moduł z biblioteki Astropy do zarządzania danymi astronomicznymi, w tym pobierania plików
from astropy.io import fits         # Moduł do obsługi formatu plików FITS

from jwst import datamodels         #Moduł z biblioteki JWST (James Webb Space Telescope) do modelowania danych z teleskopu JWST
import matplotlib.pyplot as plt         #Biblioteka Matplotlib do tworzenia wykresów i wizualizacji danych
import matplotlib as mpl

#Ustawienia rozdzielczości obrazów:
mpl.rcParams['savefig.dpi'] = 80
mpl.rcParams['figure.dpi'] = 80


def create_image(data_2d, title=None):
    '''Tworzy obraz 2D na podstawie danych '''
    fig = plt.figure(figsize=(8, 8))
    ax = plt.subplot()
    #Określenie kolorów map (cmap) dla różnych typów danych: jeśli typ danych to "IMAGE," używana jest mapa kolorów "CMRmap", jeśli typ danych to "WFSS," używana jest mapa kolorów "gray"
    if 'IMAGE' in data_2d.meta.exposure.type:
        plt.imshow(data_2d.data, origin='lower', cmap='CMRmap', vmin=0, vmax=10)
    elif 'WFSS' in data_2d.meta.exposure.type:
        plt.imshow(data_2d.data, origin='lower', cmap='gray', vmin=-0.05, vmax=0.5)
    plt.xlabel('Pixel column')
    plt.ylabel('Pixel row')
    if title:
        plt.title(title)
    fig.tight_layout()
    plt.subplots_adjust(left=0.15)
    plt.colorbar(label=data_2d.meta.bunit_data)
    #plt.show()

def create_slit_image(data_2d, slit_number, title=None):
    '''Tworzy obraz 2D na podstawie danych '''
    fig = plt.figure(figsize=(8, 8))
    ax = plt.subplot()
    plt.imshow(data_2d.slits[slit_number].data, origin='lower', cmap='gray',vmin=-0.1, vmax=0.3)
    plt.colorbar(label=data_2d.meta.bunit_data)
    plt.xlabel('Pixel column')
    plt.ylabel('Pixel row')
    if title:
        plt.title(title)
    else:
        title = "object {} order = {}".format(data_2d.slits[slit_number].source_id,
            data_2d.slits[slit_number].meta.wcsinfo.spectral_order)
        plt.title(title)
    plt.subplots_adjust(left=0.15)
    #plt.show()

#Określenie adresu URL do różnych plików FITS, które zostaną pobrane i przetworzone:

rate_file = ["https://stsci.box.com/shared/static/h30hhwhu4ihlhqjnlhbblx07wnitoytd.fits",
"example_nircam_imaging_rate.fits"]
rateints_file = ["https://stsci.box.com/shared/static/jh937bjqodqhfobhpemnbqt4jax6d6j4.fits",
"example_nircam_imaging_rateints.fits"]
ramp_file = ["https://stsci.box.com/shared/static/x7d0ldm7bp683p5yyi2buvphjcckujbe.fits",
"example_nircam_imaging_ramp.fits"]
wfss_rate_file = ["https://stsci.box.com/shared/static/d5k9z5j05dgfv6ljgie483w21kmpevni.fits",
"example_nircam_wfss_rate.fits"]
cal_file = ["https://stsci.box.com/shared/static/8g15cxb3nri47l3bx22mjtdw3yt8xxiv.fits",
"example_nircam_imaging_cal.fits"]
wfss_cal_file = ["https://stsci.box.com/shared/static/pqgt98wsjz16av3768756ierahzqn8w7.fits",
"example_nircam_wfss_cal.fits"]
wfss_x1d_file = ["https://stsci.box.com/shared/static/fjzq3dm2kgp2ttoptxwe9yfghmxxxz89.fits",
"example_nircam_wfss_x1d.fits"]
demo_ex_file = ["https://stsci.box.com/shared/static/6vn402728z12cyx6czdt5hpaxa071aek.fits",
"example_exercise_cal.fits"]
all_files = [rate_file, rateints_file, ramp_file, cal_file,
    wfss_rate_file, wfss_cal_file, wfss_x1d_file,
    demo_ex_file]
for file in all_files:
    demo_file = download_file(file[0], cache=True)
    shutil.copy(demo_file, file[1])

#Ładowanie pobranych plików FITS do modeli danych JWST za pomocą klas ImageModel, CubeModel i MultiSlitModel:

#Ładowanie danych uśrednionych przez integrację do modelu (rate_image)
rate_image = datamodels.ImageModel(rate_file[1])

#Ładowanie poszczególnych integracji do modelu (rateints_image)
rateints_image = datamodels.CubeModel(rateints_file[1])

#tworzy nowy obiekt na podstawie modelu danych dostarczonego w pliku FITS
wfss_image = datamodels.MultiSlitModel(wfss_rate_file[1])


# Sprawdzanie pliku za pomocą funkcji .info()
#rate_image.info()
wfss_image.info()

print("Shape:")

#  wypisuje kształt (shape) tablicy danych 'data' z obiektu .rate_image, .wfss_image
#print(rate_image.data.shape)
print(wfss_image.data.shape)

print("Number of slits:")

number_of_slits = len(wfss_image.slits)
print(number_of_slits)

#print("Creating image:")

# Tworzy zdjęcie z danych 'rate_image'
#plt.figure()
create_image(rate_image, title="Its full of stars!")

print("Creating slit image:")
#plt.figure()
create_slit_image(wfss_image, 0)

plt.show()  #Pokazuje oba wykresy naraz


