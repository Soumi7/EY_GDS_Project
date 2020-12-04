# EY_GDS_Project


### Repository structure : 

- data_to_preprocess :
  - This folder contains training files.
  - You can put pdfs or documents into this file for training.
  - Then type ```python3 preprocessing_folder.py```
  - Executing preprocessing_folder.py will extract sentences from the files in this folder and store them with the respective intents.

- EY_DATA : 
  - Has some Case_Study pdfs by provided by EY.
  - Can be removed if required.

- Test_pdfs :
  - Remove this?

- API_access_code_snippet :
  - Remove, but not sure

- preprocessing_folder.py :
  - Preprocesses the data_to_preprocess folder to extract training sentences from the folders.
  - Creates a csv file of the sentences and their respective intents.

- EY_intent_classification_Working_1.ipynb :
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
- Install the dependancies with ```pip install -m requirements.txt```.
