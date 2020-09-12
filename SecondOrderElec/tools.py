##
# This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.
#
# @authors: vincentchoqueuse, slashformotion
##
import numpy as np


def export_csv(data_list, filename="data.csv", header="", delimiter=","):
    """export csv data to file

    Args:
        data_list (dataframe): the data to store
        filename (str, optional): filename. Defaults to "data.csv".
        header (str, optional): header for dataframe. Defaults to "".
        delimiter (str, optional): delimiter for csv file. Defaults to ",".
    """
    if not filename.endswith(".csv"):
        filename += ".csv"
    data_2D = np.vstack(data_list)
    data_2D = np.transpose(data_2D)
    np.savetxt(filename, data_2D, delimiter, header=header)
