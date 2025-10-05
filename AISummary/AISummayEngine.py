from JsonDataProcessor import JsonDataProcessor
from DecisionAgent import CaseDecisionAgent
import json

class AISummaryEngine():
    def __init__(self, llm, scenarioKeyFilename, schemaDescFilename, scenarioFilename, verbose: bool = False):
        self.llm = llm
        self.scenarioKeyFilename = scenarioKeyFilename
        self.schemaDescFilename = schemaDescFilename
        self.scenarioFilename = scenarioFilename
        self.verbose = verbose

    def readFile(self, filename):
        data = ''
        if (filename.split('.')[-1].lower() == 'json'):
            jsonFile = open(filename, 'r')
            data = json.load(jsonFile)
            jsonFile.close()
        else:
            file = open(filename, 'r')
            data = list(file)
            file.close()
        return data
    
    def getFieldKeys(self):
        scenarioData = self.readFile(self.scenarioKeyFilename)        
        return [o['dataFieldKey'] for o in scenarioData]

    def getFieldSchemaDict(self):
        fieldDesc = self.readFile(self.schemaDescFilename)

        return {item["fieldName"]: item["description"] for item in fieldDesc}
    
    def getObservation(self, jsonData):
        fieldSchemaDict = self.getFieldSchemaDict()
        jsonDataProcessor = JsonDataProcessor()
        fieldKeys = self.getFieldKeys()

        return [fieldSchemaDict.get(o, '') + ': ' + str(value) for o in fieldKeys if (value := jsonDataProcessor.getJsonDataValue(jsonData, o.split('_'))) != '' ]

    def getAISummaryContent(self, jsonData):
        observations = self.getObservation(jsonData)
        scenarios = self.readFile(self.scenarioFilename)
        decisionAgent = CaseDecisionAgent(model= self.llm, verbose=self.verbose)

        if self.verbose:
            print(observations, scenarios)

        return {
            "observation": observations,
            "recommendation": decisionAgent.decideInvestigationNeed(observations, scenarios)
        }
        

        

