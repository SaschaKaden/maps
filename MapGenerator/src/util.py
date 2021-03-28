import csv
import json
import numpy as np
from src.feature import Feature
import easygui


def load_csv():
    path = easygui.fileopenbox()
    with open(path, 'r') as file:
        if not path.lower().endswith('.csv'):
            print('wrong file type')
            return []
        csv_reader = csv.reader(file, delimiter=';')

        line_count = 0
        features = []
        for row in csv_reader:
            if line_count != 0 and len(row[0]) > 0:
                feature = Feature(row)
                features.append(feature)
            line_count += 1

    print(f'Processed {line_count-1} features.')
    return features


def update_json(features):
    path = easygui.fileopenbox()
    with open(path, 'r') as file:
        if not path.lower().endswith('.json'):
            print('wrong file type')
            return

        data = json.load(file)
        for feature in features:
            data['features'].append(feature.get_dict())

        path = easygui.filesavebox()
        with open(path, 'w') as output_file:
            if not path.lower().endswith('.json'):
                print('wrong file type')
                return
            json.dump(data, output_file)
