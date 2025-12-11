import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="TT-BOT")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

if response.usage_metadata is not None:
    print(f"Response: {response.text}")
    if args.verbose:
        print(f"Prompt-Token Count: {response.usage_metadata.prompt_token_count}")
        print(f"Total-Token Count: {response.usage_metadata.total_token_count}")

else:
    RuntimeError("No usage MetadataObject")
