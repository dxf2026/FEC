from moviepy.editor import *
import speech_recognition as sr

video = VideoFileClip("example.mp4")
video.audio.write_audiofile("example.mp3")
r = sr.Recognizer()

audio_file = sr.AudioFile('example.mp3')

with audio_file as source:

audio = r.record(source)

text = r.recognize_google(audio)

print(text)
