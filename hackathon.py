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
    "about",
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
        "Im sorry, I cannot process you request because that command violates our policies"
    )
