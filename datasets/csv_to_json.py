import csv
import json

ADS = 'ads'
CATEGORY = 'categories'


def convert_file(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model, 'pk': int(row['id'] if 'id' in row else row['Id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'is_published' in row:
                row['is_published'] = bool(row['is_published'].lower())
            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as js_file:
        js_file.write(json.dumps(result, ensure_ascii=False))


convert_file(f"{ADS}.csv", f"{ADS}.json", "ads.ad")
convert_file(f"{CATEGORY}.csv", f"{CATEGORY}.json", "ads.category")


