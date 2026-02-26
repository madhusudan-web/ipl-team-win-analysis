import pandas as pd
import matplotlib.pyplot as plt


file_path = "ipl_matches_100.csv"  
df = pd.read_csv("C:/Users/Madhu/Downloads/ipl_matches_100.csv")


print("Columns:", df.columns)


winner_col = "match_winner"


team_wins = df[winner_col].value_counts()


print("\nMost Successful Teams:")
print(team_wins)


plt.figure()
team_wins.plot(kind='bar')
plt.title("Most Successful Teams (Wins)")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.show()