# 🎧 Model Card: Music Recommender Simulation

## Limitations and Bias 

The preference parser is not trained on training data with prompts and their intended UserProfiles. This runs a risk of confident wrong, and
unconfident correct UserProfiles. This model also generates a UserProfile when the input is not even a description of music preferences.

---

## Proper use  

This model is particularly effective when given a description of music preferences. It can pick up on key fields of the UserProfile, and the
UserProfiles it produces have some variance. When given prompts that contained word that might appear in a description of preferences, the model
would sometimes create UserProfiles as if the context was music. Prompts that were of other contexts entirely usually produced empty
UserProfiles.

---

## Surprises  

Given the same prompt, the model generated a UserProfile with all 8 fields filled and a UserProfile with only 2 fields filled. Also, the model
was able to fill fields based only on the style of a given band (The Beatles). This meant it had enough information about Beatles songs to
confidently assert fields like tempo and acousticness.

---

## AI Collaboration  

A helpful instance of an AI recommendation was combining the AI helper functions into a separate module. This simplified the code around AI
calls (preference parsing and explanation generation). An unhelpful suggestion was using dicts instead of UserProfiles for recommending songs.
This would require helper functions in the rest of the logic to switch between the two objects.