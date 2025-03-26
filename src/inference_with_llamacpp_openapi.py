from openai import OpenAI

#client = OpenAI(api_key="Key", base_url="http://0.0.0.0:1234")
client = OpenAI(api_key="Key", base_url="http://localhost:8000/v1")
while True:
    inputs = input("Enter your message: ")

    if inputs == 'exit':
        break

    completion = client.chat.completions.create(
      model="MateConv",
      messages=[
        {"role": "user", "content": inputs}
      ],
       stream=True
    )
    #print(completion.choices[0].message.content)
    for chunk in completion:
        print(chunk.choices[0].delta.content, end="")
