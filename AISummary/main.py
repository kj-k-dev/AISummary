from AISummayEngine import AISummaryEngine
import json

with open('config/appSetting.json', 'r') as file:
    config = json.load(file)
    verbose = config['verbose']
    llm = config['llm']

# data = {
#     "hitRule": {
#         "ruleId": 'RLT1'
#     },
#     "customerRisk": {
#         "currentRisk": 'high'
#     },
#     "customer": {
#         "nationality": 'Msia',
#         "age": 36
#     }
# }
data = {'hitRule': [{'ruleId': '', 'scenarioDescription': 'MANUAL TRANSACTION CASE'}, {'ruleId': 'RLT1', 'scenarioDescription': 'Large Cash Deposit (>= 10000 in MYR)'}], 'transactionSummary': ['The total transaction amount is 150.00', 'The total transaction count is 1', 'Rule ID  MANUAL TRANSACTION CASE detected on 20221007', 'Rule ID RLT1 Large Cash Deposit (>= 10000 in MYR) detected on 20230302 to 20230314'], 'customer': {'cifId': '110000147', 'cifName': 'ABDULLAH B MUSA', 'id': '', 'dob': 19340101, 'age': '91', 'nationality': '', 'occupation': '', 'industry': '', 'monthlyIncome': ''}, 'customerCurrentRisk': '', 'customerPreviousRisk': '', 'customerManualRisk': '', 'riskModelFactor': '', 'riskFactorValue': '', 'caseHistory': '', 'counterparties': ''}

# generate summary
aiSummaryEngine = AISummaryEngine(
    llm,
    './data/scenarioKeyMapping.json',
    './config/dataSchema.json',
    './config/scenarios.txt',
    verbose=False
)
response = aiSummaryEngine.getAISummaryContent(data)
print(json.dumps(response, indent=4))
