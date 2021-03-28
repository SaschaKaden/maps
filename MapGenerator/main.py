
import numpy as np
from src.feature import Feature
from src import util

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    features = util.load_csv()
    util.update_json(features)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
