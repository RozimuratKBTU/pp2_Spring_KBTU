import openai

openai.api_key = "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"

while True:
    model_engine = 'text-davinci-003'
    prompt = input('Enter your question: ')

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1000,
        n=1, stop =None,
        temperature = 0.5
    )

    if "exit" in prompt or "quit" in prompt:
        break

    response = completion.choices[0].text
    print(response)



