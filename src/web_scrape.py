import os

# import requests
import logging

# import json
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv
from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import re

# from bs4 import BeautifulSoup

load_dotenv()  # take environment variables from .env.
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

API_KEY = os.getenv("ELSEVIER_API_KEY")
TIME_OUT = 10

## Initialize client
client = ElsClient(API_KEY)


def read_affiliations(affil_id):
    """Find affiliations by ID

    Args:
        affil_id (_type_): affiliation with ID as string
    """
    my_aff = ElsAffil(affil_id=affil_id)
    if my_aff.read(client):
        print("my_aff.name: ", my_aff.name)
        my_aff.write()
    else:
        print("Read affiliation failed.")


def read_scopus_abstract(scp_id):
    """read scopus through scp_id

    Args:
        scp_id (string): scopus id
    """
    ## Scopus (Abstract) document example
    # Initialize document with ID as integer
    scp_doc = AbsDoc(scp_id=scp_id)
    if scp_doc.read(client):
        print("scp_doc.title: ", scp_doc.title)
        scp_doc.write()
    else:
        print("Read document failed.")


def read_science_direct_pii(sd_pii):
    ## ScienceDirect (full-text) document example using PII
    pii_doc = FullDoc(sd_pii=sd_pii)
    if pii_doc.read(client):
        print("pii_doc.title: ", pii_doc.title)
        pii_doc.write()
    else:
        print("Read document failed.")


def read_science_direct_doi(doi):
    ## ScienceDirect (full-text) document example using DOI
    doi_doc = FullDoc(doi=doi)
    if doi_doc.read(client):
        print("doi_doc.title: ", doi_doc.title)
        doi_doc.write()
    else:
        print("Read document failed.")


def find_scopus_id_in_serch_result(search_result):
    pattern = r"\d+"

    # Find all numbers in the input string
    numbers = re.findall(pattern, search_result)

    if numbers:
        extracted_number = numbers[0]
        return extracted_number


def search_scopus(get_all=False, count=25):
    """search scopus for author

    Args:
        auth_name (_type_): _description_
    """
    doc_srch = ElsSearch(
        'AFFILCOUNTRY ( thailand ) AND PUBYEAR > 2023 AND ( LIMIT-TO ( SUBJAREA , "ENGI" ) )',
        "scopus",
    )
    doc_srch.execute(client, get_all=get_all, count=count)
    print("doc_srch has", len(doc_srch.results), "results.")
    for doc in doc_srch.results:
        print("scopus_id_raw", doc["dc:identifier"])
        scopus_id = find_scopus_id_in_serch_result(doc["dc:identifier"])
        print("scopus_id", scopus_id)
        read_scopus_abstract(scopus_id)
        print("Finished reading scopus")
        print("=====================================")


def main():
    # ? Search something
    search_scopus(False, 5)
    # ? Using this to be a core map old data 1-1
    # read_scopus_abstract("85170238281")

    # read_affiliations("60091507")
    # read_science_direct_doi("10.1016/j.ijbiomac.2023.126316")
    # read_science_direct_pii("S1674927814000082")
    return


if __name__ == "__main__":
    main()
