# RecycleBot
Learn how to recycle anything! Upload an image, add a location and personality, and get your response straight from GPT. A valid OpenAI api key is required.

Note: using a .jpg or .png image is recommended. Limited file conversion is implemented, but not all file types are supported.

## Setup
- Setup a virtual environment
  - Run '''python -m venv openai-env''' in the main directory
- Run the following to install dependencies:
  - pip install Flask requests Werkzeug
- Run app.py

## RecycleBot Features
- Custom location
- Customizable personality with high accuracy (even with absurd or malicious inputs)
- GUI API key input
- Saves API key and settings
- Robust hand-crafted prompt, keeping responses concise and helpful with minimal moderation conflicts
- Dynamic prompting template, avoiding hardcoded settings
- Support for .jpg and .png images
- Token optimization with vision API
- Popup sidebar menu for settings input
- Simple prompt protection against malicious settings
- Limited error handling
- Debugging and cost quantification system enabling token and cost tracking (currently unused to avoid cluttering the UI)
