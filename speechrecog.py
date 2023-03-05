from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import moviepy.editor as mp
import speech_recognition as sr

nltk.download('vader_lexicon')

def toMP3():
    video = mp.VideoFileClip("FileSaving\\test.mp4")
    audio.write_audiofile("FileSaving\\sound.wav")

def getSentiment(text):
    nia = SentimentIntensityAnalyzer()
    return nia.polarity_scores(text)

def generate():
    out = "FileSaving\\sound.wav"

    toMP3()
    # engine = tts.init()
    # engine.save_to_file('''We can discuss your product design later. Email me or something. Please do not make any inquiries about your design right now.''', out)
    # engine.runAndWait()

    return(out)


def get():
    engine = sr.Recognizer()
    mp3FileName = generate()
    with sr.AudioFile(mp3FileName) as source:
        audio = engine.record(source)

    text = engine.recognize_google(audio)
    return(getSentiment(text))
