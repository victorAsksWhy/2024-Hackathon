from openai import OpenAI

client = OpenAI()

blacklist = [
    "do",
    "my",
    "homework",
    "write",
    "me",
    "an",
    "a"
    "essay",
    "solve",
    "math",
    "problem",
    "this",
    "math",
    "the",
    "about"
    "what is",
]
question = str(input("Ask me a question: "))
question = question.lower()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a general purpose assistant, that helps answer general questions",
        },
        {"role": "user", "content": f"{question}"},
    ],
)
question = question.split(" ")
# print(question)
x = 0
blacklisted = 0
for y in question:
    if question[int(x)] in blacklist:
        blacklisted += 1

if blacklisted < 1:
    print(completion.choices[0].message.content)
else:
    print(
        "I\'m sorry, I cannot process you request because that command violates our policies." 
    )
    print('However, I can provide an example of your problem.')    
    print('Tell me what you need help with. For example: \'Solving Equations\' or \'Essays\' or \'Physics\'. Alternatively, type EXIT to exit')
    explain = str(input(''))
    if explain.upper() == 'EXIT':
        exit()
    else:
        explainer = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a general purpose assistant, that helps answer general questions",
            },
            {"role": "user", "content": f"Generate a random example of {explain} and explain it."},
        ],
    )
        print(explainer.choices[0].message.content)
        


input('Press enter to exit')
