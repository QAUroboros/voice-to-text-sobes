import whisper

model = whisper.load_model("medium")  # можно заменить на "small" или "large"
result = model.transcribe("interview.m4a", language="ru")

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Готово! Результат сохранён в result.txt")
