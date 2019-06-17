import os

import yaml

def analyze_data(file_name, key):

    # with open(".%sdata%s%s.yaml" % (os.sep, os.sep, file_name), "r",encoding="utf-8") as f:
    #     case_data = yaml.load(f)[key]
    #
    #     data_list = list()
    #     for i in case_data.values():
    #         data_list.append(i)
    with open(r"./data/" + file_name + ".yaml", "r",encoding="utf-8") as f:
        data = yaml.load(f)
        data_list = list()
        data_list.extend(data[key].values())
        return data_list
