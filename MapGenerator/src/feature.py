class Feature:
    id = 0
    name = ""
    latitude = 0
    longitude = 0
    comment = ""
    marker = "campsite"
    size = "medium"
    color = "#77777"

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.latitude = float(row[2])
        self.longitude = float(row[3])
        self.comment = row[4]
        self.marker = row[5]
        self.size = row[6]
        self.color = row[7]

    def get_dict(self):
        values = dict({'_comment': self.id, 'type': 'Feature',
                       'properties': {'marker-color': self.color, 'fill': '#808080', 'stroke': '#808080',
                                      'marker-size': self.size, 'marker-symbol': self.marker,
                                      'popup-text': str(self.id) + ": " + self.name, 'color': self.color},
                       'geometry': {'type': 'Point', 'coordinates': [self.longitude, self.latitude]}})
        return values
