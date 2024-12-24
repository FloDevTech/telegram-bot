import whisper
model = whisper.load_model("medium")
result = model.transcribe("file_name.mp3")
print(result["text"])
