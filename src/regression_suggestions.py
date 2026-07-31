"""
Interactive entry point for the Regression Suggestions system.

Prompts the listener for a free-text description of their taste, parses it
into a UserProfile via src/parse_preferences.py's structured-prompting (LLM)
extraction, and prints the top 10 best-matching songs from the catalog along
with LLM-generated explanations (src/explain.py).

Run with: python -m src.regression_suggestions
"""

from src.recommender import load_songs, recommend_songs, UserProfile
from src.explain import generate_explanation
from src.parse_preferences import parse_preferences


def get_user_profile() -> UserProfile:
    description = input(
        "Describe your music taste (mood, genre, artists, energy, etc.): "
    ).strip()

    if not description:
        return UserProfile()

    profile = parse_preferences(description)
    if profile is None:
        print(
            "\nCouldn't parse that into preferences (no API key, network "
            "issue, etc.) — showing generic recommendations instead."
        )
        return UserProfile()
    return profile


def print_top_recommendations(profile: UserProfile, songs: list, k: int = 10) -> None:
    recommendations = recommend_songs(
        profile, songs, k=k, explain_fn=generate_explanation
    )

    print(f"\n=== Top {len(recommendations)} recommendations ===\n")
    for song, score, explanation in recommendations:
        print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv", "data/ai_songs.csv")
    profile = get_user_profile()
    print_top_recommendations(profile, songs)


if __name__ == "__main__":
    main()
