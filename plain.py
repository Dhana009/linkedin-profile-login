import topics
import time_tracker
import table_plan
import image_creation
import selenium_linked_in
import audio_file
import text_information
import random
import glob
import os

today_session_no = int(input('enter the session no : '))
number_for_start_end = int(input("enter 0 for start, 1 for end, 2 for daily : "))
start_end_daily_variable = ['start','end','daily']
tell_you_session_start_or_end = start_end_daily_variable[number_for_start_end]

class everything_in_one:

    def calling_all_variables(self):
        self.linkedin_post_text = text_information.text()
        self.linkedin_post_text.call_methods(tell_you_session_start_or_end,today_session_no)
        self.image_path_linked_in()
        self.linkedin_and_text_and_post_method()

    def audiofile(self):
        try:
            self.audiofile_text = input('enter the script for the audio part :')
            audio_file.text_input(self.audiofile_text)
        except :
            print('audio file error')

    def image_path_linked_in(self):
        self.images = image_creation.image_creation()
        self.images.calling_all_variables_in_images(today_session_no,tell_you_session_start_or_end)


    def linkedin_and_text_and_post_method(self):

        self.linkedin = selenium_linked_in.linked_in()

        self.linkedin_post_text.call_methods(tell_you_session_start_or_end,today_session_no)

        self.path_for_images = r"C:\Users\dhana\Pictures\images_for_linked_in_post"
        # Get a list of all PNG files in the folder
        self.jpg_files = glob.glob(self.path_for_images + '/*.jpg')
        self.selected_image_for_post = random.choice(self.jpg_files)

        try:
            if number_for_start_end == 0:
                start_text = self.linkedin_post_text.start_post_message
                self.start = self.linkedin.call_allvariables(start_text, self.selected_image_for_post)
            elif number_for_start_end == 1:
                end_text = self.linkedin_post_text.end_post_message
                self.end = self.linkedin.call_allvariables(end_text, self.selected_image_for_post)
            elif number_for_start_end == 2:
                daily_text = self.linkedin_post_text.daily_post_message
                self.daily = self.linkedin.call_allvariables(daily_text, self.selected_image_for_post)
            else:
                print('error enter 0 for start, 1 for end, 2 for daily :  ')
        except:
            print('numbers_start_end failure ')














