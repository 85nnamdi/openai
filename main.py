import os
import openai
openai.api_key = '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' # os.getenv('OPENAI_API_KEY')

# prompt = """
# Decide whether a Tweet's sentiment is positive, neutral, or negative.

# Tweet: I didn't like the new Batman movie!
# Sentiment:
# """

# response = openai.Completion.create(
#               model="text-davinci-003",
#               prompt=prompt,
#               max_tokens=100,
#               temperature=0
#             )

# print(response)

# ##############
# import openai

response = openai.Image.create(
  prompt="A fluffy white cat with yellow eyes sitting on a truck of tree logs, looking up adorably at the camera",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)