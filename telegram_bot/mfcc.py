import librosa


def read_image(filepath):
    global size_images
    image = cv2.imread(filepath)
    return cv2.resize(image, size_images)

def get(audio_path):
    x , sr = librosa.load(audio_path)
    # get_mfcc(x,sr)
    mfccs = librosa.feature.mfcc(y= x, sr=sr)
    return mfccs