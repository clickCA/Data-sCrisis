# Data Science Project

## Description

This project is a data science project that aims to [provide a brief description of your project and its goals].

## Table of Contents

- [Data Science Project](#data-science-project)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data](#data)
  - [Methods](#methods)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Installation

install the required packages using the following command:

```bash
pip install -r src/requirements.txt
```

## Usage

[Explain how to use your project, including any command-line arguments or configuration settings.]

## Data

Some useful tools for viewing JSON data (You can use this to see the whole object and understand the structure of the data):
<https://jsonviewer.stack.hu/>

- The **original** data from the following [link](<https://drive.google.com/drive/folders/1Qndie0dRyqe6pHoJK-KiPqgGBic6wpDn>):

- The **extracted** data can download via the following [link](https://drive.google.com/file/d/1FgrptkisPslqzkTcDu2PJbZEJlFwyB--/view?usp=sharing):

**the important field that will be extract**:

| Field in json                                                               | Type  in json | Description                                                                                                            | Type after Extraction | Field after Extraction                              |
| --------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------- |
| abstracts-retrieval-response.item.bibrecord.head.citation-title             | String        | The citation title of the paper                                                                                        | String                | citation-title                                      |
| abstracts-retrieval-response.item.bibrecord.head.abstracts                  | String        | The abstract of the paper                                                                                              | String                | abstracts                                           |
| abstracts-retrieval-response.item.bibrecord.tail.bibliography.reference     | List          | The List references of the paper                                                                                       | String                | references                                          |
| abstracts-retrieval-response.item.bibrecord.tail.bibliography.@refcount     | Integer       | The number of references                                                                                               | Integer               | refcount                                            |
| abstracts-retrieval-response.affiliation                                    | List          | The List of afflication -contain  affiliation-city, affilname, affiliation-country                             | String                | affiliations                                        |
| abstracts-retrieval-response.coredata.citedby-count                         | Integer       | The number of                                                                                                          | Integer               | a.citedby-count                                     |
| abstracts-retrieval-response.coredata.prism:issn : "14683288 00175749"      | String        | The issn number of this publication                                                                                    | String                | issn                                                |
| abstracts-retrieval-response.coredata.eid                                   | String        | This should be the primary key of this                                                                                 | String                | eid                                                 |
| abstracts-retrieval-response.coredata.dc:title                              | String        | journal title or another identifier for the journal                                                                    | String                | journal-title                                       |
| abstracts-retrieval-response.coredata.dc:description                        | String        | journal description                                                                                                    | String                | description                                         |
| abstracts-retrieval-response.coredata.dc:publisher                          | String        | journal publisher                                                                                                      | String                | publisher                                           |
| * _PRISM_ is a set of metadata vocabularies designed to describe _magazine_ | -             | -                                                                                                                      | -                     | -                                                   |
| abstracts-retrieval-response.coredata.prism:CoverDate                       | String        | The date displayed on the cover                                                                                        | String                |                                                     |
| abstracts-retrieval-response.coredata.prism:aggregationType                 | String        | The aggregation Type                                                                                                   | String                | aggregation-type                                    |
| abstracts-retrieval-response.coredata.prism:publicationName                 | String        | The publication name _the title is the title of the article, and the publication name is the name of the journal._ | String                | publication-name                                    |
| abstracts-retrieval-response.language.@xml:lang                             | String        | The language of this journal                                                                                           | String                | language                                            |
| abstracts-retrieval-response.subject-areas.subject-area.$                   | List          | List of related subject areas                                                                                          | String                | subject-area                                        |
| abstracts-retrieval-response.authors.author.preferred-name.ce:given-name    | List          | List of authors name                                                                                                   | String                | Will merge with surname and initial call "Fullname" |
| abstracts-retrieval-response.authors.author.preferred-name.ce:surname       | List          | List of authors surname                                                                                                | String                | -                                                   |
| abstracts-retrieval-response.authors.author.preferred-name.ce:initials      | List          | List of authors's                                                                                                      | String                | -                                                   |

## Methods

### Data extraction

You can rerun the data extraction process by running the following command:

```bash
unrar x Data 2018-2023.rar 
sh gen_json.sh
python src/data_extraction.py
python src/merge_data.py
```

[Explain the methods or algorithms used in your project, including any data analysis or machine learning techniques.]

## Results

[Present the results of your project, including any visualizations or performance metrics.]

## Contributing

[Provide guidelines for contributing to your project, if applicable.]

## License

[Specify the license under which your project is released.]

## Contact

[Provide contact information for any questions or inquiries.]
