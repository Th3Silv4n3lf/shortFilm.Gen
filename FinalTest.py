from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("MIRA_API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

# Basic test
flow = CompoundFlow(source=r"shortFilmGen.yaml")  # Load flow configuration
input_dict = {"genre": "Suspense Action", "cinematographer": "Quentin Tarantino", "story_type": "KGF, Bahubali"}  # Prepare test input

#Exception Handling
try:
    response = client.flow.test(flow, input_dict)  # Test entire pipeline
    print("Test response:", response)
    
    # Save the response to a file
    with open("response_output.txt", "w") as file:
        file.write(str(response))
except FlowError as e:
    print("Test failed:", str(e))
