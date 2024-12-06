from openai import OpenAI
import os

# Clear the screen
os.system("clear")


# Create an OpenAI Client
client = OpenAI(api_key="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")


# Define the system role
def initialize_conversation(system_message):
	return [{"role":"system", "content": system_message}]

# Add Message
def add_message(messages, role, content):
	messages.append({"role":role, "content":content})



# Pick our models
def pick_model():
	# List our models
	models = ["o1-preview", "o1-mini", "gpt-4o", "gpt-4o-mini"]
	# Clear the screen
	os.system("clear")

	print("--- Model Menu ---")
	print("1. o1 Preview")
	print("2. o1 Mini")
	print("3. GPT4o")
	print("4. GPT4o Mini")

	while True:
		# Prompt the user
		model = input("Choose Model (1-4): ")
		# Logic for user input
		if model == "1":
			model = models[0]
			break

		elif model == "2":
			model = models[1]
			break

		elif model == "3":
			model = models[2]
			break

		elif model == "4":
			model = models[3]
			break
		else:
			print("Error: Please select a number between 1-4: ")
	# Return the model selected
	return model


def ask_gpt(model, messages):
	# Deal with Quitting
	# Error Handling
	try:
		response = client.chat.completions.create(
			model=model,
			messages=messages
		)

		return (response.choices[0].message.content)
	
	# Upon Error, print message
	except Exception as e:
		return f"There was an error. \n {e}"

def ask_o1(question, model_selection):
	# Error Handling
	try:
		response = client.chat.completions.create(
			model=model_selection,
			messages=[
			{
				"role":"user",
				"content": question
				}
			]
		)

		return (response.choices[0].message.content)
	
	# Upon Error, print message
	except Exception as e:
		return f"There was an error. \n {e}"



def main():
	system_context = (
		"You are an expert Math Tutor. "
		"Provide ccurate answers in a friendly yet perfunctory tone. "
		"End each answer with the phrase 'I Make Maths Fun!'"
		)
	# Pass the system Context into history
	conversation_history = initialize_conversation(system_context)

	# Pick our Model
	model = pick_model()

	# Prompt the user
	while True:
		# Clear the screen
		os.system("clear")
		'''
		print("--- Model Menu ---")
		print("1. o1 Preview")
		print("2. o1 Mini")
		print("3. GPT4o")
		print("4. GPT4o Mini")
		# Prompt the user
		model = input("Choose Model (1-4): ")
		# Logic for user input
		if model == "1":
			model = models[0]
		elif model == "2":
			model = models[1]
		elif model == "3":
			model = models[2]
		elif model == "4":
			model = models[3]
		else:
			model = input("Error: Please select a number between 1-4: ")
		'''

		# Prompt User for text completion
		question = input(f"{model}: Ask Chatbot Something (q to quit): ")
		# Add quit stuff
		if question.lower() in {"q", "quit"}:
			print("Ending Conversation. Goodbye!")
			break
		
		# Query Openai - Logic for model selection
		if model == "gpt-4o" or model == "gpt-4o-mini":
			# Add user message to the converation
			# messages, role, content
			add_message(conversation_history, "user", question)
			
			# Query the model and get a reponse
			assistant_response = ask_gpt(model, conversation_history)
			# Print response to screen
			print(f"{model}: {assistant_response}")

			# Add response message to the conversation history
			add_message(conversation_history, "system", assistant_response)



			#print(f"\n{ask_gpt(question, model)}\n")
		else:
			print(f"\n{ask_o1(question, model)}\n")



# Run the program
main()