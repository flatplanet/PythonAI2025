from tkinter import *
from openai import OpenAI


# create a root app
root = Tk()
#Add a title
root.title("Codemy.com Chatbot")
# Set the size
root.geometry('500x500')


# Define the system role
def initialize_conversation(system_message):
	return [{"role":"system", "content": system_message}]

# Add Message
def add_message(conversation_history, role, content):
	conversation_history.append({"role":role, "content":content})
	return conversation_history
	


# Define our bot's personality
system_context = (
		"You are an expert Math Tutor. "
		"Provide ccurate answers in a friendly yet perfunctory tone. "
		"End each answer with the phrase 'I Make Maths Fun!'"
		)
# Pass the system Context into history

conversation_history = initialize_conversation(system_context)





def ask(conversation_history):
	# Add Message to the conversation history
	message = add_message(conversation_history, "user", my_entry.get())

	#print(message)
	# Delete whatever is already in the text box
	# my_text.delete("1.0", END)

	# Create an OpenAI Client
	client = OpenAI(api_key="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")

	try:
		response = client.chat.completions.create(
			model="gpt-4o",
			messages=message
		)

		# Get the response
		assistant_response = response.choices[0].message.content
		# Print to text box
		my_text.insert(END, f'({my_entry.get()})')
		my_text.insert(END, "\n")

		my_text.insert(END, assistant_response)
		my_text.insert(END, "\n\n")

		# Delete the entry box
		my_entry.delete(0, END)

		# Add the response to our conversation history
		add_message(conversation_history, "system", assistant_response)

	
	# Upon Error, print message
	except Exception as e:
		my_text.insert(END, f"There was an error. \n {e}")






# Text window
my_text = Text(root, width=60, wrap="word")
my_text.pack(pady=10)

# Entry window for typing the prompt
my_entry = Entry(root, font=("Helvetica", 16), width=40)
my_entry.pack(pady=10)

# Button
my_button = Button(root, text="Ask Chatbot", command=lambda: ask(conversation_history))
my_button.pack()
















# Start the app
root.mainloop()