import mfcc
import wavelet

model_mfcc = keras.models.load_model('mfcc_model.h5')
model_wavelet = None
model_ensemble = keras.models.load_model('ensemble_model.h5')

def get_genre(path):
    file_wavelet = wavelet.get(path)
    file_mfcc = mfcc.get(path)
    out_mfcc = model_mfcc.predict(file_mfcc)
    out_wavelet = model_mfcc.predict(file_wavelet)

    #Esto devuelve un entero
    return model_ensemble.predict([out_mfcc,out_wavelet])
    





