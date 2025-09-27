class JsonDataProcessor:
    def __init__(self):
        pass

    def getJsonDataValue(self, jsonData, keyList):
        if jsonData.get(keyList[0]) is not None:
            return self.getJsonDataValue(jsonData[keyList[0]], keyList[1:]) if len(keyList) > 1 else jsonData[keyList[0]]
        else:
            return ''
