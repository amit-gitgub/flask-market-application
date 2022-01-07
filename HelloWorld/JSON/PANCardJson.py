import json
import requests
with open("BOSPS3111P.json",'r') as file:

    data = json.load(file)

    # This method is just to pretify the json.
    prety_json = json.dumps(data, indent=2)


    #print(prety_json)
    print(data['ITR']['ITR1']['Refund']['BankAccountDtls']['AddtnlBankDetails'][0])

    for k,v in data['ITR']['ITR1']['Refund']['BankAccountDtls']['AddtnlBankDetails'][0].items():
        #print(f"{item}--->{data['ITR']['ITR1']['Refund']['BankAccountDtls']['AddtnlBankDetails'][0][item]}")
        print(k,v)
