import key
import base64
import requests
import re
import json
import defaults

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def numTokens(response):
    # Check if the response has 'usage' key
    if 'usage' in response:
        # Extracting prompt_tokens and completion_tokens
        prompt_tokens = response['usage']['prompt_tokens']
        completion_tokens = response['usage']['completion_tokens']
        total_tokens = prompt_tokens+completion_tokens
    else:
        # Default values if 'usage' key is not present
        prompt_tokens, completion_tokens, total_tokens = -1, -1, -2

    return prompt_tokens, completion_tokens, total_tokens

def getCost(prompt_tokens, completion_tokens):
    return (prompt_tokens*0.01/1000) + (completion_tokens*0.03/1000)

# Gets recycling info 
def query_recycling_info(image_path, town, state, object=defaults.getDefaultObject(), personality=defaults.getDefaultPersonality()):
    
    # Final check to force default on empty strings
    if(object==''):
        object = defaults.getDefaultObject()
    if(personality==''):
        personality = defaults.getDefaultPersonality()  
    
    print('Loading...')
    print(personality)
    # OpenAI API Key
    api_key = key.getKey()

    # Combine town and state
    if(town != '' and state !=''):
        combinedLocation = ' in ' + town + ',' + state
    else:
        combinedLocation=''

    # Getting the base64 string
    base64_image = encode_image(image_path)

    # Setup headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Setup payload
    payload = {
        #Allows image uploads
        "model": defaults.getDefaultModel(), 
        
        #Prompt
        "messages": [
            {
                # Most of the prompt is included here because GPT4 tends to adhere to answer format (which includes personality) better in the dedicated system role, rather than the user prompt
                "role": "system", "content": "You are a helpful local waste management director" + combinedLocation + " helping others decide if their object is recyclable. Phrase your recycling instructions in the style of " + personality + " while maintaining complete accuracy.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Is this " + object + " recyclable" + combinedLocation + "? All answers must be in this format: [Yes/No][object name][How to do this]. Example 1: [Yes][paper][Just toss it into your recycling bin!]. Example 2: [Yes, but...][phone][Don't throw it in the bin! You can recycle this by bringing it to your nearest recycling center!]. Example 3: [No][styrofoam container][No need to recycle. Just toss it in the trash!].",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            
                            #Compresses image to optimize token usage
                            "detail":"low"
                        }
                    }
                ]
            }
        ],
        #Hard cap on token usage (near impossible to reach). About $0.01 - $0.03
        "max_tokens": 1000
    }

    # Send request
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Process response
    if response.status_code == 200:
        raw_response = response.json()
        return raw_response

    else:
        print(str(response))
        return "Error code 11: Error in API call"
    
# Parses through to find brackets. Expects [answer][object][details]
def separate_answer_and_details(combined_response):
    print(combined_response)
    
    textResponse = str(combined_response)
    
    if("Error code" in textResponse):
        return str(textResponse), "this", "This is probably because you took a photo of something the program didn't expect."
    
    # Find the positions of the brackets
    first_open_bracket = textResponse.find('[')
    first_close_bracket = textResponse.find(']', first_open_bracket + 1)
    second_open_bracket = textResponse.find('[', first_close_bracket + 1)
    second_close_bracket = textResponse.find(']', second_open_bracket + 1)
    third_open_bracket = textResponse.find('[', second_close_bracket + 1)
    third_close_bracket = textResponse.find(']', third_open_bracket + 1)

    # Extract the personality and prompt
    answer = textResponse[first_open_bracket+1:first_close_bracket]
    object = textResponse[second_open_bracket+1:second_close_bracket]
    details = textResponse[third_open_bracket+1:third_close_bracket]

    return answer, object, details

def extract_message(json_response):
    # Navigate through the JSON structure to extract the message content
    # Assuming 'json_response' is the JSON object you provided
    if 'choices' in json_response and json_response['choices']:
        first_choice = json_response['choices'][0]
        if 'message' in first_choice and 'content' in first_choice['message']:
            return first_choice['message']['content']
        else:
            return "Error code 21: Message content not found"
    else:
        return "Error code 22: Choices not found in response"
