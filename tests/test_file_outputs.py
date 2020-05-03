""" Test Suite """

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nemreader import output_as_csv
from nemreader import output_as_data_frames


def test_csv_output(tmpdir):
    """ Create a temporary csv output """
    file_name = "examples/unzipped/Example_NEM12_actual_interval.csv"
    output_files = output_as_csv(file_name, output_dir=tmpdir)
    assert len(output_files) == 1


def test_data_frame_output():
    """ Create a pandas dataframe """
    file_name = "examples/unzipped/Example_NEM12_actual_interval.csv"
    output_dfs = output_as_data_frames(file_name)
    for nmi, df in output_dfs:
        assert type(nmi) == str
        assert df["quality_method"][0] == "A"
