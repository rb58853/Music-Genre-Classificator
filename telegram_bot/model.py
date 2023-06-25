import mfcc
import wavelet
import pickle
import keras
import os

with open('telegram_bot/dtcwt_rf.bin', 'rb') as archivo:
    model_wavelet = pickle.load(archivo)

model_mfcc = keras.models.load_model('telegram_bot/mfcc_model.h5')
model_ensemble = keras.models.load_model('telegram_bot/ensemble_model.h5')

def get_genre(file):
    file_wavelet = wavelet.get(file)
    file_mfcc = mfcc.get(file)
    out_mfcc = model_mfcc.predict(file_mfcc)
    out_wavelet = model_mfcc.predict(file_wavelet)

    #Esto devuelve un entero
    return model_ensemble.predict([out_mfcc,out_wavelet])
    





