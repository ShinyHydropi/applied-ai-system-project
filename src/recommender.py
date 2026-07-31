import csv
from typing import Callable, List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_artist: str | None = None
    favorite_genre: str | None = None
    favorite_mood: str | None = None
    target_energy: float | None = None
    target_bpm: float | None = None
    target_valence: float | None = None
    target_danceability: float | None = None
    target_acousticness: float | None = None

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(*csv_paths: str) -> List[Dict]:
    """
    Loads songs from one or more CSV files into a combined list of dicts.
    Required by src/main.py
    """
    songs = []
    for csv_path in csv_paths:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                songs.append({
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                })
    return songs

CATEGORICAL_SONG_FIELDS = {"genre", "mood", "artist"}
CATEGORICAL_MISMATCH_ERROR = 0.2

# tempo_bpm lives on a ~60-180 scale while the other numeric features
# (energy, valence, danceability, acousticness) are all 0-1. Dividing its
# error by this range brings it back down to roughly the same scale so it
# doesn't dominate the MSE.
TEMPO_BPM_RANGE = 200.0

# Maps each UserProfile field to the song dict key it's compared against.
_PROFILE_TO_SONG_FIELD = {
    "favorite_artist": "artist",
    "favorite_genre": "genre",
    "favorite_mood": "mood",
    "target_energy": "energy",
    "target_bpm": "tempo_bpm",
    "target_valence": "valence",
    "target_danceability": "danceability",
    "target_acousticness": "acousticness",
}


def score_song(user_profile: UserProfile, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against a UserProfile's preferences.
    Required by recommend_songs() and src/main.py

    Lower scores are better matches. For each preference the profile sets
    (i.e. not None), we compute an error against the song's value:
      - categorical features (genre, mood, artist) get an error of 0.0
        for an exact match, otherwise a fixed 0.2
      - numerical features (energy, valence, danceability, acousticness)
        get an error of (target - actual)
      - tempo_bpm gets that same error normalized by TEMPO_BPM_RANGE, since
        it's on a much larger scale than the other numeric features
    The final score is the mean of those errors squared (MSE), so
    missing all preferences closely is favored over nailing a few and
    ignoring the rest.
    """
    errors = []
    reasons = []

    for profile_field, song_field in _PROFILE_TO_SONG_FIELD.items():
        target = getattr(user_profile, profile_field)
        if target is None or song_field not in song:
            continue

        actual = song[song_field]

        if song_field in CATEGORICAL_SONG_FIELDS:
            if str(actual).lower() == str(target).lower():
                errors.append(0.0)
                reasons.append(f"{song_field} matches ({actual})")
            else:
                errors.append(CATEGORICAL_MISMATCH_ERROR)
                reasons.append(f"{song_field} doesn't match (wanted {target}, got {actual})")
        else:
            error = target - actual
            reasons.append(f"{song_field} target {target}, actual {actual} (off by {abs(error):.2f})")
            errors.append(error / TEMPO_BPM_RANGE if song_field == "tempo_bpm" else error)

    if not errors:
        return 0.0, ["No preferences specified"]

    mse = sum(error ** 2 for error in errors) / len(errors)
    return mse, reasons

def recommend_songs(
    user_profile: UserProfile,
    songs: List[Dict],
    k: int = 5,
    explain_fn: Optional[Callable[[Dict, List[str], float], str]] = None,
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py

    Scores every song against user_profile and returns the k lowest-scoring
    (best-matching) songs, sorted from best to worst.

    explain_fn, if given, turns each song's (song, reasons, score) into the
    explanation string instead of the default "; ".join(reasons) template —
    e.g. src.explain.generate_explanation for an LLM-written explanation.
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_profile, song)
        if explain_fn is not None:
            explanation = explain_fn(song, reasons, score)
        else:
            explanation = "; ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda entry: entry[1])
    return scored[:k]
