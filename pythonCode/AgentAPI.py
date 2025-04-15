import requests
from typing import List

API_URL = "http://localhost:3000/api/v1/prediction/29e2db45-5c86-4de5-bf46-e498b0e6e5eb"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

output = query({
    "question": "Generate a prompt for generating the code from input high level requirements",
})

if "text" in output:  # Check if the key 'text' exists in the response
    print(output["text"])  # Print the value of the 'text' key
else:
    print("Key 'text' not found in the response:", output)

class Supervisor:
    def __init__(self, name: str, prompt: str, summarization: bool = False, recursion_limit: int = 100):
        self.name = name
        self.prompt = prompt
        self.summarization = summarization
        self.recursion_limit = recursion_limit

class Worker:
    def __init__(self, name: str, prompt: str, tools: List[str] = None, max_iterations: int = None):
        self.name = name
        self.prompt = prompt
        self.tools = tools or []
        self.max_iterations = max_iterations

class Serper:
    def __init__(self, credential: str):
        self.credential = credential

class ChatOpenAI:
    def __init__(self, model_name: str, temperature: float = 0.9):
        self.model_name = model_name
        self.temperature = temperature

# Instantiate components
chat_openai = ChatOpenAI(model_name="gpt-4o", temperature=0.9)
serper = Serper(credential="serperApi")

supervisor = Supervisor(
    name="Supervisor",
    prompt="You are a supervisor tasked with managing a conversation between the following workers: {team_members}.\nGiven the following user request, respond with the worker to act next.\nEach worker will perform a task and respond with their results and status.\nWhen finished, respond with FINISH.\nSelect strategically to minimize the number of steps taken.",
    summarization=False,
    recursion_limit=100
)

worker_0 = Worker(
    name="Profile Researcher",
    prompt="Your role is to conduct comprehensive online searches to gather detailed information about individuals. Using the Serper API tool, you will perform searches across various platforms such as LinkedIn, X, Orkut, Facebook, and others to compile a profile of the person in question. Your focus is on collecting accurate and relevant data regarding their background, education, interests, and current projects. Your goal is to create a detailed profile that can be used for further processing. Conduct a thorough search for person_name, gathering information on their professional background, educational history, personal interests, and any current projects they are involved in. Use only verified and publicly available information from reliable sources. Avoid making assumptions and ensure that the data is accurate and up-to-date. Produce a comprehensive report on person_name, highlighting their career trajectory, educational qualifications, personal interests, and ongoing projects. Pass the information to the CV Creator.",
    tools=[serper],
    max_iterations=None
)

worker_1 = Worker(
    name="CV Creator",
    prompt="u are responsible for transforming detailed personal profiles into professionally formatted CVs. Using the information provided by the Profile Researcher, you will create a comprehensive and polished CV in MS Word format. Your role is crucial in presenting the individual's qualifications and experiences in a clear and compelling manner. Your goal is to produce a professional CV that accurately reflects the individual's profile. Utilize the detailed profile report on person_name to draft a CV that includes sections on their background, education, interests, and current projects. Ensure the CV is well-organized, visually appealing, and free of errors. The document should be formatted in MS Word and tailored to highlight the individual's strengths and achievements. The output should be a complete CV for person_name, formatted in MS Word, with sections that clearly outline their professional history, educational background, personal interests, and current projects. Maintain a professional tone and ensure the document is ready for use in professional settings.",
    tools=[],
    max_iterations=None
)

# Define connections
supervisor_model = chat_openai
worker_0_supervisor = supervisor
worker_1_supervisor = supervisor
worker_0_tools = [serper]