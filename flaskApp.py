from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import traceback
from AISumaryContentGenerator import AISumaryContentGenerator

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# utility function
def returnStringJsonContent(content):
    return json.dumps(json.dumps(content))

# core function
@app.route("/ping", methods=['GET'])
@cross_origin()
def ping():
    return returnStringJsonContent({"result": "pong"}), 200
    
@app.route("/get-ai-summary", methods=['POST'])
@cross_origin()
def getAISummary():
    return returnStringJsonContent({"observation": ["abcefg", "123456"], "recommendation": "Based on the observation, it is recommended to escalate the case."})

    # receiving data
    data = {}
    for line in request.stream:
        try:
            if line := line.strip():
                record = json.loads(line)

                table, tableData = next(iter(record.items()))
                if table and tableData:
                    if table not in data.keys():
                        data[table] = []
                    data[table].append(tableData)

            else:
                continue
        except Exception as e:
            print(f"Invalid line: {line} - {e}")
            return returnStringJsonContent({"error": f"{line}- {traceback.format_exc()}"})

    # generating result
    try:
    
        return json.dumps("hihi")

        summaryGenerator = AISumaryContentGenerator(data)
        data['aggregatedTxn'] = summaryGenerator.aggregateTxn()

        return returnStringJsonContent(data), 200

        summaryGenerator = AISumaryContentGenerator(data)
        return returnStringJsonContent(summaryGenerator.generateContent()), 200
    
    except:
        print({"error": traceback.format_exc()})
        return returnStringJsonContent({"error": traceback.format_exc()})    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10500, debug=False)
    # app.run()