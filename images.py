from openai import OpenAI
import os
from PIL import Image
import requests
from io import BytesIO

# Clear the screen
os.system("clear")


# Create an OpenAI Client
client = OpenAI(api_key="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")


# Save the file
def get_image(our_url):
	# ask for filename
	file_name = input("Enter a File Name (must end in .png): ")
	# Error handling for png
	if file_name.endswith(".png"):
		# dog.png to images/dog.png
		file_name = f'images/{file_name}'
	else:
		# They forgot the .png, let's add it for them
		file_name = f'images/{file_name}.png'

	# Download the image
	downloaded_image = requests.get(our_url)

	# Get the image data
	img_data = downloaded_image.content

	# Save the image
	try:
		# Open and save the file
		Image.open(BytesIO(img_data)).save(file_name)
		print("Image Saved")
		# Open the image in users computers default image program
		img = Image.open(file_name)
		img.show()

	except:
		print("There was a problem saving the file...")



def ask(question):
	if question == "q":
		quit()
	else:
		response = client.images.generate(
			model="dall-e-3",
			prompt=question,
			n=1,
			# 1024x1024, 1792x1024, or 1024x1792
			size="1024x1024",
			style="natural", #vivid or natural
			)

		# Return the results
		return response.data[0].url

# Prompt the user
while True:
	question = input("Describe the image to create (q to quit): ")
	# Get image URL from model
	our_url = ask(question)
	#print(f"\n{ask(question)}\n")

	# Ask to save file 
	saver = input("Save File? (y/n): ")

	# Save logic
	if saver.lower() == "y":
		#save the file 
		get_image(our_url)

	else:
		print("Shutting down...")
		quit()