import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
import ast
import os


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def retrieve_tags(image_path: str) -> dict:

    prompt = """
    Analyze the provided image and describe the key fashion elements. 
    Please categorize the clothing item, identify the primary and secondary colors, 
    and define the style. Provide the information in a structured format: 
    {type: clothing type, primary_color: primary color, secondary_color: secondary color, style: style}
    format string so that ast.literal_eval would easily convert to dictionary
    return only structured string - { .... }"""

    try:
        img = PIL.Image.open(image_path)
        response = model.generate_content([prompt, img])
        output = ast.literal_eval(response.text)
    except:
        output = {
                    'type': 'unknown',
                    'primary_color': 'unknown',
                    'secondary_color': 'unknown',
                    'style': 'unknown'
                 }

    return(output)


def retrieve_response(prompt: str) -> str:

    system_prompt = """
    You are an advanced AI fashion stylist. 
    Generate a concise and fashion conscious response to the user question (question)
    using the following - user provided information (style_info), recent user & model interaction (recent_conversations), 
    Tags describing user uploaded images (image_tags)
    if user only asks about a specific image, you can assume user is referring to the most recent which will be last entry.
    Ask for clarification if unsure of user request.
    Context: 
    """

    try:
        prompt = f"{system_prompt} {str(prompt)}"
        response = model.generate_content(prompt)
        output = response.text
    except:
        output = ""

    return(output)


def style_matching(prompt: dict) -> str:

    system_prompt = """
    You are an advanced AI fashion stylist. You are an expert at 
    analyzing user wardrobe and suggesting match groupings taking into account fashion trends.
    Given a number of tags (image_tags), each representing a description of the user's wardobe items,
    and user provided style preferences (user_style), your job is to generate at most, 5 groups of matches. 
    Each group should only contain one of each category. Multiple items on the list
    must not serve the same function. e.g (do not include two shoes, or two pants to the same group, 
    or a dress, and a shirt in the same group). The goal is to provide recommendations with each group representing 
    stylistic matches of what the user should wear.
    You will return a structured list of lists, each list contain a matched group,
    and in each group will only be the filenames of the items.
    Only the actual filenames will suffice. You can exclude the path.
    Output format example: [["shirt001.png", "shoe000.png"], ["Dress1.png", "shoe111.png", "bag000.png"]]
    Return only the list. Nothing else [[...], [...]]

    """

    try:
        prompt = f"{system_prompt} {str(prompt)}"
        response = model.generate_content(prompt)
        output = response.text
        #output = ast.literal_eval(response.text)
    except:
        output = ''

    return(output)