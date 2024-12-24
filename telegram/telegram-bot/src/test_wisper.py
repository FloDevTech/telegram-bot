import os
import whisper

audio_file='file_name.mp3'
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    # try:
        # Verificar si el archivo de audio existe
        print("")
        print("")
        print("")
        if not os.path.exists(audio_path):
            print(f"Archivo de audio no encontrado: {audio_path}")
            return ''

        # Transcribir el audio
        print("Transcribir el audio")
        print("")
        result = model.transcribe(audio_path, fp16=False)
        text = result['text']

        print("Transcripción completada")
        print(f"Audio transcrito: {audio_path}")
        print(f"Texto: {text}")
        return text
    # except Exception as e:
        print(f"Error al transcribir el audio {audio_path}: {e}")
        return ''
    
audio_file='C:/00_programacion/telegram/telegram-bot/src/file_name.wav'
transcription = transcribe_audio(audio_file)

if transcription:
    text_file_path = os.path.splitext(audio_file)[0] + '_transcription.txt'

    with open(text_file_path, 'w') as file:
        file.write(transcription)

    print(f"Transcripción guardada en: {text_file_path}")
else:
    print("No se pudo transcribir el audio.")