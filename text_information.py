import random
from datetime import datetime
Insert_Session_Topic = input("enter the topic of this session : ").upper()
Insert_Learning_Objective = input("enter the Learning_Objective of this session : ").upper()

class text:

    def call_methods(self,texts,sessions):
        self.first_lines()
        self.text_formater(texts,sessions)

    def first_lines(self):
        self.Insert_Learning_Objective = Insert_Learning_Objective
        self.Insert_Session_Topic = Insert_Session_Topic

        self.start_first_line = ["Embark on this incredible data science journey with me! 🚀💡",
                                 "Ready to dive into today's data science adventure? Join me! 📚🔍",
                                 "Calling all data enthusiasts! Let's reflect on today's exciting study session. 🌟📊",
                                 "Curious about my data science progress? Join me for a daily review! 📈💻",
                                 "Data science explorers unite! Discover the highlights of today's study session. 🌐🔬",
                                 "Unlock the power of data science together! Join me on this learning journey. 💪📚",
                                 "Data science insights await! Let's review today's fascinating discoveries. 🌌💡",
                                 "Ready to level up your data skills? Join me as we conquer new frontiers! 🚀📈",
                                 "Data science enthusiasts, unite! Join me for a daily dose of knowledge and progress. 🌟💻",
                                 "Embrace the data-driven world! Let's review today's step forward in our learning journey. 📊🌍"
                                 ]
        self.end_first_line = [f"{self.Insert_Session_Topic} Session Recap: Reflecting on Today's Learnings 📝🔍,"
                               f"Deep Dive into {self.Insert_Session_Topic}: Insights and Highlights of the Day 🌟💡",
                               f"Unveiling the Secrets of {self.Insert_Session_Topic}: Key Takeaways and Reflections 🚀🔍",
                               f"{self.Insert_Session_Topic} Exploration: Delving into the World of Data Science 🌐🔎",
                               f"Today's Focus: {self.Insert_Session_Topic} Session Recap and Progress Update 📚💡",
                               f"Unlocking the Power of {self.Insert_Session_Topic}: Recap and Lessons Learned 💡✨",
                               f"Reflections on Today's {self.Insert_Session_Topic} Session: Key Concepts and Insights 📝🧠",
                               f"{self.Insert_Session_Topic} Session Highlights: A Journey of Discovery and Growth 🌱🚀",
                               f"Learning Journey Update: Insights from Today's {self.Insert_Session_Topic} Session 💡📚",
                               f"Unraveling the World of {self.Insert_Session_Topic}: Recap and Achievements of the Day 🔍📈"]

        self.daily_review_first_lines = ["Today's Data Science Diary: Unveiling the Learnings and Progress! 📚💡",
                                         "Reflections on My Data Science Expedition: Insights & Milestones! 🚀🔍",
                                         "Journeying through Data Science: Today's Review and Revelations! 📊✨",
                                         "Data Science Chronicles: Daily Reflections and Growth 📖💪",
                                         "Unearthing Data Science Gems: Daily Review and Knowledge Nuggets! 💎🔍",
                                         "Data Science Insights Unleashed: A Daily Review and Analysis 📝🔬",
                                         "Navigating the Data Science Frontier: Daily Reflections and Discoveries! 🌌✨",
                                         "Embracing the Data Science Odyssey: A Daily Review of Learnings and Insights! 🚀💡",
                                         "Data Science Musings: Today's Review and Triumphs! 📚🎉",
                                         "Embarking on a Data Science Adventure: Daily Reflections and Breakthroughs! 🚀🔍"]

    def text_formater(self, text,session):

        self.text = text
        self.session = int(session)
        try:
            if self.text.lower() == "start":

                self.start_post_message = f""" {random.choice(self.start_first_line)}
                
                Session : {self.session} Start
                Session Time: {datetime.today()}
                
                Excited to embark on my data science learning journey! Today's session: {self.Insert_Session_Topic}
                
                Objective: {self.Insert_Learning_Objective}
                
                Looking forward to expanding my knowledge in {self.Insert_Session_Topic} and gaining hands-on experience. Stay tuned for updates on my progress!
    
                #DataScience #LearningJourney #HandsOnExperience
                #DataScience, #MachineLearning, #DataAnalytics, #ArtificialIntelligence, #BigData, #PythonProgramming, #RProgramming, #DataVisualization, #Statistics, #DataMining, #DeepLearning, #Coding, #DataDriven, #AI, #DataAnalysis, #DataScientist, #DataSkills, #STEM, #Technology, #CareerDevelopment, #Learning, #Programming, #TechCommunity, #EducationalContent, #DataScienceJourney, #DataScienceSkills, #TechSkills, #ProblemSolving, #ContinuousLearning, #ProfessionalDevelopment, #CareerGoals
                """
                print(self.start_post_message)
            elif self.text.lower() == 'end':
                self.Key_Takeaway_one = input('enter the key takeaway from this session : ').upper()
                self.Key_Takeaway_two = input('enter the key second takeaway from this session : ').upper()
                self.Key_Takeaway_three = input('enter the key third takeaway from this session : ').upper()

                self.end_post_message = f""" {random.choice(self.end_first_line)}
                
                Session : {self.session} End
                Session Time: {datetime.today()}
                
                Just completed an engaging data science session on {self.Insert_Session_Topic}!
                
                Key Takeaways:
                {self.Key_Takeaway_one}
                {self.Key_Takeaway_two}
                {self.Key_Takeaway_three}
                
                Feeling excited and motivated to apply these insights to real-world projects. Keep following along for more updates on my data science journey! 
                Looking forward to expanding my knowledge in {self.Insert_Session_Topic} and gaining hands-on experience. Stay tuned for updates on my progress!
    
                #DataScience #LearningJourney #HandsOnExperience
                #DataScience, #MachineLearning, #DataAnalytics, #ArtificialIntelligence, #BigData, #PythonProgramming, #RProgramming, #DataVisualization, #Statistics, #DataMining, #DeepLearning, #Coding, #DataDriven, #AI, #DataAnalysis, #DataScientist, #DataSkills, #STEM, #Technology, #CareerDevelopment, #Learning, #Programming, #TechCommunity, #EducationalContent, #DataScienceJourney, #DataScienceSkills, #TechSkills, #ProblemSolving, #ContinuousLearning, #ProfessionalDevelopment, #CareerGoals
                """
                print(self.start_post_message)

            elif self.text.lower() == 'daily' :
                self.Insert_Duration = input('enter the total study duration of today : ')
                self.Progress_Update = input('enter the Progress_Update of today : ')
                self.Challenges_faced = input('enter the Challenges_faced of today : ')
                self.Overall_progress = input('enter the Overall_progress of today : ')

                self.daily_post_message = f""" {random.choice(self.daily_review_first_lines)}
                
                🔍 Today's Study Session: {self.Insert_Session_Topic}
                ⏱️ Study Time: {self.Insert_Duration}
                
                📊 Progress Update:
                {self.Progress_Update}
                
                💡 Challenges & Insights:
                {self.Challenges_faced}
                
                📈 Overall Progress:
                {self.Overall_progress}
                
                🔮 Looking Ahead:
                I'm excited about the opportunities ahead and can't wait to apply what I've learned to real-world projects.
                🤝 Let's Connect
                I'm always eager to connect with fellow data enthusiasts, professionals, and mentors. If you have any insights, recommendations, or want to discuss data science, feel free to reach out! Let's learn and grow together. #DataScience #LearningJourney #ProgressUpdate #CommunityEngagement"
                #DataScience, #LearningJourney, #ProgressUpdate, #DailyReview, #StudySession, #DataScienceCommunity, #DataAnalysis, #MachineLearning, #ArtificialIntelligence, #Coding, #DataVisualization, #HandsOnLearning, #ContinuousLearning, #DataDriven, #ProblemSolving, #SkillsDevelopment, #CareerGrowth, #TechSkills, #DataInsights, #ProfessionalDevelopment, #DataEnthusiast, #DataScientists, #KnowledgeSharing, #Inspiration, #Motivation, #TechCommunity, #DataProjects, #DataSkills, #Analytics, #STEM, #DataMastery
                """

                print(self.daily_post_message)
            else:
                pass
        except Exception as e:
            print(e)