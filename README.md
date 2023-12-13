# Recycle_Bot
Learn how to recycle anything! Upload an image, add a location and personality, and get your response straight from GPT. A valid OpenAI api key is required.

Note: using a .jpg or .png image is recommended. Limited file conversion is implemented, but not all file types are supported.

## Setup
- Setup a virtual environment
  - Run ```python -m venv openai-env``` in the main directory
- After you've created a virtual environment, activate it with one of the following
    - Windows: ```openai-env\Scripts\activate```
    - Mac: ```source openai-env/bin/activate```
- Install dependencies
  - Run ```pip install --upgrade openai Flask requests Werkzeug```
- Run app.py to load Recycle_Bot!
## Recycle_Bot Features
### Basic Functions
- Upload images and receive realtime responses from GPT4
- Adaptive location to tailor instructions to local recycling programs
- Customizable personality with continued accuracy
- Robust hand-crafted prompt, keeping responses concise and helpful (even with absurd or malicious parameters)
- Dynamic prompting template, avoiding hardcoded settings
- Token optimization with vision API

### Quality of Life Additions
- Saves API key and settings for future use
- GUI input for API key
- Support for .jpg and .png images, with limited support for converting other file types
- Popup sidebar menu for settings input

### Security protections
- Simple prompt protection against malicious injection attacks 
- Limited error handling
- Debugging and cost quantification system enabling token and cost tracking (currently unused to avoid cluttering the UI)
