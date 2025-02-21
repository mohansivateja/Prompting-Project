# -*- coding: utf-8 -*-
"""Reelon Technology 2.0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19zciDEwee3TmlWNRqRc7dxY2rdq0gUve
"""

!pip install google-generativeai

import google.generativeai as genai

genai.configure(api_key="AIzaSyCE2De6RE2nHAKA5wRVCLNgMpLSo-bBg9w")

for m in genai.list_models():
  print(m.name)

!pip install --upgrade google-generativeai

import google.generativeai as genai
print(genai.__version__)

from google import genai

client = genai.Client(api_key="AIzaSyCE2De6RE2nHAKA5wRVCLNgMpLSo-bBg9w")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="what is the whatsup feature",
)

print(response.text)

"""# **Text Summarization**"""

def summarize_text(text_to_summarize):
    """Summarizes the given text using the Gemini API."""
    try:
        client = genai.Client(api_key="AIzaSyCE2De6RE2nHAKA5wRVCLNgMpLSo-bBg9w")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Summarize the following text:\n{text_to_summarize}",
        )

        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
text = """
Knowing how to write a paragraph is incredibly important.
It’s a basic aspect of writing, and it is something that everyone should know how to do.
There is a specific structure that you have to follow when you’re writing a paragraph.
This structure helps make it easier for the reader to understand what is going on.
Through writing good paragraphs, a person can communicate a lot better through their writing.
When you want to write a paragraph, most of the time you should start off by coming up with an idea.
After you have your idea or topic, you can start thinking about different things you can do to expand upon that idea.
You should only finish the paragraph when you’ve finished covering everything you want about that idea.
"""

summary = summarize_text(text)

if summary:
    print("Summary:\n", summary)

"""# **Podcast Script Generation**"""

!pip install google-generativeai

import google.generativeai as genai

genai.configure(api_key="AIzaSyCE2De6RE2nHAKA5wRVCLNgMpLSo-bBg9w")

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_podcast_script(topic):
    prompt = f"Generate a detailed podcast script about '{topic}'. Include an introduction, main discussion points, expert insights, and a conclusion."
    response = model.generate_content(prompt)
    return response.text

# Example usage
if __name__ == "__main__":
    topic = input("Enter the podcast topic: ")
    script = generate_podcast_script(topic)
    print("\nGenerated Podcast Script:\n")
    print(script)



"""# **Content Moderation System Development**"""

!pip install --upgrade google-generativeai
import google.generativeai as genai
from google.generativeai import models

def moderate_content(content_type, content):
    """
    Classifies user-generated content based on various factors.

    Args:
        content_type: The type of content ("text", "image", or "video").
        content: The actual content.

    Returns:
        A dictionary containing the moderation result and scores.
    """
    try:
        toxicity_score = detect_toxicity(content_type, content)
        spam_score = detect_spam(content_type, content)
        inappropriate_score = score_content(content_type, content)

        overall_score = (toxicity_score + spam_score + inappropriate_score) / 3

        if overall_score <= 25:
            return {"result": "Allow", "toxicity": toxicity_score, "spam": spam_score, "inappropriate": inappropriate_score, "overall": overall_score}
        elif 25 < overall_score <= 60:
            return {"result": "Flag for Review", "toxicity": toxicity_score, "spam": spam_score, "inappropriate": inappropriate_score, "overall": overall_score}
        else:
            return {"result": "Block", "toxicity": toxicity_score, "spam": spam_score, "inappropriate": inappropriate_score, "overall": overall_score}
    except Exception as e:
        print(f"An error occurred during content moderation: {e}")
        return {"result": "Flag for Review", "error": str(e)}


# Example usage (assuming the functions from previous responses are defined)

text_content = "This is a sample text. It maintains a professional tone and avoids any inappropriate language or misleading offers."
moderation_result_text = moderate_content("text", text_content)
print(f"Text Moderation Result: {moderation_result_text}")

image_content = "/content/YOLO_image02.jpg"
moderation_result_image = moderate_content("image", image_content)
print(f"Image Moderation Result: {moderation_result_image}")


video_content = "/content/8327786-uhd_3840_2160_25fps.mp4"
moderation_result_video = moderate_content("video", video_content)
print(f"Video Moderation Result: {moderation_result_video}")

"""# **Workflow Automation & AI Optimization**"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyCE2De6RE2nHAKA5wRVCLNgMpLSo-bBg9w")

def call_genai(prompt, model="gemini-2.0-flash"):
    """Generate AI response based on the prompt."""
    try:
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 🚀 Example Usage
prompts = [
    "How does AI contribute to personalized medicine?",
    "List the ethical challenges in using AI for decision-making.",
    "Explain how AI can optimize supply chain management."
]

responses = [call_genai(prompt) for prompt in prompts]

for p, r in zip(prompts, responses):
    print(f"\nPrompt: {p}\nResponse: {r}")











