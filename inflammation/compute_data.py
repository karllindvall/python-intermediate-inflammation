"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

class CSVDataSource:

    def __init__(self, data_path):
        self.data_path = data_path


    def load_inflammation_data(self):
        """Loads the data from all files in the data_path directory.

        Args:
            data_path (str): The path to the data files

        Raises:
            ValueError: There are no CSV files in the chosen path

        Returns:
            array: inflammation data from all CSV files in the path
        """
        data_file_paths = glob.glob(os.path.join(self.data_path, 'inflammation*.csv'))
        if len(data_file_paths == 0):
            raise ValueError(f"No inflammation CSV files found in the path {self.data_path}")
        data = map(models.load_csv, data_file_paths)
        return list(data)


class JSONDataSource:

    def __init__(self, data_path):
        self.data_path = data_path

    def load_inflammation_data(self):
        """Same purpose as CSVDataSource, but for JSON files containing inflammation data."""
        data_file_paths = glob.glob(os.path.join(self.data_path, 'inflammation*.json'))
        if len(data_file_paths = 0):
            raise ValueError(f"No inflammation JSON files found in the path {self.data_path}")
        data = map(models.load_json, data_file_paths)
        return list(data)


def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation


def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Plots the graphs of standard deviation of daily means."""
    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    #views.visualize(graph_data)
    return daily_standard_deviation
