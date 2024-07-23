import streamlit as st
import pandas as pd

st.title("Building a Winning NBA Roster")

df_teams = pd.read_csv("../../data/interim/NBA_team_stats_1979-2024_clean.csv")

teams = df_teams['Team']

draftable_players = pd.read_csv("../../data/interim/draft_prospects.csv", encoding='ISO-8859-1')


# Select a team
st.subheader("Teams")
team = st.selectbox("Select a team:", teams)

# Display draftable players
st.subheader("Draftable Players")
selected_draftable_players = st.multiselect("Select players to draft from draftable players:", draftable_players)

st.subheader("Top Picks")
# Display selected players
if selected_draftable_players:
    st.subheader(f"{team} Drafted Players")
    for player in selected_draftable_players:
        st.write(player)
else:
    st.write("No players selected yet.")