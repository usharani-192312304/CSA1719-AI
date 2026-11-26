
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-item rating data
data = {
    'Movie1': [5, 4, 0, 0],
    'Movie2': [4, 5, 0, 0],
    'Movie3': [0, 0, 5, 4],
    'Movie4': [0, 0, 4, 5]
}

# Create rating matrix
ratings = pd.DataFrame(
    data,
    index=['User1', 'User2', 'User3', 'User4']
)

# Calculate user similarity
similarity = cosine_similarity(ratings)

similarity_df = pd.DataFrame(
    similarity,
    index=ratings.index,
    columns=ratings.index
)

# Recommend movies for User1
user = 'User1'

scores = similarity_df.loc[user] @ ratings
scores = scores / similarity_df.loc[user].sum()

# Remove already rated movies
scores = scores[ratings.loc[user] == 0]

# Display recommendation
print("Recommendation for", user)
print("Recommended Movie:", scores.idxmax())
