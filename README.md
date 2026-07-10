# 🎵 Music Recommender Simulation

## Project Summary

This system is intendended to be used to find new music for a user to enjoy. Songs output by this system are ranked according to user preferences. 

---

## How The System Works

My design will be rule-based recommendation system that scores each song based on how closely it matches a user's preferences. For numerical features, score will be calculated with mean square error (MSE) in order to prioritize matching all features closely over matching some features exactly and some weakly. For categorical features, since a comprehensive model of relationships between catagories would probably require a neural network, exact matches will be treated as an error of 0 and anything else as an error of 0.2. This fixed error may result in the recommender worrying more about matching numerical features than categorical features. Rankings are determined by lowest to highest MSE.

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

One experiment I tried was using profiles with only some features included. Due to the process used for scoring, removal of features did not drastically affect the rankings.

---

## Limitations and Risks

One weakness of the model is that it cannot dynamically tune itself to improve its recommendations. Thus, it must rely on a user's own interpretation of features. Additionally, it cannot adapt with a change in user preferences without the user adjusting the themselves

---

## Reflection

Through this assignment, I learned that recommendation models have to balance the importance of many features when recommending songs to users. In working on this project, I continued honing my skills with prompting AI assistants on generating code. I have noticed that the AI is requiring less prompts to acheive the results I am intending.



## Output of Profiles
```
=== Top recommendations for pop fan ===

Sunrise City - Score: 0.00
Because: genre matches (pop); mood matches (happy); energy target 0.8, actual 0.82 (off by 0.02); valence target 0.8, actual 0.84 (off by 0.04); danceability target 0.8, actual 0.79 (off by 0.01); acousticness target 0.2, actual 0.18 (off by 0.02)

Rooftop Lights - Score: 0.01
Because: genre doesn't match (wanted pop, got indie pop); mood matches (happy); energy target 0.8, actual 0.76 (off by 0.04); valence target 0.8, actual 0.81 (off by 0.01); danceability target 0.8, actual 0.82 (off by 0.02); acousticness target 0.2, actual 0.35 (off by 0.15)

Gym Hero - Score: 0.01
Because: genre matches (pop); mood doesn't match (wanted happy, got intense); energy target 0.8, actual 0.93 (off by 0.13); valence target 0.8, actual 0.77 (off by 0.03); danceability target 0.8, actual 0.88 (off by 0.08); acousticness target 0.2, actual 0.05 (off by 0.15)

Fiesta Nocturna - Score: 0.02
Because: genre doesn't match (wanted pop, got latin); mood doesn't match (wanted happy, got festive); energy target 0.8, actual 0.8 (off by 0.00); valence target 0.8, actual 0.9 (off by 0.10); danceability target 0.8, actual 0.94 (off by 0.14); acousticness target 0.2, actual 0.15 (off by 0.05)

City Lights Anthem - Score: 0.02
Because: genre doesn't match (wanted pop, got hip hop); mood doesn't match (wanted happy, got confident); energy target 0.8, actual 0.85 (off by 0.05); valence target 0.8, actual 0.72 (off by 0.08); danceability target 0.8, actual 0.91 (off by 0.11); acousticness target 0.2, actual 0.08 (off by 0.12)


=== Top recommendations for rock fan ===

Storm Runner - Score: 0.00
Because: genre matches (rock); mood matches (intense); energy target 0.9, actual 0.91 (off by 0.01); valence target 0.5, actual 0.48 (off by 0.02); danceability target 0.6, actual 0.66 (off by 0.06); acousticness target 0.1, actual 0.1 (off by 0.00)

Night Drive Loop - Score: 0.02
Because: genre doesn't match (wanted rock, got synthwave); mood doesn't match (wanted intense, got moody); energy target 0.9, actual 0.75 (off by 0.15); valence target 0.5, actual 0.49 (off by 0.01); danceability target 0.6, actual 0.73 (off by 0.13); acousticness target 0.1, actual 0.22 (off by 0.12)

Iron Fist - Score: 0.02
Because: genre doesn't match (wanted rock, got metal); mood doesn't match (wanted intense, got angry); energy target 0.9, actual 0.97 (off by 0.07); valence target 0.5, actual 0.3 (off by 0.20); danceability target 0.6, actual 0.52 (off by 0.08); acousticness target 0.1, actual 0.03 (off by 0.07)

Gym Hero - Score: 0.03
Because: genre doesn't match (wanted rock, got pop); mood matches (intense); energy target 0.9, actual 0.93 (off by 0.03); valence target 0.5, actual 0.77 (off by 0.27); danceability target 0.6, actual 0.88 (off by 0.28); acousticness target 0.1, actual 0.05 (off by 0.05)

City Lights Anthem - Score: 0.04
Because: genre doesn't match (wanted rock, got hip hop); mood doesn't match (wanted intense, got confident); energy target 0.9, actual 0.85 (off by 0.05); valence target 0.5, actual 0.72 (off by 0.22); danceability target 0.6, actual 0.91 (off by 0.31); acousticness target 0.1, actual 0.08 (off by 0.02)


=== Top recommendations for jazz fan ===

Coffee Shop Stories - Score: 0.00
Because: genre matches (jazz); mood matches (relaxed); energy target 0.4, actual 0.37 (off by 0.03); valence target 0.7, actual 0.71 (off by 0.01); danceability target 0.5, actual 0.54 (off by 0.04); acousticness target 0.85, actual 0.89 (off by 0.04)

Desert Bloom - Score: 0.01
Because: genre doesn't match (wanted jazz, got folk); mood doesn't match (wanted relaxed, got warm); energy target 0.4, actual 0.45 (off by 0.05); valence target 0.7, actual 0.74 (off by 0.04); danceability target 0.5, actual 0.48 (off by 0.02); acousticness target 0.85, actual 0.8 (off by 0.05)

Library Rain - Score: 0.02
Because: genre doesn't match (wanted jazz, got lofi); mood doesn't match (wanted relaxed, got chill); energy target 0.4, actual 0.35 (off by 0.05); valence target 0.7, actual 0.6 (off by 0.10); danceability target 0.5, actual 0.58 (off by 0.08); acousticness target 0.85, actual 0.86 (off by 0.01)

Focus Flow - Score: 0.02
Because: genre doesn't match (wanted jazz, got lofi); mood doesn't match (wanted relaxed, got focused); energy target 0.4, actual 0.4 (off by 0.00); valence target 0.7, actual 0.59 (off by 0.11); danceability target 0.5, actual 0.6 (off by 0.10); acousticness target 0.85, actual 0.78 (off by 0.07)

Spacewalk Thoughts - Score: 0.02
Because: genre doesn't match (wanted jazz, got ambient); mood doesn't match (wanted relaxed, got chill); energy target 0.4, actual 0.28 (off by 0.12); valence target 0.7, actual 0.65 (off by 0.05); danceability target 0.5, actual 0.41 (off by 0.09); acousticness target 0.85, actual 0.92 (off by 0.07)


=== Conflicting signals (sad mood + high energy/valence/danceability) ===

Neon Pulse Rave - Score: 0.01
Because: mood doesn't match (wanted sad, got euphoric); energy target 0.9, actual 0.96 (off by 0.06); valence target 0.9, actual 0.88 (off by 0.02); danceability target 0.9, actual 0.93 (off by 0.03)

Fiesta Nocturna - Score: 0.01
Because: mood doesn't match (wanted sad, got festive); energy target 0.9, actual 0.8 (off by 0.10); valence target 0.9, actual 0.9 (off by 0.00); danceability target 0.9, actual 0.94 (off by 0.04)

Gym Hero - Score: 0.01
Because: mood doesn't match (wanted sad, got intense); energy target 0.9, actual 0.93 (off by 0.03); valence target 0.9, actual 0.77 (off by 0.13); danceability target 0.9, actual 0.88 (off by 0.02)

Sunrise City - Score: 0.02
Because: mood doesn't match (wanted sad, got happy); energy target 0.9, actual 0.82 (off by 0.08); valence target 0.9, actual 0.84 (off by 0.06); danceability target 0.9, actual 0.79 (off by 0.11)

Rooftop Lights - Score: 0.02
Because: mood doesn't match (wanted sad, got happy); energy target 0.9, actual 0.76 (off by 0.14); valence target 0.9, actual 0.81 (off by 0.09); danceability target 0.9, actual 0.82 (off by 0.08)


=== No preferences specified ===

Sunrise City - Score: 0.00
Because: No preferences specified

Midnight Coding - Score: 0.00
Because: No preferences specified

Storm Runner - Score: 0.00
Because: No preferences specified

Library Rain - Score: 0.00
Because: No preferences specified

Gym Hero - Score: 0.00
Because: No preferences specified


=== Extreme/out-of-range targets ===

Iron Fist - Score: 10.68
Because: genre doesn't match (wanted pop, got metal); energy target 5.0, actual 0.97 (off by 4.03); tempo_bpm target 999, actual 168.0 (off by 831.00); acousticness target -3.0, actual 0.03 (off by 3.03)

Storm Runner - Score: 11.08
Because: genre doesn't match (wanted pop, got rock); energy target 5.0, actual 0.91 (off by 4.09); tempo_bpm target 999, actual 152.0 (off by 847.00); acousticness target -3.0, actual 0.1 (off by 3.10)

Fiesta Nocturna - Score: 11.09
Because: genre doesn't match (wanted pop, got latin); energy target 5.0, actual 0.8 (off by 4.20); tempo_bpm target 999, actual 180.0 (off by 819.00); acousticness target -3.0, actual 0.15 (off by 3.15)

Neon Pulse Rave - Score: 11.14
Because: genre doesn't match (wanted pop, got edm); energy target 5.0, actual 0.96 (off by 4.04); tempo_bpm target 999, actual 128.0 (off by 871.00); acousticness target -3.0, actual 0.04 (off by 3.04)

Gym Hero - Score: 11.16
Because: genre matches (pop); energy target 5.0, actual 0.93 (off by 4.07); tempo_bpm target 999, actual 132.0 (off by 867.00); acousticness target -3.0, actual 0.05 (off by 3.05)


=== Genre/artist/mood not present in dataset ===

Sunrise City - Score: 0.04
Because: artist doesn't match (wanted Nonexistent Artist, got Neon Echo); genre doesn't match (wanted polka, got pop); mood doesn't match (wanted apathetic, got happy)

Midnight Coding - Score: 0.04
Because: artist doesn't match (wanted Nonexistent Artist, got LoRoom); genre doesn't match (wanted polka, got lofi); mood doesn't match (wanted apathetic, got chill)

Storm Runner - Score: 0.04
Because: artist doesn't match (wanted Nonexistent Artist, got Voltline); genre doesn't match (wanted polka, got rock); mood doesn't match (wanted apathetic, got intense)

Library Rain - Score: 0.04
Because: artist doesn't match (wanted Nonexistent Artist, got Paper Lanterns); genre doesn't match (wanted polka, got lofi); mood doesn't match (wanted apathetic, got chill)

Gym Hero - Score: 0.04
Because: artist doesn't match (wanted Nonexistent Artist, got Max Pulse); genre doesn't match (wanted polka, got pop); mood doesn't match (wanted apathetic, got intense)
```