from responsive_voice.voices import UKEnglishMale,UKEnglishFemale

text =""" 

"Hey there, fellow automation and data science enthusiasts! Today, I'm thrilled to share an exciting update on my data science journey. After spending 10 hours immersed in Selenium automation, I've also been passionately diving into the vast world of data science. Armed with Python and powerful libraries like Pandas, NumPy, and Scikit-learn, I'm unlocking hidden patterns and extracting meaningful insights from complex datasets. From exploratory data analysis to machine learning models, my data science endeavors are taking off. And here's where automation comes into play. By integrating my newfound automation skills with data science workflows, I'm streamlining repetitive tasks, enhancing data preprocessing, and accelerating model evaluation. Together, automation and data science are revolutionizing the way I tackle projects, empowering me to uncover impactful discoveries efficiently. Join me on this exhilarating journey as I continue to merge the realms of automation and data science, paving the way for groundbreaking advancements and innovation. Subscribe now and be a part of this incredible expedition!"
"""
def text_input(text):

    ukm = UKEnglishMale(0.5, 0.60)
    #ukf = UKEnglishFemale(0.5, 0.63)

    ukm.get_mp3(text, mp3_file='malevoice.mp3')

    #ukf.get_mp3(text, mp3_file='female.mp3')

text_input(text)