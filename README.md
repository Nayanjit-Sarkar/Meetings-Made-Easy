# Meeting Analysis

Welcome to the Meeting Analysis repository! In this section, we will discuss the approach taken to tackle the problem statement of meeting analysis. The primary goal of this project is to extract meaningful insights and patterns from meeting data using data analysis and natural language processing techniques.

## Data Collection
For the purpose of meeting analysis, two approaches were employed to gather the necessary data:

#### Approach 1: AMI Dataset
The initial dataset was sourced from the Hugging Face Dataset Hub, specifically leveraging the  [AMI dataset](https://groups.inf.ed.ac.uk/ami/corpus/). The AMI dataset contains a collection of meeting recordings, covering various scenarios and meeting types. To ensure relevance and focus, scenario-based meetings were selected from the AMI dataset, providing a diverse range of meeting scenarios for analysis.

#### Approach 2: ChatGPT-generated Dataset
As the required meeting transcripts were not available in the initial dataset, a new dataset was manually created using ChatGPT. This involved generating 220 meeting transcripts by providing ChatGPT with a prompt describing the meeting topic and participants.

### Dataset Format
The dataset is available in a structured format, with each data sample containing the following fields:

- start_time: The start time of the speech segment in the format "HH:MM:SS".
- end_time: The end time of the speech segment in the format "HH:MM:SS".
- speaker: The speaker ID for the speech segment.
- text: The transcribed text of the speech segment.

## Chosen Approach
The chosen approach for the meeting analysis task is Natural Language Processing (NLP) with Spacy. This decision was made based on the following considerations:

1. Familiarity and Individual Work: Being Familiar with Spacy, and leveraging existing knowledge and experience in Spacy expedited the development process.

2. Accurate Named Entity Recognition (NER): NER is a critical aspect of meeting analysis, particularly in identifying and extracting relevant entities from the transcripts. Spacy is known for its accurate and efficient NER capabilities, making it an ideal choice for this task.



## Model Building

To facilitate the analysis of meeting transcripts, a custom NER (Named Entity Recognition) model was developed. Here's an overview of the steps involved in building the model:

### NER Text Annotator: 
To annotate the meeting transcripts with relevant entities, a [NER text annotator](https://tecoholic.github.io/ner-annotator/) was utilized. This annotator allows for the annotation of text segments as either regular text or assignee information.

### Preprocessing and Modification: 
The generated annotated JSON file was preprocessed and modified to meet the requirements of the Spacy NER model.

### Training and Validation: 
Using the modified JSON file, separate .spacy files were created for training and validation purposes.

### Customization of Spacy NER Model: 
The .spacy files were used to train and customize the Spacy NER model. This allows the model to accurately identify and classify entities within the meeting transcripts.

## Citations
The following resources were referred to during the development process:

- [AMI dataset](https://groups.inf.ed.ac.uk/ami/corpus/)
- [NER text annotator](https://tecoholic.github.io/ner-annotator/)
- [Spacy](https://spacy.io/usage/training)

  
## Limitations
The current approach using NLP with Spacy for meeting analysis has certain limitations, including:

- Accuracy of entity recognition: The performance of the entity recognition model heavily relies on the quality and diversity of the training data. In cases where the transcripts contain uncommon or domain-specific terms, the accuracy of entity recognition may be affected.

- Handling of noisy data: Meeting transcripts can often contain noise, such as overlapping speech or incomplete sentences. The current approach may face challenges in accurately processing such noisy data.

- Limited context understanding: While NLP techniques can extract useful information from meeting transcripts, they may have limitations in capturing the full context and nuances of human conversations. This can potentially affect the accuracy and comprehensiveness of the analysis.

It is important to keep these limitations in mind when interpreting the results of the meeting analysis

## Setup
1. Clone the repository to your local machine:
  ```
  git clone https://github.com/DiveHQ-Octernships/dive-ml-engineering-octernship-Nayanjit-Sarkar.git
  ```

2. Install the required dependencies by running the following command:
```
pip install python
pip install spacy
python -m spacy download en_core_lg
```
This will install all the necessary libraries and packages needed to run the codebase.

## Running the Pipeline

1. Prepare your meeting transcript file in the required format.

2. Place the transcript file in the designated input folder.

3. Run the pipeline script to generate the transcript and extract action items:
```
python main.py
```
4. The pipeline will process the meeting transcript and generate the output.

5. Once the pipeline completes, the action items will be printed to the console, with each item on a separate line.

Congratulations! You have successfully set up the codebase and run the Meeting Analysis Pipeline. Make sure to review the generated action items for further analysis and decision-making.

Please note that the specific commands and file formats may vary depending on your project setup and requirements. Make sure to adapt the instructions accordingly.

Feel free to reach out if you have any questions or encounter any issues during the setup or execution of the pipeline.

## Demo Video

For a more detailed understanding of how Meeting Analysis works and its features, watch the demo video. The video provides a live demonstration of the project in action, showcasing the transcript parsing, action item extraction, and participant contribution analysis.

- [Demo Video](https://drive.google.com/file/d/1JmxqQ6cmB8XQrBYKzANbF9vSGEa9b_Cv/view?usp=sharing)
