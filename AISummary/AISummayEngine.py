from jsonDataProcessor import JsonDataProcessor
import json

class AISummaryEngine():
    def __init__(self, fieldKeys, schemaDescFilename):
        self.fieldKeys = fieldKeys
        self.schemaDescFilename = schemaDescFilename

    def getFieldSchemaDict(self):
        jsonFile = open(self.schemaDescFilename, 'r')
        fieldDesc = json.load(jsonFile)
        jsonFile.close()

        return {item["fieldName"]: item["description"] for item in fieldDesc}


    def getAISummaryContent(self, jsonData):
        fieldSchemaDict = self.getFieldSchemaDict()

        jsonDataProcessor = JsonDataProcessor()

        observations = [fieldSchemaDict.get(o, '') + ': ' + jsonDataProcessor.getJsonDataValue(jsonData, o.split('_')) for o in self.fieldKeys]
        print(observations)
        

