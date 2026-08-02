# Final Project Details

## Original Project Summary (Music Recommender Simulation)

This system is intendended to be used to find new music for a user to enjoy. Songs output by this system are ranked according to user preferences. 

---

## Title and Summary

This project, **Regression Suggestions 2.0**, is a rule-based recommendation system that matches user preferences to songs using mean squared
error (MSE). Using MSE, this system recommends songs that more holistically match the user's preferences. Generative AI features surround this
recommender engine with natural language parsing to generate an object to represent user preferences, and generated explanations for the
rankings of recommended songs.

---

## Architecture Overview

Song data from the data folder and a natural language description of the user's preferences are taken as input. The description is parsed into
a json file of the UserProfile representing the set of preferences. The model also generates a confidence score of the parsing for the user.
Every song is scored against the UserProfile and ranked using MSE. The details of the scoring are used to prompt AI to generate an explanation
of each score. These explanations are checked for their length and trustworthyness. The UserProfile, confidence score, and recommended songs
with their explained scores are output to the user. Before every AI call there is a guard for prompt injection.

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
python -m src.regression_suggestions
```

## Sample Recommendation Output

### Sample 1
```
python -m src.regression_suggestions                                        
Describe your music taste (mood, genre, artists, energy, etc.): I prefer music that is more energetic, dynamic, upbeat, and a little funky.

Generated preferences: UserProfile(favorite_artist=None, favorite_genre='funk', favorite_mood='upbeat', target_energy=0.8, target_bpm=120.0, target_valence=None, target_danceability=0.7, target_acousticness=0.3)
LLM confidence in these preferences: 85%

=== Top 10 recommendations ===

Night Drive Loop by Neon Echo - Score: 0.02
Because: I recommend "Night Drive Loop" by Neon Echo, though it's a moody synthwave track rather than the upbeat funk you wanted.

Rooftop Lights by Indigo Parade - Score: 0.02
Because: While "Rooftop Lights" by Indigo Parade misses your funk and upbeat preferences, it's a happy indie pop track with a close tempo and energy.

Sunrise City by Neon Echo - Score: 0.02
Because: While the genre and mood missed the mark, Sunrise City by Neon Echo matches your energy and tempo targets closely!

Storm Runner by Voltline - Score: 0.03
Because: "Storm Runner by Voltline isn't a great match because the genre, mood, tempo, and other features don't align with your upbeat funk preferences."

Golden Hour Highway by Crimson Fade - Score: 0.03
Because: I wouldn't recommend "Golden Hour Highway" by Crimson Fade since you wanted upbeat funk, but this is a nostalgic country track with lower energy and tempo.

Island Breeze by Solar Tide - Score: 0.03
Because: "Island Breeze" by Solar Tide is a playful reggae track that's slower and more acoustic than your upbeat, energetic funk target.

City Lights Anthem by Bass Ritual - Score: 0.03
Because: I recommend "City Lights Anthem" by Bass Ritual; while it's confident hip hop instead of your desired upbeat funk, it hits your exact energy target!

Gym Hero by Max Pulse - Score: 0.03
Because: "Gym Hero by Max Pulse" isn't a great match because it's an intense pop track rather than your desired upbeat funk.

Velvet Nights by Marlowe Grey - Score: 0.04
Because: genre doesn't match (wanted funk, got r&b); mood doesn't match (wanted upbeat, got romantic); energy target 0.8, actual 0.5 (off by 0.30); tempo_bpm target 120.0, actual 84.0 (off by 36.00); danceability target 0.7, actual 0.68 (off by 0.02); acousticness target 0.3, actual 0.42 (off by 0.12)

Neon Pulse Rave by Kilowatt - Score: 0.04
Because: genre doesn't match (wanted funk, got edm); mood doesn't match (wanted upbeat, got euphoric); energy target 0.8, actual 0.96 (off by 0.16); tempo_bpm target 120.0, actual 128.0 (off by 8.00); danceability target 0.7, actual 0.93 (off by 0.23); acousticness target 0.3, actual 0.04 (off by 0.26)
```

### Sample 2
```
python -m src.regression_suggestions   
Describe your music taste (mood, genre, artists, energy, etc.): I love relaxed, easy-going jazz — coffee shop afternoons, not club energy. Warm, mostly acoustic instrumentation, and nothing too danceable.

Generated preferences: UserProfile(favorite_artist=None, favorite_genre='jazz', favorite_mood='relaxed', target_energy=0.3, target_bpm=80.0, target_valence=0.6, target_danceability=0.2, target_acousticness=0.9)
LLM confidence in these preferences: 95%

=== Top 10 recommendations ===

Coffee Shop Stories by Slow Stereo - Score: 0.02
Because: You'll love "Coffee Shop Stories" by Slow Stereo because its jazz genre and relaxed mood match your preferences perfectly!

Spacewalk Thoughts by Orbit Bloom - Score: 0.02
Because: Orbit Bloom's "Spacewalk Thoughts" is a great ambient track that comes close on energy, valence, and acousticness, though the genre and tempo differ from your jazz request.

Autumn Sonata by Elena Voss - Score: 0.02
Because: Although it misses your jazz and relaxed preferences by giving you a melancholic classical piece, "Autumn Sonata" matches your energy and danceability targets.

Desert Bloom by Wandering Roots - Score: 0.03
Because: genre doesn't match (wanted jazz, got folk); mood doesn't match (wanted relaxed, got warm); energy target 0.3, actual 0.45 (off by 0.15); tempo_bpm target 80.0, actual 96.0 (off by 16.00); valence target 0.6, actual 0.74 (off by 0.14); danceability target 0.2, actual 0.48 (off by 0.28); acousticness target 0.9, actual 0.8 (off by 0.10)

Library Rain by Paper Lanterns - Score: 0.03
Because: Although the genre and mood differ from your jazz and relaxed preferences, "Library Rain" by Paper Lanterns is a close overall match with great acoustic and valence alignment!

Focus Flow by LoRoom - Score: 0.04
Because: "Focus Flow by LoRoom" features the right tempo, but it’s lofi instead of jazz and more focused than your relaxed mood.

Delta Crossroads by Otis Blackwood - Score: 0.04
Because: genre doesn't match (wanted jazz, got blues); mood doesn't match (wanted relaxed, got sad); energy target 0.3, actual 0.33 (off by 0.03); tempo_bpm target 80.0, actual 70.0 (off by 10.00); valence target 0.6, actual 0.28 (off by 0.32); danceability target 0.2, actual 0.38 (off by 0.18); acousticness target 0.9, actual 0.65 (off by 0.25)

Midnight Coding by LoRoom - Score: 0.04
Because: While "Midnight Coding" by LoRoom didn't match your jazz and relaxed preferences, its tempo was very close to what you wanted!

Golden Hour Highway by Crimson Fade - Score: 0.07
Because: While it doesn't match your relaxed jazz preference, "Golden Hour Highway" by Crimson Fade is a nostalgic country song you might still enjoy!

Velvet Nights by Marlowe Grey - Score: 0.08
Because: genre doesn't match (wanted jazz, got r&b); mood doesn't match (wanted relaxed, got romantic); energy target 0.3, actual 0.5 (off by 0.20); tempo_bpm target 80.0, actual 84.0 (off by 4.00); valence target 0.6, actual 0.7 (off by 0.10); danceability target 0.2, actual 0.68 (off by 0.48); acousticness target 0.9, actual 0.42 (off by 0.48)
```

---

## Design Decisions

For reliability, I opted for a confidence score over options like testing or logging. With a natural language description of preferences, the
correct UserProfile can be ambiguous. While testing and logging may be more effective when evaluating how agents reach a target, confidence
scores effectively evaluate accuracy for targets open to interpretation.

---

## Testing Summary

I tested a few different prompts to get the desired level of creativity in UserProfile generation. Initially, Gemini felt obliged to fill every
field of the UserProfile even if it was not hinted at in the prompt. Prompting AI with "do not invent any facts" helped but it would not fill
in fields that were not explicitly mentioned in the description. The prompt that let the AI infer just enough included "It is okay to interpret
the description slightly creatively, but do not include fields that you have no confidence in."

---

## Reflection

Through this assignment, I learned that small changes in how you prompt AI can have an important impact on its output. I also learned how to
integrate generative AI agent calls into code using API. Furthermare, working on this project has strengthed my ability to prompt AI
assistants. These skills will be invaluable as tech careers expect proficiency in many CS subjects.