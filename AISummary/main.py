import re
from keywordExtractor import KeywordExtractor
from RAG import RAG
from AISummayEngine import AISummaryEngine
import json


# process scenario data
with open('config/scenarios.txt', 'r') as file:
    scenarioData = [{'scenario': re.sub(r'^\d+\.\s*|\n$', '', o)} for o in list(file)]

keywordExtractor = KeywordExtractor()
ragModel = RAG()

for o in scenarioData:
    o['keyword'] = keywordExtractor.extractKeyword(o['scenario'])
    o['dataFieldKey'] = ragModel.getRelatedContent(', '.join(o['keyword']), './config/dataSchema.json')[0]['fieldName']

print(json.dumps(scenarioData, indent=4))


data = {
    "hitRule": {
        "ruleId": 'RLT1'
    },
    "customerRisk": {
        "currentRisk": 'high'
    },
    "customer": {
        "nationality": 'Msia',
        "age": 36
    }
}

# generate summary
aiSummaryEngine = AISummaryEngine([o['dataFieldKey'] for o in scenarioData], './config/dataSchema.json')
aiSummaryEngine.getAISummaryContent(data)
