# RecycleBot
Learn how to recycle anything! Upload an image, add a location and personality, and get your response straight from GPT. A valid OpenAI api key is required.

Note: using a .jpg or .png image is recommended. Limited file conversion is implemented, but not all file types are supported.

## Setup
Run the following to install dependencies:
pip install Flask requests Werkzeug

## RecycleBot Features
- Supports custom location
- Customizable personality with high accuracy (even with absurd settings)
- GUI API key input
- Saves settings for future use
- Dynamic prompt template, enabling recycle checks without hardcoded default settings
- Support for .jpg and .png images
- Popup sidebar menu for settings input
- Token optimization with vision API
- Minimal conflicts with GPT moderation
- Limited error handling
- Debugging and cost quantification system enabling token and cost tracking (currently unused to avoid cluttering the UI)
