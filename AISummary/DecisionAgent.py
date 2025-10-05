import requests

class CaseDecisionAgent:
    def __init__(self, model: str = "llama3.2:latest", verbose: bool = False):
        self.model = model
        self.apiUrl = "http://localhost:11434/api/generate"
        self.verbose = verbose

    def formatList(self, items):
        return "\n".join(f"- {item}" for item in items) if items else "None"

    def getPrompt(self, observations, scenarios):
        return f"""
You are a compliance analyst reviewing a potential suspicious activity case.

You are given:
1. A list of observations from transaction monitoring or customer behavior analysis.
2. A list of suspicious scenarios that need further investigation.

Your task:
Decide if the case **needs further investigation**. A case need further investigation when any of the observations matches at least one of the given scenarios.

Respond in formal and concise sentence to include:
- whether the case needs further investigation or not. (Dont show 'Yes' or 'No').
- **brief explanation** of your decision. (Dont state the scenario number)

Output format:
- dont use new line in string sentence

---  
Observations:
{self.formatList(observations)}

Scenarios:
{self.formatList(scenarios)}

Does this case need further investigation?
Answer:
""".strip()

    def decideInvestigationNeed(self, observations, scenarios) -> bool:
        payload = {
            "model": self.model,
            "prompt": self.getPrompt(observations, scenarios),
            "stream": False
        }

        try:
            response = requests.post(self.apiUrl, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error communicating with Ollama: {e}")

        output = response.json().get("response", "").strip()
        if self.verbose:
            print("Model output:")
            print(output)

        return output
