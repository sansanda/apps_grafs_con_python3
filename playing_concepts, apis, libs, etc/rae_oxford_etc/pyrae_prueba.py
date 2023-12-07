from pyrae import dle
import json

palabra = 'verbo'
res = dle.search_by_word(word=palabra)
res = res.to_dict()
print(res)

with open('data.json', 'w') as f:
    json.dump(res, f)

# convertir res a string
json_string = json.dumps(res)

data = json.loads(json_string)
print(data['articles'][0]['definitions'][0]['sentence']['text'])

for articles in data['articles']:
    for definitions in articles['definitions']:
        print(definitions['sentence'])

