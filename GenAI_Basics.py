#Gen AI Basics using Open AI API with valid syntax with basic explanation and examples for a beginner level with explanation of each step
#import the openai library
import openai

#set the api key
openai.api_key = "sk-proj-1234567890"

#generate the response  using the openai  with latest response model
response = openai.responses.create(
    model="gpt-6-astra",
    input="Write a one-sentence bedtime story about a unicorn.",
    prompt="Write a one-sentence bedtime story about a unicorn.",
    max_tokens=100,
    temperature=0.5
)

print(response.output_text)

#How to store api key
store the api key in a file called .env
- create a file called .env
- add the api key to the file
  #example: api_key=sk-proj-1234567890
- load the api key from the .env 

#how to load the api key from the file?
- use the os library to load the api key from the file 

import os
from dotenv import load_dotenv

# 1. Load the variables from your .env file into the system environment
load_dotenv()
# 2. Now os.getenv can successfully find your key
api_key = os.getenv("api_key")
# 3. Print the api key
print(api_key)


#Incase of pushing to github, we need to add the .env file to the .gitignore file
- create a file called .gitignore
- add the .env file to the .gitignore file


load_dotenv() #to load the api key from the .env file
api_key = os.getenv("api_key")
print(api_key)

how is load_dotenv different from os.getenv?
- load_dotenv is used to load the api key from the .env file
- os.getenv is used to load the api key from the environment variables



#import the load_dotenv library
import load_dotenv
#load the api key from the .env file
load_dotenv()
api_key = os.getenv("api_key")
print(api_key)
