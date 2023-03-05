from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import moviepy.editor as mp
nltk.download('vader_lexicon')

def toMp3(mp4inp, mp3dest):
    video = mp.VideoFileClip("C:\\Users\\dxf20\\PycharmProjects\\HackTJ\\FileSaving\\video.mp4")
    audio = video.audio
    audio.write_audiofile("C:\\Users\\dxf20\\PycharmProjects\\HackTJ\\FileSaving\\sound.mp3")

def getSentiment(text):
    nia = SentimentIntensityAnalyzer()
    return nia.polarity_scores(text)

# def main():
#     inp = "C:\\Users\\dxf20\\PycharmProjects\\HackTJ\\FileSaving\\video.mp4"
#     out = "C:\\Users\\dxf20\\PycharmProjects\\HackTJ\\FileSaving\\sound.mp4"

#     toMp3(inp, out)

# if __name__ == "__main__":
#     main()
