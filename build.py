from src.data import load, clean

data_dir = 'data'
external_dir = f'{data_dir}/external'
interim_dir = f'{data_dir}/interim'
processed_dir = f'{data_dir}/processed'

# Scraping team data From Stathead
load.scrape_stathead_teams(external_dir)

# Downloading player datasets from Kaggle
load.download_kaggle_set('wyattowalsh/basketball', external_dir, 'kaggle1')
load.download_kaggle_set('sumitrodatta/nba-aba-baa-stats', external_dir, 'kaggle2')

# Scraping player data from Stathead
player_query = "https://stathead.com/basketball/player-season-finder.cgi?request=1&year_min=2001&year_max=2024&display_type=per_g&ccomp%5B2%5D=gt&cval%5B2%5D=8&cstat%5B2%5D=mp_per_g"
all_star_query = "https://stathead.com/basketball/player-season-finder.cgi?request=1&year_min=2001&year_max=2024&display_type=per_g&as_selections_type=Y"
college_query = "https://stathead.com/basketball/cbb/player-season-finder.cgi?request=1&order_by=pts_per_g&year_min=2001&year_max=2024&comp_id=NCAAM&team_success=ncaa_made&draft_status=drafted&draft_pick_type=overall"
load.scrape_stathead_knn_stats(external_dir, player_query, 10000, "all_player_stats.csv")
load.scrape_stathead_knn_stats(external_dir, all_star_query, 600, "allstar_stats.csv")
load.scrape_stathead_knn_stats(external_dir, college_query, 1600, "college_player_stats.csv")

# Combine kaggle data into single player dataset
clean.process_player_data_long(kaggle1_dir='data/external/kaggle1',
                               kaggle2_dir='data/external/kaggle2',
                               output_dir=interim_dir)

# Cleaning team stats
clean.clean_team_stats('data/external/team_stats.csv',
                       processed_dir)

# Cleaning aggregated player stats
clean.clean_player_data_long('data/interim/player_data_long_aggregated.csv',
                             processed_dir)
