from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import moviepy.editor as mp
import speech_recognition as sr

nltk.download('vader_lexicon')

def toMP3(videof):
    audio = videof.audio
    audio.write_audiofile("FileSaving\\sound.wav")

def getSentiment(text):
    nia = SentimentIntensityAnalyzer()
    return nia.polarity_scores(text)

def generate(videog):
    out = "FileSaving\\sound.wav"

    toMP3(videog)
    # engine = tts.init()
    # engine.save_to_file('''We can discuss your product design later. Email me or something. Please do not make any inquiries about your design right now.''', out)
    # engine.runAndWait()

    return(out)


def get(vid):
    engine = sr.Recognizer()
    mp3FileName = generate(vid)
    with sr.AudioFile(mp3FileName) as source:
        audio = engine.record(source)

    text = engine.recognize_google(audio)
    return(getSentiment(text))
