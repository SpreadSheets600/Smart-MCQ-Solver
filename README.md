# Smart MCQ Solver

An AI-powered Multiple Choice Question (MCQ) solver built for the **Smart MCQ Solver Challenge**. This project explores transformer-based models and parameter-efficient fine-tuning techniques (LoRA) to accurately rank answer choices for challenging multiple-choice questions.

## Project Description

Welcome to the Smart MCQ Solver Challenge!

In this competition, participants are required to build AI based systems capable of solving complex multiple choice questions. Each question contains a prompt along with five possible answer options labeled A, B, C, D, and E. The objective is to predict the top three most likely correct answers in ranked order.

The competition is designed to provide hands on experience in developing, training, and evaluating machine learning models for multiple choice question answering. Participants are encouraged to experiment with different approaches, including transformer based models, fine tuning, retrieval based methods, ensemble techniques, and efficient inference pipelines.

Rather than focusing on a single modeling strategy, the competition encourages participants to compare approaches, analyze their performance, and build solutions that achieve strong predictive accuracy on the provided benchmark dataset.

Submissions will be evaluated using Mean Average Precision at 3 (MAP@3), where models receive higher scores when the correct answer appears earlier in their ranked predictions.

Goal: The goal of this competition is to develop AI based models that accurately rank the most probable answers for multiple choice questions using the provided dataset. Participants are expected to apply appropriate machine learning techniques, evaluate different modeling strategies, and optimize their solutions to achieve the best performance under the given evaluation metric.

## Student Details

- **Name:** Soham Maity
- **Student ID:** 24F2008474

<img width="1240" height="388" alt="dms_capture_1793904819463" src="https://github.com/user-attachments/assets/02151cfe-3fdf-49a5-ae66-6ee744d54d01" />

## Competition Objective

The goal of this challenge is to develop an intelligent model capable of predicting the **top three most likely correct answers** for each multiple-choice question.

Each question consists of:
- A prompt
- Five answer choices (A, B, C, D, E)

Instead of predicting only the correct answer, the model must rank the three most probable answers in order of confidence.

## Evaluation Metric

Submissions are evaluated using **Mean Average Precision at 3 (MAP@3)**.

A higher score is achieved when the correct answer appears earlier in the predicted ranking.

| Ground Truth | Prediction | Result |
|--------------|------------|--------|
| A | A B C | Best |
| A | B A C | Good |
| A | C D A | Lower |


## Submission Format

Predictions must contain **exactly three ranked answer labels** separated by spaces.

Example:

```csv
ID,Prediction
1,A B C
2,C A D
3,B D A
```

## Competition

**Smart MCQ Solver Challenge**

The competition focuses on developing AI systems capable of reasoning over multiple-choice questions and effectively ranking the most probable answers using modern Natural Language Processing techniques.
