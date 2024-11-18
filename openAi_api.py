from openai import OpenAI

client = OpenAI(
api_key=""
)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "what is today's date?"}
  ]
)

print(completion.choices[0].message.content)
