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

## RecycleBot Features
- Adaptive location
- Customizable personality with high accuracy (even with absurd or malicious inputs)
- GUI input for API key
- Saves API key and settings
- Robust hand-crafted prompt, keeping responses concise and helpful with minimal moderation conflicts
- Dynamic prompting template, avoiding hardcoded settings
- Support for .jpg and .png images
- Token optimization with vision API
- Popup sidebar menu for settings input
- Simple prompt protection against malicious settings
- Limited error handling
- Debugging and cost quantification system enabling token and cost tracking (currently unused to avoid cluttering the UI)
