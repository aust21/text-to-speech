import pyttsx3

def voice_engine():
	engine = pyttsx3.init()
	set_properties(engine)
	return engine


def set_properties(engine) -> None:
	engine.setProperty("rate", 150)
	engine.setProperty("voice", 
		"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")


def read_file(file) -> list:
	try:
		with open(file) as fl:
			return fl.readlines()
	except FileNotFoundError:
		print("File does not exist.")


def save_audio(file, engine) -> None:
	file_text = ' '.join(''.join(file).split("\n"))
	engine.save_to_file(file_text, "audio_file.mp3")

def text_to_speech(file, engine) -> None:
	for line in file:
		engine.say(line)
		engine.runAndWait()
