import textwrap
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pyjokes
import text_information
import os
import random
import glob

class image_creation :

    def calling_all_variables_in_images(self,session_no,session_status):
        self.image_variables(session_no,session_status)
        self.imagecoordiantes()
        self.image_over_lay()


    def image_variables(self,session_no,session_status):

        self.session_no = session_no
        self.session_status = session_status
        self.topics = text_information.text().first_lines()

        # Specify the path to the folder containing PNG images
        folder_path = r'C:\Users\dhana\Pictures\background_images'

        # Get a list of all PNG files in the folder
        self.png_files = glob.glob(folder_path + '/*.png')


    def imagecoordiantes(self):

        self.cordiantes = [[(106,375),(106,428),(106,490),(106,550),(106,680),(40,84)],
                           [(108,302),(108,360),(108,440),(108,500),(108,630),(40,84)],
                           [(95,300),(95,360),(95,430),(95,492),(95,600),(40,84)],
                           [(60,440),(60,505),(60,590),(60,650),(60,770),(40,84)],
                           [(145,370),(145,420),(145,490),(145,540),(145,680),(40,84)],
                           [(340,360),(1051,360)]]

        text_color = (255, 255, 255)

        self.no_track = 0

        for j in range(0,len(self.png_files)):

            self.file = self.png_files[j]

            # Open the image
            image = Image.open(self.file)

            # Convert image to RGB mode
            self.image = image.convert("RGB")

            # Create a drawing object
            self.draw = ImageDraw.Draw(self.image)

            # Get a random joke
            self.joke = pyjokes.get_joke()
            self.date = datetime.now().strftime("%d-%m-%Y")
            self.time = datetime.now().strftime("%H:%M %p")

            self.image_no = j

            for i in range(1, 7):

                try:
                    if i == 1:
                        text = "> Start_the_data_science_session"
                        text_position = (self.cordiantes[self.image_no][0][0],self.cordiantes[self.image_no][0][1])
                        text_color = (255, 255, 255)
                        font = ImageFont.truetype("C:\\Windows\\Fonts\\Fira Code\\FiraCode-Bold.ttf", 40)
                        self.draw.text(text_position, text, font=font, fill=text_color)
                except :
                    print(f'image {i} error')


                try:
                    if i == 2:
                        text = f"O : {self.date}, {self.time}, Session {self.session_no} {self.session_status}"
                        text_position = (self.cordiantes[self.image_no][1][0],self.cordiantes[self.image_no][1][1])
                        text_color = (255, 255, 255)
                        font = ImageFont.truetype("C:\\Windows\\Fonts\\Fira Code\\FiraCode-Light.ttf", 40)
                        self.draw.text(text_position, text, font=font, fill=text_color)
                except:
                    print(f'image {i} error')

                try:
                    if i == 3:
                        text = '> Goal_of_this_Session'
                        text_position = (self.cordiantes[self.image_no][2][0],self.cordiantes[self.image_no][2][1])
                        text_color = (255, 255, 255)
                        font = ImageFont.truetype("C:\\Windows\\Fonts\\Fira Code\\FiraCode-Bold.ttf", 40)
                        self.draw.text(text_position, text, font=font, fill=text_color)
                except:
                    print(f'image {i} error')

                try:
                    if i == 4:
                        text = f'> {self.topics} '
                        text_position = (self.cordiantes[self.image_no][3][0],self.cordiantes[self.image_no][3][1])
                        text_color = (255, 255, 255)
                        font = ImageFont.truetype("C:\\Windows\\Fonts\\Fira Code\\FiraCode-Light.ttf", 40)
                        wrapper = textwrap.TextWrapper(width=40)
                        wrapped_text = wrapper.wrap(text)
                        text = "\n".join(wrapped_text)
                        self.draw.text(text_position, text, font=font, fill=text_color)
                except:
                    print(f'image {i} error')

                try:
                    if i == 5:
                        text = f"pyjokes : {self.joke}"
                        text_position = (self.cordiantes[self.image_no][4][0],self.cordiantes[self.image_no][4][1])
                        font = ImageFont.truetype("C:\\Windows\\Fonts\\Fira Code\\FiraCode-SemiBold.ttf", 40)
                        text_color = (255, 255, 255)
                        wrapper = textwrap.TextWrapper(width=40)
                        wrapped_text = wrapper.wrap(text)
                        text = "\n".join(wrapped_text)
                        self.draw.text(text_position, text, font=font, fill=text_color)
                except:
                    print(f'image {i} error')

                try:
                    if i == 6:
                        text = f"DAY{self.date[0:2]}"
                        text_position = (self.cordiantes[self.image_no][5][0],self.cordiantes[self.image_no][5][1])
                        font = ImageFont.truetype("C:\\Windows\\Fonts\\Fira Code\\FiraCode-SemiBold.ttf", 33)
                        text_color = (0,0,0)
                        wrapper = textwrap.TextWrapper(width=40)
                        wrapped_text = wrapper.wrap(text)
                        text = "\n".join(wrapped_text)
                        self.draw.text(text_position, text, font=font, fill=text_color)

                except:
                    print(f'image {i} error')

            try:

                # Save the modified image as JPEG
                self.image.save(r"C:\Users\dhana\Pictures\full_images" + "\\" + f"image{j}.jpg", "JPEG")

            except:
                print('image save and open erorr')

            #image = Image.open(r"C:\Users\dhana\Pictures\full_images" + "\\" + f"image{j}.jpg")

            # Display the image
            #image.show()

    def image_over_lay(self):
        try:
            print('ok')
            self.newdirectory = r"C:\Users\dhana\Pictures\full_images"

            # Get a list of all PNG files in the folder
            jpg_files = glob.glob(self.newdirectory + '/*.jpg')

            # Specify the path to the folder containing PNG images
            self.folder_path = r'C:\Users\dhana\Pictures\animated_images'

            # Get a list of all PNG files in the folder
            self.png_files = glob.glob(self.folder_path + '/*.png')

            for i in range(5):

                # Randomly select one PNG file
                self.selected_file = random.choice(self.png_files)
                self.selected_file1 = random.choice(self.png_files)

                # Open the background image
                self.background_image = Image.open(jpg_files[i])

                # Open the overlay image
                self.overlay_image = Image.open(self.selected_file)
                self.overlay_image1 = Image.open(self.selected_file1)

                # Adjust the size of the overlay image
                overlay_width, overlay_height = self.overlay_image.size
                new_overlay_width = int(overlay_width * 2)  # Adjust the size as needed
                new_overlay_height = int(overlay_height * 2)  # Adjust the size as needed

                resized_overlay_image = self.overlay_image.resize((new_overlay_width, new_overlay_height))
                resized_overlay_image1 = self.overlay_image1.resize((new_overlay_width, new_overlay_height))

                # Calculate the position to place the overlay image on the background image
                position = (750, 800)  # Adjust the position as needed
                position1 = (50, 800)

                # Paste the overlay image onto the background image
                self.background_image.paste(resized_overlay_image, position, resized_overlay_image)
                self.background_image.paste(resized_overlay_image1, position1, resized_overlay_image1)

                # Save the final image
                self.background_image.save(r"C:\Users\dhana\Pictures\images_for_linked_in_post" + "\\" + f"output_image{i}.jpg")
                print('ok')
        except:
            print('eeror')











