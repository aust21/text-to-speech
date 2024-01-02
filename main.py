import tts

def run_tts() -> None:
	engine = tts.voice_engine()
	text = tts.read_file("text.txt")
	tts.save_audio(text, engine)
	tts.text_to_speech(text, engine)


if __name__ == "__main__":
	run_tts()