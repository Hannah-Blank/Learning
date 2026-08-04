from openai import OpenAI

client = OpenAI()

user_prompt = input("Enter your prompt: ")
system_prompt = "Limit your answer to one sentence."

response = client.responses.create(
    input =user_prompt,
    instructions = system_prompt,
    model = "gpt-5"
)

print(response.output_text)