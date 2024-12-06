from openai import OpenAI

# Create an OpenAI Client
client = OpenAI(api_key="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")



response = client.chat.completions.create(
	model="o1-preview",
	messages=[
	{
		"role":"user",
		"content": "Write a 5 line poem about how awesome Python is."
		}
	]
)

print(response.choices[0].message.content)