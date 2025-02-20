import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_diet_plan(preferences):
    prompt = (
        f"Generate a detailed weekly diet plan based on the following preferences and restrictions: {preferences}. "
        "Include breakfast, lunch, dinner, and snack ideas for each day."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional nutritionist."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    preferences = input("Enter your dietary preferences, restrictions, and goals: ")
    diet_plan = generate_diet_plan(preferences)
    print("\nGenerated Weekly Diet Plan:\n", diet_plan)
