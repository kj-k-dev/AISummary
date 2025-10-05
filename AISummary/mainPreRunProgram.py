import re
from KeywordExtractor import KeywordExtractor
from RAG import RAG
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

with open("data/scenarioKeyMapping.json", "w") as file:
   json.dump(scenarioData, file)