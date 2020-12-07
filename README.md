# EY_GDS_Project : Prototype submission for Intent based search and Classification

![img](https://github.com/Soumi7/EY_GDS_Project/blob/main/images/im_ey_1.png)

## Hackpions – EY GDS Hackathon

## Theme

Intent based search and Classification

## Problem statement

- Propose and design an algorithm that can periodically crawl content repositories of files (shared file or SharePoint) to determine the properties (metadata) and the content of the files and match them against some predefined intents. Example: reusable assets, policy documents and solution accelerators

- List and match metadata of newly added items and add metadata of the matching items to a tracking database with an index and matched pre-defined intents

We have a created a solution for both the points!

## Solution

### Features

- Retrainable on new data.
- Can crawl through all files and sub-folders in a parent repository and generate intents for each specific file.
- It stores all this information in <insert csv name>
- We have an intelligent query search which undertands the intents associated with a query sentence and provides the file names and location of the intents of this query.

## Dataset

### External libraries and frameworks used :

- pdfminer.six : To extract text from pdfs.
- bert-for-tf2 : For fine tuning the Bert model with our training data. 
- tensorflow : Using keras to create a custom model
- pandas - for data analysis
- os - For crawling through repository.
- sklearn - 
- nltk

## Portability

- We give the notebook access to google drive using an API access token.
- In the same way, we can connect share point.
- For the folder you want to crawl, just provide the path of the folder like we have for our google drive folder.

### Repository structure : 

- data_to_preprocess :
  - This folder contains training files.
  - You can put pdfs or documents into this file for training.
  - Then type ```python3 preprocessing_folder.py```
  - Executing preprocessing_folder.py will extract sentences from the files in this folder and store them with the respective intents.

- EY_DATA : 
  - Has some Case_Study pdfs by provided by EY.
  - Can be removed if required.

- API_access_code_snippet :
  - Sharepoint API client

- preprocessing_folder.py :
  - Preprocesses the data_to_preprocess folder to extract training sentences from the folders.
  - Creates a csv file of the sentences and their respective intents.

- Crawler_and_intelligent_query_search.ipynb :
  - Uses train.csv, test.csv and valid.csv to fine tune BERT.
  - Shows the test accuracies and metrics.
  - The model contains the new updated checkpoints now.
  - Download this complete folder.

- crawler.py :
  - Crawls through any given content repository.
  - Loads the trained model.
  - For each file, it predicts the intents of the file.
  - It stores the filename, file location and unique intents in a csv.

- query_search.py :
  - You can enter as many number of queries you want.
  - For each query sentence, our model predicts its intent or intents.
  - We look through the csv of files and respectivey intents generated in the crawling process.
  - If our query sentence's intent matches with intent of any file, we display that file.
  - In this way, we display all the files which have the intents in the query sentence.

## Why is this is an intelligent search?

  - Because we recognise the intents of the query sentence first.
  - Then we check if some files have the same intents.
  - For each file in the repo, we have already predicted multiple intents.


## Steps to execute :

- Create a new conda envioronment.
- Install the dependancies with ```pip install -r requirements.txt```.


