import whisper
import torch
from tqdm import tqdm
import librosa
import time


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"The current device torch is running on is: {device}")

audio = "testaudio.wav" # use your audio
#duration_audio = round((librosa.get_duration(filename=audio) // 60), 2)
#print(f"The duration of the audio is: {duration_audio}")

def whisper_transcribe(path_to_audio):
    model = whisper.load_model("small.en")
    result = model.transcribe(audio = path_to_audio) 
    print(f"Transcribing your speech...")
    transcription = result['text']
    return transcription

start_time = time.time()
print(f"{whisper_transcribe(audio)}")
end_time = time.time()

print(f"Time taken for the execution: {round((end_time - start_time), 2)} seconds.")
