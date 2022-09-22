import os


def check_file_creation(file_dir):
    assert os.path.isfile(file_dir)  # check if the new html file is created


def check_if_file_not_empty(file_dir):
    assert os.stat(file_dir).st_size != 0  # check if the new file is not empty


def check_if_variable_is_not_empty(variable):
    assert variable is not None
