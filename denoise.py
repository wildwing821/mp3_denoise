import os,pathlib
from pydub import AudioSegment
import noisereduce as nr
import numpy as np
from scipy.io import wavfile

dirpath = pathlib.Path(__file__).parent.resolve()
os.chdir(dirpath)



def read_mp3(file_path):
    audio = AudioSegment.from_mp3(file_path)
    return audio 


def remove_noise(audio):
    samples = np.array(audio.get_array_of_samples())
    sample_rate = audio.frame_rate
    reduced_noise = nr.reduce_noise(y=samples, sr=sample_rate, prop_decrease=1.0)
    cleaned_audio = AudioSegment(reduced_noise.tobytes(), frame_rate=sample_rate, sample_width=audio.sample_width, channels=audio.channels)
    return cleaned_audio


def trim_audio(audio, start_time, end_time):
    start_time = start_time * 1000  # convert to milliseconds
    end_time = end_time * 1000  # convert to milliseconds
    trimmed_audio = audio[start_time:end_time]
    return trimmed_audio


def save_audio(audio, output_path):
    audio.export(output_path, format="mp3")

def main():
    input_file_path = "input.mp3"
    output_file_path = "output.mp3"
    start_time = 6  # in seconds
    end_time = 20  # in seconds

    audio = read_mp3(input_file_path)
    cleaned_audio = remove_noise(audio)
    trimmed_audio = trim_audio(cleaned_audio, start_time, end_time)
    save_audio(trimmed_audio, output_file_path)

if __name__ == "__main__":
    main()
    