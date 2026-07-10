# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **Regression Suggestions 1.0**  

---

## 2. Intended Use  

This system is intendended to be used to find new music for a user to enjoy. Songs output by this system are ranked according to user preferences. 

---

## 3. How the Model Works  

This model is a rule-based recommendation system that scores each song based on how closely it matches a user's preferences. For numerical features, score is calculated with mean square error (MSE) in order to prioritize matching all features closely over matching some features exactly and some weakly. For categorical features exact matches are treated as an error of 0 and anything else as an error of 0.2. This fixed error may result in the recommender worrying more about matching numerical features than categorical features. Rankings are determined by lowest to highest MSE.

---

## 4. Data  

The dataset used by the model is the initial set of songs and 10 AI generated songs. 

---

## 5. Strengths  

This model is particularly effective at ranking songs that more hollistically match the profile higher than songs which only match a few features very closely. 

---

## 6. Limitations and Bias 

One weakness of the model is that it cannot dynamically tune itself to improve its recommendations. Thus, it must rely on a user's own interpretation of features. Additionally, it cannot adapt with a change in user preferences without the user adjusting the themselves  

---

## 7. Evaluation  

Pop: The model correctly surfaced songs with high energy, high valence, high danceability, and low acousticness, matching the upbeat "happy" mood the profile targeted.

Rock: The model correctly searched for common rock features such as high energy, low acousticness, and an intense mood.

Jazz: The model correctly searced for common jazz features such as high acousticness, middling danceability, and a relaxed mood.

---

## 8. Future Work  

A future version of this model could use a neural network, sentiment analysis, or other architecture to more accurately evaluate error between categorical features.

---

## 9. Personal Reflection  

Through this assignment, I learned that recommendation models have to balance the importance of many features when recommending songs to users. In working on this project, I continued honing my skills with prompting AI assistants on generating code. I have noticed that the AI is requiring less prompts to acheive the results I am intending.
