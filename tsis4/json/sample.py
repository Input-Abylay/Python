import json
with open('sample-data.json') as file: 
   data = json.load(file)


print('Interface Status')
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 50 + ' ' + '-' * 20 + ' ' + '-'*6 + ' ' + '-' * 6)

for i in data['imdata']:
    print(f"{i['l1PhysIf']['attributes']['dn']:<70} {i['l1PhysIf']['attributes']['speed']:<6}  {i['l1PhysIf']['attributes']['mtu']}")