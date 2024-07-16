# imports
from logging import setLogRecordFactory
import streamlit as st
from openai import OpenAI

# Methods
def generate_story(story_prompt, client):
    story_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": 'system', "content": "You are a bestseller story writer. You will take user's prompt and generate a 100-word short story for adults age 20-30"},
            {"role": 'user', 'content': f'{story_prompt}'}
        ],
        max_tokens=400,
        temperature=0.8
    )

    story = story_response.choices[0].message.content
    return story

def generate_cover_description(story, client):
    design_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": 'system', "content": """
                Based on the story given, you will design a detailed image prompt for the cover of this story.
                The image prompt should include the theme of the story with relevant color, suitable for adults.
                The output should be written within 100 characters.
            """},
            {"role": 'user', 'content': f'{story}'}
        ],
        max_tokens=400,
        temperature=0.8
    )
    design = design_response.choices[0].message.content
    return design

def generate_cover_url(design_description, client):
    cover_response = client.images.generate(
        model='dall-e-2',
        prompt=f"{design_description}",
        size='256x256',
        quality='standard',
        n=1,
    )

    image_url = cover_response.data[0].url
    return image_url

api_key = st.secrets['OPENAI_SECRET']
client = OpenAI(api_key=api_key)

st.markdown(
    """
    <style>
        .main {
            padding: 10px;
        }
        .header {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            font-size: 24px;
            color: #2e3b4e;
            font-weight: italics;
            text-align: center;
        }
        .prompt-label {
            font-size: 18px;
        }
        .divider {
            margin: 20px 0;
        }
        .image-container {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="header">Story Generator</div>', unsafe_allow_html=True)
st.markdown('<em><div class="subheader">Create a short story and its cover</div></em>', unsafe_allow_html=True)

with st.form("story_form"):
    st.markdown('<div class="prompt-label">Enter keywords to generate a story:</div>', unsafe_allow_html=True)
    prompt = st.text_input(label="", placeholder="e.g., mystery, romance, adventure", key="prompt_input")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.balloons()
        story = generate_story(prompt, client)
        cover_description = generate_cover_description(story, client)
        image_url = generate_cover_url(cover_description, client)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image_url)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write(story)
