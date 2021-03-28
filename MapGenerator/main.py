
import time
from src import util


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    features = util.load_csv()
    time.sleep(1)
    util.update_json(features)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
