from django.shortcuts import render
from openai import OpenAI



# Create homepage view
def home(request):
	if request.POST:
		prompt = request.POST['prompt']
		history = request.POST['history']

		# Create history list
		conversation_history = []
		if history:
			for line in history.splitlines():
				role, content = line.split(":", 1)
				conversation_history.append({"role":role, "content":content.strip()})
		
		if prompt:
			conversation_history.append({"role":"user", "content":prompt})


		######### Do AI stuff  ##########
		# Create an OpenAI Client
		client = OpenAI(api_key="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")

		try:
			response = client.chat.completions.create(
				model="gpt-4o",
				messages=[
				{
					"role":"system",
					"content": "You are a cheery math tutor who answers precisely and ends each answer with the phrase 'bully bully!'"
					}
				]  + conversation_history
			)

			# Get the answer from openai
			answer = response.choices[0].message.content
			# Add answer to conversation history
			conversation_history.append({"role":"system", "content":answer})

		
		# Upon Error, print message
		except Exception as e:
			answer = f"There was an error. \n {e}"

		# Convert our conversation_history to a string from a list and dictionary
		history = "\n".join(
			f"{item['role']}:{item['content']}" for item in conversation_history
			)
	
		return render(request, 'home.html', {"prompt":prompt, "answer":answer, "history":history})

	else:
		return render(request, 'home.html', {})