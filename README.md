# Smart MCQ Solver

An AI-powered Multiple Choice Question (MCQ) solver built for the **Smart MCQ Solver Challenge**. This project explores transformer-based models and parameter-efficient fine-tuning techniques (LoRA) to accurately rank answer choices for challenging multiple-choice questions.

## Student Details

- **Name:** Soham Maity
- **Student ID:** 24F2008474

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
