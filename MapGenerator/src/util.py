import csv
import json
import numpy as np
from src.feature import Feature
import easygui


def load_csv():
    type = '*.csv'
    path = easygui.fileopenbox(default=type, title='Laden der CSV', filetypes=type)
    with open(path, 'r') as file:
        if not path.lower().endswith('.csv'):
            print('wrong file type')
            return []
        csv_reader = csv.reader(file, delimiter=';')

        line_count = 0
        count = 0
        features = []
        for row in csv_reader:
            if line_count != 0 and len(row[0]) > 0:
                feature = Feature(row)
                features.append(feature)
                count += 1
            line_count += 1

    print(f'Processed {count} features.')
    return features


def update_json(features):
    type = "*.geojson"
    path = easygui.fileopenbox(filetypes=type, default=type, title='Laden der Karte')
    with open(path, 'r') as file:
        if not path.lower().endswith(('.json', '.geojson')):
            print('wrong file type')
            return

        data = json.load(file)
        for feature in features:
            data['features'].append(feature.get_dict())

        type = "*.geojson"
        path = easygui.filesavebox(filetypes=type, default=type, title='Speichern')
        with open(path, 'w') as output_file:
            if not path.lower().endswith(('.json', '.geojson')):
                print('wrong file type')
                return
            json.dump(data, output_file, indent=4)
