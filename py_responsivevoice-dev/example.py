'''from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")
engine.say("hello world",
           gender=ResponsiveVoice.MALE,
           rate=0.45)

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_BR)
file_path = engine.get_mp3("olá mundo")
engine.play_mp3(file_path)

'''
'''from responsive_voice.voices import UKEnglishMale,UKEnglishFemale,USEnglishMale,USEnglishFemale


text = """
"Hey, data enthusiasts! Welcome to day 3 of our 365-day data science challenge. 
In today's session, we dived into the fascinating world of MySQL. 
Our learning objective was to master the art of join commands in MySQL. 
And guess what? We nailed it! We now have a clear understanding of how to combine data from multiple tables using powerful join operations. 
It's simply amazing how join commands can unlock new insights from your databases. 
So, stay tuned for more exciting data adventures in our 365-day challenge. 
Don't forget to hit that subscribe button and join us on this incredible data science journey! Keep learning, keep exploring, and let's conquer the world of data together!"

"""
um = UKEnglishMale(0.5,0.5)
uf = UKEnglishFemale(0.6,0.6)
usm = USEnglishFemale(1,1)
usf = USEnglishMale(0.5,0.7)

um1 = UKEnglishMale(1,0.7)
uf1 = UKEnglishFemale(0.7,0.7)
usm1 = USEnglishFemale(0.8,0.8)
usf1 = USEnglishMale(0.9,0.9)


for i in range(8):
    if i==0 :
        um.get_mp3(text,f'hello{i}.mp3')
    elif i==1:
        uf.get_mp3(text, f'hello{i}.mp3')
    elif i==2:
        usm.get_mp3(text, f'hello{i}.mp3')
    elif i==3:
        usf.get_mp3(text, f'hello{i}.mp3')
    elif i==4:
        um1.get_mp3(text, f'hello{i}.mp3')
    elif i==5:
        uf1.get_mp3(text, f'hello{i}.mp3')
    elif i==6:
        usm1.get_mp3(text, f'hello{i}.mp3')
    elif i==7:
        usf1.get_mp3(text, f'hello{i}.mp3')
    else:
        print(i)'''






from responsive_voice.voices import UKEnglishMale,UKEnglishFemale,USEnglishMale,USEnglishFemale


text = """
"Hey, data enthusiasts! Welcome to day 3 of our 365-day data science challenge. 
In today's session, we dived into the fascinating world of MySQL. 
Our learning objective was to master the art of join commands in MySQL. 
And guess what? We nailed it! We now have a clear understanding of how to combine data from multiple tables using powerful join operations. 
It's simply amazing how join commands can unlock new insights from your databases. 
So, stay tuned for more exciting data adventures in our 365-day challenge. 
Don't forget to hit that subscribe button and join us on this incredible data science journey! Keep learning, keep exploring, and let's conquer the world of data together!"

"""
um = UKEnglishMale(0.5, 0.63)
uf = UKEnglishFemale(0.5, 0.63)
usm = USEnglishFemale(0.5, 0.63)
usf = USEnglishMale(0.5, 0.63)

i=0
while i<4:
    if i == 0:
        um.get_mp3(text, f'hello{i}.mp3')
        um.get_mp3(text, mp3_file=f'hello{i}.mp3')
    elif i == 1:
        uf.get_mp3(text, f'hello{i}.mp3')
        uf.get_mp3(text, mp3_file=f'hello{i}.mp3')

    else:
        print(i)
    i+=1





'''import pygame

def play_audio(file_path):
    pygame.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()

# Usage
audio_file = r'F:\all_pycharm_files\py_responsivevoice-dev\hello.mp3'
play_audio(audio_file)

'''