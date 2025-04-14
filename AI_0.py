import os
from openai import OpenAI

#  ----- Directions to obtain the API key: -----
# 1. Visit the OpenAI API website: https://platform.openai.com/
# 2. Log in to the website. You can find the login button in the top-right corner. Make sure to log into the API section.
# 3. Navigate to Dashboard → API Keys, or access this link directly.
# 4. Click on the green button "+ Create new secret key".
# 5. A window will appear where you can assign a name to your key (e.g., "MyFirstKey"). Keep the default values for the other fields and click "Create secret key".
# 6. A new window will display your API key. Click the green "Copy" button to save it. This is the only time you will be able to see it. If you forget to copy it, you will need to create a new one.

# ----- Set up your billing information: -----
# 1. On the same page, click "Add to credit balance".
# 2. Do not enable auto-recharge.
# 3. To avoid unexpected charges, set up budget alerts and limits:
#    Go to Usage Limits. Scroll down to "Set up budget alerts".
#.   Set the alert threshold to $40 and the usage cap to $50.
#    Click "Save" to apply the new settings.


# This is a simple script to test the OpenAI API.
api_key = os.getenv('OPENAI_API_KEY')
# If the API key is not set, raise an error.
if api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Check if we established a connection to the OpenAI API:


# Create the client object, which will be used to make the requests.
client = OpenAI()
# This will send a request to the model gpt-3.5-turbo-16k
completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        # This is the prompt. It will tell the LLM the context of our query.
        {"role": "system", "content": "You are an orchid lover with extensive knowledge of Data Analytics"},
        {
            "role": "user",
            # This is our query.
            "content": "Write a hymn about orchids."
        }
    ]
)

print(completion.choices[0].message.content)