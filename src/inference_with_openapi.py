from openai import OpenAI

client = OpenAI(api_key="Key", base_url="http://127.0.0.1:8000/v1")
while True:
    inputs = input("Enter your message: ")

    if inputs == 'exit':
        break

    completion = client.chat.completions.create(
      model="MateConv",
      messages=[
        {"role": "user", "content": inputs}
      ]
    )
    print(completion.choices[0].message.content)
