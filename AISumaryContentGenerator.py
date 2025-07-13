import pandas as pd

class AISumaryContentGenerator:
    def __init__(self, data):
        self.data = data
        self.gotManualRisk = (manualRisk := data.get('manualRisk')) and manualRisk.get('MANUAL_RISK_DESC') != ""
        self.customerData = {
            "Customer Name": self.data["customer"][0]["INFO_NAME_FULL"],
            "CIF No.": self.data["customer"][0]["NO_CIF"],
            "ID": self.data["customer"][0]["ID1_NO"],
            "DOB/Age": f'{self.data["customer"][0]["INFO_DOB"]} / {self.data["customer"][0]["INFO_AGE"]}',
            "Country": self.data["customer"][0]["INFO_NAT"],
            "Employment": self.data["customer"][0]["INFO_OCC"],
            "Income (Monthly)": self.data["customer"][0]["INFO_INCOME"],
            "Customer's risk level": f'{self.data["systemRisk"][0]["LAST_RISK_LEVEL"]} (System){ " / " + self.data["manualRisk"][0]["MANUAL_RISK_DESC"] + " (Manual)" if self.gotManualRisk else ""}',
        }
        self.rfTxnData = self.data["rfTxnHit"]

    def aggregateTxn(self):
        df = pd.DataFrame(self.rfTxnData)
        df.fillna('unknown', inplace=True)

        # return df.to_dict(orient="records")

        # Ensure date is datetime
        df["TRAN_DATE"] = pd.to_datetime(df["TRAN_DATE"])

        # Group by sender and beneficiary names (with banks)
        group_cols = ["SENDER_NAME", "SENDER_BANK", "BENEFICIARY_NAME", "BENEFICIARY_BANK"]

        # Aggregate: sum amount, min date, max date
        aggDf = df.groupby(group_cols).agg(
            TOTAL_AMOUNT=("AMOUNT", "sum"),
            FIRST_TRAN_DATE=("TRAN_DATE", "min"),
            LAST_TRAN_DATE=("TRAN_DATE", "max")
        ).reset_index()
        
        aggDf['FIRST_TRAN_DATE'] = aggDf['FIRST_TRAN_DATE'].dt.strftime('%Y-%m-%d')
        aggDf['LAST_TRAN_DATE'] = aggDf['LAST_TRAN_DATE'].dt.strftime('%Y-%m-%d')

        # Optional: convert to list of dicts
        result = aggDf.to_dict(orient="records")
        
        return result

    def generateContent(self):
        result = {}
        
        result['Initial Risk'] = '<p><b>Alerted Scenario</b>:</p>' + '<ol>' + ''.join(f'<li>{o["HIT_RULEID"]} - {o["HIT_RULENAME"]}</li>' for o in self.data['hitRule']) + '</ol>'
        result['Research on Focus'] = ''.join(f'<p><b>{key}</b>: {value}</p>' for key, value in self.customerData.items())

        return result
