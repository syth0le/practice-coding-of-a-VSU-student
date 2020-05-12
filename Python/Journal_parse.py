import argparse
import os
import tempfile
import json
import sys
import plotly.offline as offline
import pandas as pd
from plotly.graph_objs import *


"""This program read log-files and get needful data-statistics from it, there is histogram is drawn by plotly.
Program works in 4 modes:
(for working u must use console and enter: python Journal_parse.py .... and then modes:)
1 - (.... --parse log-file --stat stat-file.csv --all) - this mode for reading every file for saving data to temporary-file in your system.
2 - (.... --parse log-file --stat stat-file.csv) - this mode for getting statistic from only one file with following histagram drawing.
3 - (.... --show show --stat stat-file.csv) - this mode for showing full info from temporary-file(with histagram drawing)
4 - (.... --clear clear) - clear your temporary-file with data.

for getting data only for one log-file use 2nd mode.
for getting full info from all files. use 1st mode for every file and finally use 3rd mode for drawing graphic.
DON'T forget use 4th mode to clear your temporary file after all work."""


data_input = {}  # dict for saving input data from input file.
data_for_stat_out = {}  # dict for saving all needful data to writing in statistic.txt.
time_dict = {}  # dict for saving login timings.


class FileReader:
    """class for reading from file.
    For using this class, new class example was created and it has got following updates"""

    def __init__(self, storage_path):
        self.raw = storage_path

    def read(self):
        """trying reading from file by context manager"""

        try:
            with open(self.raw, 'r') as file:
                _data = file.readlines()
            return _data
        except FileNotFoundError:
            return 'NO FILE IN SYSTEM'


def put(key, value):
    """putting needful values to dict"""

    if key in data_input:
        data_input[key].append(value)
    else:
        data_input[key] = [value]


def _splitting():
    """function of initial processing of input values"""

    for string in _file.read():
        massive = string.split(' ')
        timing = massive[0]
        work_time = timing[:5]
        facult_massive = massive[5].split("'")
        # trying to save input values to dict and process all errors and login fails.

        try:
            key_facult = facult_massive[1].split("@")[1]
            if key_facult.endswith('.vsu.ru'):
                put(key_facult, (timing, work_time))
            else:
                put("login failed", (timing, work_time))
        except:
            put("login failed", (timing, work_time))


def put_temp(key, data_structure):
    """function of counting quantity of faculties or etc"""

    _count = 0
    if key in data_structure:
        data_structure[key] += 1
    else:
        data_structure[key] = _count


def writing(stat_file, data_structure):
    """create output csv-file with context manager
    and  writing all needful values to it."""

    with open(stat_file, 'w') as f:
        f.write('key1;key2' + '\n')
        for key in data_structure:
            string = str(key) + ";" + str(data_structure[key])
            f.write(string + '\n')


def rewriting_data():
    """restructuring all time-data to correct format
    this needs to correct drawing output graphics"""

    for facult in data_input:
        for time in data_input[facult]:
            temp = time[1]
            if 0 <= int(temp[-2:]) < 10:
                temp = temp[:-2] + "05"
            elif 10 <= int(temp[-2:]) < 20:
                temp = temp[:-2] + "15"
            elif 20 <= int(temp[-2:]) < 30:
                temp = temp[:-2] + "25"
            elif 30 <= int(temp[-2:]) < 40:
                temp = temp[:-2] + "35"
            elif 40 <= int(temp[-2:]) < 50:
                temp = temp[:-2] + "45"
            elif 50 <= int(temp[-2:]) < 60:
                temp = temp[:-2] + "55"
            put_temp(temp, time_dict)


def get_data():
    """creating temporary file and get data from him."""
    
    if not os.path.isfile(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        local_data = f.read()
        if local_data:
            return json.loads(local_data)

        return {}



def put_data(dictionary):
    """put data to temporary file from dict, which was entered by u"""

    datas = get_data()
    _count = 0
    for key in dictionary:
        if key in datas:
            datas[key] += dictionary[key]
        else:
            datas[key] = dictionary[key]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(datas))


def clear():
    """remove temp-file from your system"""
    os.remove(storage_path)


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')  # create temp-file
    
    """parsing work arguments and get data from needful file."""
    parser = argparse.ArgumentParser(description="key-value storage")
    parser.add_argument('--parse', help='Parsing File')
    parser.add_argument('--stat', help='Statistic')
    parser.add_argument('--all', action='store_true', help='amount stat')
    parser.add_argument('--show', help='showing all stat')
    parser.add_argument('--clear', help='showing all stat')
    args = parser.parse_args()
    datas = get_data()
    work_file_ = args.parse
    stat_file = args.stat

    if args.parse and args.stat and args.all:
        if not os.path.exists(storage_path):
            with open(storage_path, 'w'):
                print('file was created')
        else:
            # reading work files from console.
            _file = FileReader(work_file_)
            _splitting()  # process our input data by created function

            for key in data_input:
                for value in data_input[key]:
                    put_temp(key, data_for_stat_out)

            rewriting_data()  # Preparing data for drawing graphics.
            put_data(time_dict)

    elif args.parse and args.stat:
        # reading work files from console.
        work_file_ = args.parse
        stat_file = args.stat
        _file = FileReader(work_file_)
        _splitting()  # process our input data by created function

        for key in data_input:
            for value in data_input[key]:
                put_temp(key, data_for_stat_out)

        rewriting_data()  # Preparing data for drawing graphics.
        writing(stat_file, time_dict) 

        """prepare our data and draw graphic"""
        df = pd.read_csv(stat_file, index_col=False, sep=';')
        df.sort_values("key1", inplace=True)
        df.head()
        trace = Scatter(x=df.key1, y=df.key2)

        data = [trace]

        offline.plot(data)
        writing(stat_file, data_for_stat_out)  # save faculties data to csv-file

    elif args.show and args.stat:
        
        """prepare our data and draw graphic"""
        writing(stat_file, datas)

        df = pd.read_csv(stat_file, index_col=False, sep=';')
        df.sort_values("key1", inplace=True)
        df.head()
        trace = Scatter(x=df.key1, y=df.key2)

        data = [trace]

        offline.plot(data)
        writing(stat_file, data_for_stat_out)  # save faculties data to csv-file

    elif args.clear:
        clear()
