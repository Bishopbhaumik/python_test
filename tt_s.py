from gtts import gTTS
import os
myText="I am Bishop Bhaumik.I am a student of kiit university 2019 batch .My roll no is 1928024.What is your name? "
utext="Question.txt"

language= 'en'

output=gTTS(text=myText, lang=language,slow=False)

output.save("ni.mp3")

os.system("start ni.mp3")