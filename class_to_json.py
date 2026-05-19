from character_sheet import gear
import json

jsonArr = []
for armor in gear.allarmor:
    jsonArr.append(armor.__dict__)

jsonString = json.dumps(jsonArr, indent = 4)

with open('armor.json', 'w', encoding = 'utf-8') as jsonfile:
    jsonString = json.dumps(jsonArr, indent=4)
    jsonfile.write(jsonString)