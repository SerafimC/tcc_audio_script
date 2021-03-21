import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from pydub import AudioSegment
from IPython.display import Audio
from numpy.fft import fft, ifft
import data_prep as data_proc

subject_id = 11

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms / 1000

def base_audio(subject_id):
    '''
    return array data, frequency, pydub.AudioSegment  
    '''

    Fs, data = read('./'+str(subject_id)+'.wav')
    print('Sampling Frequency is', Fs)
    print('Minutes =', len(data) / Fs / 60)
    channel1 = data
    sound = AudioSegment(
        channel1.tobytes(),
        frame_rate = Fs,
        sample_width=channel1.dtype.itemsize,
        channels=1
    )

    return data, Fs, AudioSegment(
        data.tobytes(),
        frame_rate = Fs,
        sample_width=data.dtype.itemsize,
        channels=1
    )

def remove_silence(data, Fs):
    '''
    returns timestamp of start and beggining without silence
    '''
    trim_sound = AudioSegment(
        data.tobytes(),
        frame_rate = Fs,
        sample_width=data.dtype.itemsize,
        channels=1
    )

    start_trim = detect_leading_silence(trim_sound, -50)
    end_trim = detect_leading_silence(trim_sound.reverse(), -55)

    return start_trim, end_trim

def trim_samples(data, Fs, subject_id):
    i = 1
    timestamps_subject = data_proc.main(subject_id)

    for sample in timestamps_subject:

        start = sample[0]
        end = sample[1]

        index1 = int((start - 0.3) * Fs)
        index2 = int((end - 0.0) * Fs)

        sample_data = data[index1:index2]

        s1, s2 = remove_silence(sample_data, Fs)

        start_trim = int(s1 * Fs)
        end_trim = int(len(sample_data) - (s2 * Fs))

        write('.\subject'+str(subject_id) + "\sub" + str(subject_id) + '_sample'+str(i)+'.wav', Fs, sample_data[start_trim:end_trim])
        i += 1


data, Fs, audio = base_audio(subject_id)
trim_samples(data, Fs, subject_id)


# # # Audio(data, rate=Fs)

# # Plot the wave
# # plt.figure()
# # plt.plot(sample1)
# # # plt.plot(sample1)
# # plt.xlabel('Sample index')
# # plt.ylabel('Amplitude')
# # plt.title('Waveform')
# # plt.show()