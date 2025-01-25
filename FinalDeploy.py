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
try:
        client.flow.deploy(flow)  # Exit loop if successful
        print("Deployed succesffuly")                             # Deploy to platform
except FlowError as e:
    print(f"Error occurred: {str(e)}")                      # Handle deployment error
