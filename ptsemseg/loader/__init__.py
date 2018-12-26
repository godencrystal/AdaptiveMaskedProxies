import json

from ptsemseg.loader.pascal_voc_loader import pascalVOCLoader
from ptsemseg.loader.pascal_voc_5i_loader import pascalVOC5iLoader

def get_loader(name):
    """get_loader

    :param name:
    """
    return {
        "pascal": pascalVOCLoader,
        "pascal5i": pascalVOC5iLoader,
    }[name]


def get_data_path(name, config_file="config.json"):
    """get_data_path

    :param name:
    :param config_file:
    """
    data = json.load(open(config_file))
    return data[name]["data_path"]
