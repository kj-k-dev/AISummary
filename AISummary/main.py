import re
from keywordExtractor import KeywordExtractor
from RAG import RAG
import json


# region read scenario data
with open('config/scenarios.txt', 'r') as file:
    data = [{'scenario': re.sub(r'^\d+\.\s*|\n$', '', o)} for o in list(file)]


# object initialization
keywordExtractor = KeywordExtractor()
ragModel = RAG()

for o in data:
    o['keyword'] = keywordExtractor.extractKeyword(o['scenario'])
    o['dataFieldKey'] = ragModel.getRelatedContent(', '.join(o['keyword']), './config/dataSchema.json')[0]['fieldName']

print(json.dumps(data, indent=4))

