import re
from KeywordExtractor import KeywordExtractor
from RAG import RAG
import json

with open('config/appSetting.json', 'r') as file:
    config = json.load(file)
    verbose = config['verbose']

with open('config/scenarios.txt', 'r') as file:
    scenarioData = [{'scenario': re.sub(r'^\d+\.\s*|\n$', '', o)} for o in list(file)]

keywordExtractor = KeywordExtractor()
ragModel = RAG()

for o in scenarioData:
    o['keyword'] = keywordExtractor.extractKeyword(o['scenario'])
    o['dataFieldKey'] = ragModel.getRelatedContent(', '.join(o['keyword']), './config/dataSchema.json')[0]['fieldName']

if verbose:
    print(json.dumps(scenarioData, indent=4))

with open("data/scenarioKeyMapping.json", "w") as file:
   json.dump(scenarioData, file)