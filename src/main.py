"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs, UserProfile
from src.explain import generate_explanation
from src.parse_preferences import parse_preferences


def print_recommendations(label: str, profile: UserProfile, songs: list, k: int = 5, explain_fn=None) -> None:
    recommendations = recommend_songs(profile, songs, k=k, explain_fn=explain_fn)

    print(f"\n=== {label} ===\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv", "data/ai_songs.csv")

    pop = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        target_valence=0.8,
        target_danceability=0.8,
        target_acousticness=0.2,
    )
    rock = UserProfile(
        favorite_genre="rock",
        favorite_mood="intense",
        target_energy=0.9,
        target_valence=0.5,
        target_danceability=0.6,
        target_acousticness=0.1,
    )
    # Demo of the structured-prompting input parser (src/parse_preferences.py):
    # the jazz profile is extracted from a free-text taste description
    # instead of being hand-filled, falling back to the literal UserProfile
    # below if parsing fails (no API key, network error, etc.).
    jazz_description = (
        "I love relaxed, easy-going jazz — coffee shop afternoons, not "
        "club energy. Warm, mostly acoustic instrumentation, and nothing "
        "too danceable."
    )
    jazz = parse_preferences(jazz_description) or UserProfile(
        favorite_genre="jazz",
        favorite_mood="relaxed",
        target_energy=0.4,
        target_valence=0.7,
        target_danceability=0.5,
        target_acousticness=0.85,
    )

    for profile in (pop, rock, jazz):
        # The jazz profile gets LLM-generated explanations (src/explain.py) as
        # a demo of the generative-AI explanation path; the rest use the
        # default templated explanation so the simulation stays API-free.
        explain_fn = generate_explanation if profile is jazz else None
        print_recommendations(
            f"Top recommendations for {profile.favorite_genre} fan",
            profile,
            songs,
            explain_fn=explain_fn,
        )
"""
    # --- Adversarial / edge case profiles ---
    # These aren't "realistic" users. They're crafted to probe whether
    # score_song/recommend_songs holds up under contradictory, empty, or
    # out-of-range input rather than to model a plausible listener.

    # Conflicting signals: energy/valence/danceability all say "upbeat party"
    # but mood says "sad". No real song will satisfy both halves, so this
    # checks that the scorer just averages the disagreement instead of
    # erroring or letting one strong signal silently dominate.
    conflicting_signals = UserProfile(
        favorite_mood="sad",
        target_energy=0.9,
        target_valence=0.9,
        target_danceability=0.9,
    )

    # No preferences at all: every field is None. score_song should hit its
    # "no preferences specified" fallback (score 0.0 for every song) rather
    # than raising, and recommend_songs should just return the first k songs
    # in whatever order they were loaded.
    no_preferences = UserProfile()

    # Out-of-range targets: energy/acousticness targets outside the natural
    # [0, 1] range of the data, and a wildly unrealistic tempo. Since the
    # scorer does raw (target - actual) with no clamping, this should still
    # produce a valid (if inflated) score rather than breaking anything.
    extreme_values = UserProfile(
        favorite_genre="pop",
        target_energy=5.0,
        target_bpm=999,
        target_acousticness=-3.0,
    )

    # Preferences that don't exist anywhere in the dataset. Every categorical
    # field should mismatch (fixed 0.2 error each) for every song, so this
    # profile's "best" recommendations are really just tie-breaks decided by
    # the numeric fields we didn't set (all None here, so score should be 0
    # from those and driven purely by the categorical mismatches).
    nonexistent_taste = UserProfile(
        favorite_genre="polka",
        favorite_artist="Nonexistent Artist",
        favorite_mood="apathetic",
    )

    adversarial_cases = (
        ("Conflicting signals (sad mood + high energy/valence/danceability)", conflicting_signals),
        ("No preferences specified", no_preferences),
        ("Extreme/out-of-range targets", extreme_values),
        ("Genre/artist/mood not present in dataset", nonexistent_taste),
    )

    for label, profile in adversarial_cases:
        print_recommendations(label, profile, songs)
"""

if __name__ == "__main__":
    main()
