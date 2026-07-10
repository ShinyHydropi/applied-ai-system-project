# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

My design will be rule-based recommendation system that scores each song based on how closely it matches a user's preferences. For numerical features, score will be calculated with mean square error in order to prioritize matching all features closely over matching some features exactly and some weakly. For categorical features, since a comprehensive model of relationships between catagories would probably require a neural network, exact matches will be treated as an error of 0 and anything else as an error of 0.2. This fixed error may result in the recommender worrying more about matching numerical features than categorical features. Rankings are determined by lowest to highest MSE.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Top recommendations:

Sunrise City - Score: 0.00
Because: genre matches (pop); mood matches (happy); energy target 0.8, actual 0.82 (off by 0.02)

Rooftop Lights - Score: 0.01
Because: genre doesn't match (wanted pop, got indie pop); mood matches (happy); energy target 0.8, actual 0.76 (off by 0.04)

Gym Hero - Score: 0.02
Because: genre matches (pop); mood doesn't match (wanted happy, got intense); energy target 0.8, actual 0.93 (off by 0.13)

Fiesta Nocturna - Score: 0.03
Because: genre doesn't match (wanted pop, got latin); mood doesn't match (wanted happy, got festive); energy target 0.8, actual 0.8 (off by 0.00)

City Lights Anthem - Score: 0.03
Because: genre doesn't match (wanted pop, got hip hop); mood doesn't match (wanted happy, got confident); energy target 0.8, actual 0.85 (off by 0.05)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



