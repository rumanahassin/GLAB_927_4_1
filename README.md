
# GLAB 927.4.1 - Hands-On Sentiment Analysis With Python

## Project Overview

This lab explores how Python and TextBlob can analyze
customer feedback to identify positive and negative sentiment.

## Tools Used

- Python 3.13
- TextBlob
- uv
- Visual Studio Code

## Tasks Completed

### Task 1: Import TextBlob
Installed TextBlob and verified that the library works.

### Task 2: Analyze a Customer Review
Analyzed a positive customer review and calculated:
- Polarity: 0.8125
- Subjectivity: 0.8

### Task 3: Analyze Multiple Reviews
Used a Python list and a for loop to analyze four
customer reviews.

Results:
- Fantastic service: 0.30
- Unhappy with product quality: -0.60
- Okay, but could be improved: 0.50
- Amazing experience: 0.70

## How to Run

From the project folder, run:

```bash
uv sync
uv run python src/glab_927_4_1/sentiment_analysis.py
```

## What I Learned

I learned how to use TextBlob to calculate sentiment
scores and how Python loops can automate the analysis
of multiple customer reviews.

I also noticed that TextBlob gave a positive score
to a review containing mixed feedback. This helped
me understand that automated sentiment analysis
has limitations and may require human interpretation.
