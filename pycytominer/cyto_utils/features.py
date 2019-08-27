"""
Utility function to manipulate cell profiler features
"""

import os
import pandas as pd

blacklist_file = os.path.join(
    os.path.dirname(__file__), "..", "data", "blacklist_features.txt"
)


def get_blacklist_features(blacklist_file=blacklist_file, population_df=None):
    """
    Get a list of blacklist features

    Arguments:
    blacklist_file - file location of dataframe with features to exclude
    population_df - profile dataframe used to subset blacklist features [default: None]

    Return:
    list of features to exclude from downstream analysis
    """

    blacklist = pd.read_csv(blacklist_file)

    assert any(
        [x == "blacklist" for x in blacklist.columns]
    ), "one column must be named 'blacklist'"

    blacklist_features = blacklist.blacklist.to_list()
    if isinstance(population_df, pd.DataFrame):
        population_features = population_df.columns.tolist()
        blacklist_features = [x for x in blacklist_features if x in population_features]

    return blacklist_features


def label_compartment(cp_features, compartment, metadata_cols):
    """
    Assign compartment label to each features as a prefix

    Arguments:
    cp_features - list of all features being used
    compartment - a string indicating the measured compartment
    metadata_cols - a list indicating which columns should be considered metadata

    Return:
    Recoded column names with appopriate metadata and compartment labels
    """

    compartment = compartment.Title()
    avail_compartments = ["Cells", "Cytoplasm", "Nuceli", "Image", "Barcode"]

    assert (
        compartment in avail_compartments
    ), "provide valid compartment. One of: {}".format(avail_compartments)

    cp_features = [
        "Metadata_{}".format(x)
        if x in metadata_cols
        else "{}_{}".format(compartment, x)
        for x in cp_features
    ]

    return cp_features


def infer_cp_features(population_df):
    """
    Given a dataframe, output features that we expect to be cell painting features
    """
    features = [
        x
        for x in population_df.columns.tolist()
        if (
            x.startswith("Cells_")
            | x.startswith("Nuclei_")
            | x.startswith("Cytoplasm_")
        )
    ]

    return features
