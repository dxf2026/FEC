from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import moviepy.editor as mp
import speech_recognition as sr

nltk.download('vader_lexicon')

def toMP3(videof):
    video = mp.VideoFileClip(videof)
    audio = video.audio
    audio.write_audiofile("FileSaving\\sound.wav")

def getSentiment(text):
    nia = SentimentIntensityAnalyzer()
    return nia.polarity_scores(text)

def generate(videof):
    out = "FileSaving\\sound.wav"

    toMP3(videof)
    # engine = tts.init()
    # engine.save_to_file('''We can discuss your product design later. Email me or something. Please do not make any inquiries about your design right now.''', out)
    # engine.runAndWait()

    return(out)


def get(videof):
    engine = sr.Recognizer()
    mp3FileName = generate(videof)
    with sr.AudioFile(mp3FileName) as source:
        audio = engine.record(source)

    text = engine.recognize_google(audio)
    return(getSentiment(text))
