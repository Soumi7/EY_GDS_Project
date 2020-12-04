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
  - Crawls through the complete repository.