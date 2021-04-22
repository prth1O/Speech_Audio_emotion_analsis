import tensorflow as tf
import numpy as np
import librosa




Emot_pred=tf.keras.models.load_model("./CNN_LSTM.h5")
#Age_pred=tf.keras.models.load_model("./AgeDistMdl.h5")
#Gen_pred=tf.keras.models.load_model("./GenDistMdl.h5")

def prediction(file ,FolderPath):

    Emot_pred.predict(file)
    class_names = [ 'neutral', 'happy', 'sad', 'angry', 'fearful' ,'disgust']
    PRED_CLASS=[]
    for i in range(len(Emot_pred)):
        TEST_CLASS.append(class_names[np.argmax(Emot_pred[i])])
    return PRED_CLASS


def chunking(Infile_path,split_file_path):
    sound = AudioSegment.from_wav(Infile_path)

    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )

    if not os.path.isdir(split_file_path):
        os.mkdir(split_file_path)

    maplist={}
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(split_file_path, f"speech_chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        audio_feature=ferture_extrack(chunk_filename)

        maplist['audio_data'].append(audio_feature)
    return maplist



def feature_extrack(file):
    SAMPLES_TO_CONSIDER = 22050*3

    signal,sr=librosa.load(file)

    if len(signal) >= SAMPLES_TO_CONSIDER:


            # ensure consistency of the length of the signal
            signal = signal[:SAMPLES_TO_CONSIDER]

            # extract MFCC
            MFCCs = librosa.feature.mfcc(signal,sr,n_mfcc=18,n_fft=2048,hop_length=512).T
            #filea.append(MFCCs)
            #label.append(to_categorical(emot,len(df.Emot.unique())))
    #ret_data=padding_n_reshape(filea)

            return MFCCs
