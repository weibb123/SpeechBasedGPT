# SpeechBasedGPT

## Demonstration
https://github.com/weibb123/SpeechBasedGPT/assets/84426364/9af3ce7f-55e1-49c4-9680-640993874c99

## Table of Contents

  - [Business problem](#business-problem)
  - [Data source](#data-source)
  - [Methods](#methods)
  - [Tech Stack](#tech-stack)
  - [Lessons learned and recommendation](#lessons-learned-and-recommendation)
  - [Limitation and what can be improved](#limitation-and-what-can-be-improved)
  - [Evaluation](#Evaluation)

## Business Problem

Recently, I learned that Mercedes Benz install ChatGPT in their car system which gives me the inspiration to build a voice GPT web application. By allowing customers to talk to ChatGPT can be incorporate in many technologies such as Alexa, Siri, car system, or software applications that assist users.

## Data Source
No dataset was needed for this project. Only input from user is their speech

## Methods

  1. User clicks the button
  2. recognize user's voice and perform speech recognition using Google's speech recognition algorithm
  3. Convert user's speech into text
  4. Input user's text to ChatGPT to get response
  5. Can change ChatGPT's persona to fit your own use case
  6. GPT will give a response based on te text provided.

## Tech Stack

- Python/LangChain (Main coding)
- OPENAI API (Leveraging Large Language Model)
- STREAMLIT (UI for the system)
- Google voice recognition

## Lessons learned and recommendation


## Limitation and what can be improved


## Evaluation

Although this webapp does not include evaluation.., one can certainly use different evaluation methods to evaluate success.\
BLEU score: comparing human response and GPT response\
OPENAI API Check: Check whether GPT response contains harmful content\
Human validation: Check if GPT reponse match with what human will typically response.


