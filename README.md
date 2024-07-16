# AI Powered Story Generator

Generate a short story based on keywords with an image about the story. Feel free to try it out by pressing this ![link](https://mainpy-fgfdrxnoguzug2vg69strw.streamlit.app/)

## Badges

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white)

## Features

- Generate a 100-word short story based on user input keywords.
- Create a cover image prompt based on the generated story.
- Display the generated story and cover image.

## Prerequisites

To run this project, you need:

- Python 3.7 or higher
- Streamlit
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-story-generator.git
cd ai-story-generator
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key in Streamlit secrets:
- Create a secrets.toml file in the .streamlit directory:

```bash
mkdir -p .streamlit
echo "[secrets]" > .streamlit/secrets.toml
echo "OPENAI_SECRET = 'your_openai_api_key'" >> .streamlit/secrets.toml
```

## Running the App
To run this project locally, use the following command:

```bash
streamlit run app.py
```

