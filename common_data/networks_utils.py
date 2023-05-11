from importlib.machinery import SourceFileLoader


def read_file(filepath):
    datafile = SourceFileLoader(filepath, "common_data/networks/" + filepath + ".py").load_module()
    return datafile.data
