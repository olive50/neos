"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    # Declaration of list of dicts witch will contain a list of neos in form of dict
    neos = []
    with open(neo_csv_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            neo = NearEarthObject(**item)
            neos.append(neo)
            #print(neo)
    return neos

#load_neos("./data/neos.csv")

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    # below declaration of list of dictionnary objects  of close approches
    cas = []
    with open(cad_json_path, 'r') as jsonfile:
        content = json.load(jsonfile)
        for info in content["data"]:
            ca = CloseApproach(**dict(zip(content["fields"], info)))
            #print(ca)
            cas.append(ca)
                
    return cas

# load_approaches("./data/cad.json")
