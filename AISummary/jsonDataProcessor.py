class JsonDataProcessor:
    def __init__(self):
        pass

    def getJsonDataValue(self, jsonData, keyList):
        if jsonData.get(keyList[0]) is not None:
            if len(keyList) == 1:
                return jsonData[keyList[0]]
            else:
                return [self.getJsonDataValue(item, keyList[1:]) for item in jsonData[keyList[0]]] if isinstance(jsonData[keyList[0]], list) else self.getJsonDataValue(jsonData[keyList[0]], keyList[1:])
        else:
            return ''
        
    def getStringData(self, data):
        if isinstance(data, list):
            return ", ".join(f"'{x}'" for x in data)
        else:
            return str(data) 
