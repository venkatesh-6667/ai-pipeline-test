import openai, os, sys

openai.api_key = os.getenv("OPENAI_API_KEY")
file = sys.argv[1]

with open(file, 'r') as f:
    code = f.read()

prompt = f"Fix the following Python code if it has issues and explain what you changed:\n\n{code}"

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print("🔧 AI Suggestion:\n")
print(response.choices[0].message.content)

