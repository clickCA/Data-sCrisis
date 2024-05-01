import json
import pyarrow.feather as feather
import pyarrow
import pprint
def extract_data_to_feather(json_file, feather_file):
    """Extracts target data from a JSON file and writes it to a feather file."""

    with open(json_file, 'r') as f:
        data = json.load(f)

    # Access relevant data structures within the JSON
    abstracts_retrieval_response = data['abstracts-retrieval-response']
    item = abstracts_retrieval_response['item']
    bibrecord = item['bibrecord']
    head = bibrecord['head']
    tail = bibrecord['tail']
    pprint.pp(head)
    # Extract target data
    # title = head['citation-title']
    # abstract = head['abstracts']
    # date_of_publication = head['source']['publicationdate']  # Consider further processing for desired format
    # affiliations = []
    # for author_group in head.get('author-group', []):
    #     for aff in author_group.get('affiliation', []):
    #         print(aff)
    # citations = tail.get('bibliography', {}).get('reference', [])  # Handle potential absence of bibliography
    # keywords = head['citation-info'].get('author-keywords', {}).get('author-keyword', None)

    # # Process document classification codes (assuming they are in 'enhancement')
    # classification_codes = []
    # if 'enhancement' in head:
    #     for classificationgroup in head['enhancement']['classificationgroup']:
    #         print((classificationgroup))
    #         # for classification in classificationgroup['classifications']:
    #             # classification_codes.append(classification['classification-code'])

    # # Create a list of dictionaries for each record
    # records = [
    #     {
    #         'Title': title,
    #         'Abstract': abstract,
    #         'Document Classification Codes': classification_codes,
    #         'Date of Publication': date_of_publication,
    #         'Affiliations': affiliations,
    #         'Citations': citations,
    #         'Keywords': keywords
    #     }
    # ]

    # # Create a PyArrow table and write to feather file
    # table = pyarrow.Table.from_pylist(records)
    # feather.write_feather(table, feather_file)

# Example usage
json_file_path = 'data/2018/201802791.json'
feather_file_path = 'extract_data/2018/201802791.feather'
extract_data_to_feather(json_file_path, feather_file_path)