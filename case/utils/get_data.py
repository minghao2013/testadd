import os.path

import yaml


def get_file_path(file_type="data\\data.yml"):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    # print(dir_path)
    # print(os.path.join(dir_path, "..\\", file_type))
    final_path = yaml.safe_load(os.path.join(dir_path, "..\\", file_type))
    return final_path


def get_data(name="add", level="P0", ids="ids", filepath="data\\data.yml"):
    final_path = get_file_path(filepath)
    with open(final_path, encoding="utf-8")as f:
        source_result = yaml.safe_load(f)
    # print(source_result)
    data = source_result.get(name).get(level).get("data")
    ids_name = source_result.get(name).get(level).get(ids)
    return data, ids_name

# if __name__ != "main":
#     data_result = get_data("add", "P0", "ids")
#     print(data_result)
