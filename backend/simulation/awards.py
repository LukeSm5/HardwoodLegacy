# Awards.py
# Define awards
# Help determine award winners based on player stats and team performance
GUARD_WEIGHTS = {"points": 0.45, "assists": 0.25, "rebounds": 0.10, "steals": 0.15, "blocks": 0.05}
WING_WEIGHTS  = {"points": 0.40, "assists": 0.20, "rebounds": 0.20, "steals": 0.10, "blocks": 0.10}
BIG_WEIGHTS   = {"points": 0.45, "assists": 0.10, "rebounds": 0.25, "steals": 0.05, "blocks": 0.15}
GENERAL_WEIGHTS = {"points": 0.45, "assists": 0.20, "rebounds": 0.15, "steals": 0.10, "blocks": 0.10}
DEFENSIVE_WEIGHTS = {"steals": 0.40, "blocks": 0.40, "assists": 0.20}

BONUS_FACTORS = {"team_success": 0.10, "schedule_strength": 0.05}

ALL_AMERICAN_TEAMS = {
    f"{tier}_team_all_american": {
        "name": f"{tier.title()} Team All-American",
        "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS},
        "num_winners": 5,
    }
    for tier in ["first", "second", "third"]
}

NATIONAL_AWARDS = {
    "player_of_year":          {"name": "National Player of the Year",         "trophy_name": "Golden Award",   "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS,  "bonus_factors": BONUS_FACTORS}, "num_winners": 1},
    "defensive_player_of_year":{"name": "National Defensive Player of the Year","trophy_name": "Leonard Award",  "criteria": {"min_games": 25, "stat_weights": DEFENSIVE_WEIGHTS,"bonus_factors": BONUS_FACTORS}, "num_winners": 1},
    "coach_of_year":           {"name": "National Coach of the Year",           "trophy_name": "Coach's Trophy", "criteria": {"stat_weights": {"win_percentage": 0.70, "team_improvement": 0.30}, "bonus_factors": BONUS_FACTORS}, "num_winners": 1},
    **ALL_AMERICAN_TEAMS,
}

POSITION_AWARDS = {
    "point_guard":    {"name": "Top Point Guard",    "trophy_name": "Cousy Award",  "criteria": {"min_games": 20, "stat_weights": GUARD_WEIGHTS}, "num_winners": 1},
    "shooting_guard": {"name": "Top Shooting Guard", "trophy_name": "West Award",   "criteria": {"min_games": 20, "stat_weights": {**GUARD_WEIGHTS, "points": 0.50, "assists": 0.15}}, "num_winners": 1},
    "small_forward":  {"name": "Top Small Forward",  "trophy_name": "Erving Award", "criteria": {"min_games": 20, "stat_weights": WING_WEIGHTS}, "num_winners": 1},
    "power_forward":  {"name": "Top Power Forward",  "trophy_name": "Malone Award", "criteria": {"min_games": 20, "stat_weights": {**BIG_WEIGHTS,  "assists": 0.15, "rebounds": 0.20}}, "num_winners": 1},
    "center":         {"name": "Top Center",         "trophy_name": "Alcindor Award",   "criteria": {"min_games": 20, "stat_weights": BIG_WEIGHTS}, "num_winners": 1},
}
CONFERENCE_AWARDS = {
    "conference_player_of_year":{"name": "Conference Player of the Year", "trophy_name": "Conference Player of the Year", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS, "bonus_factors": BONUS_FACTORS}, "num_winners": 1},
    "conference_defensive_player_of_year":{"name": "Conference Defensive Player of the Year", "trophy_name": "Conference Defensive Player of the Year Trophy", "criteria": {"min_games": 25, "stat_weights": DEFENSIVE_WEIGHTS, "bonus_factors": BONUS_FACTORS}, "num_winners": 1},
    "conference_freshman_of_year": {"name": "Conference Freshman of the Year", "trophy_name": "Conference Freshman of the Year Trophy", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 1},
    "coach_of_year": {"name": "Conference Coach of the Year", "trophy_name": "Conference Coach's Trophy", "criteria": {"stat_weights": {"win_percentage": 0.70, "team_improvement": 0.30}, "bonus_factors": BONUS_FACTORS}, "num_winners": 1},
    "first_team_all_conference_team": {"name": "All-Conference Team", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 5},
    "second_team_all_conference_team": {"name": "All-Conference Team", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 5},
    "rookie_of_the_year": {"name": "Conference Rookie of the Year", "trophy_name": "Conference Rookie of the Year Trophy", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 1},
    "sixth_man_of_the_year": {"name": "Conference Sixth Man of the Year", "trophy_name": "Conference Sixth Man of the Year Trophy", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 1},
    "first_team_all_freshman_team": {"name": "All-Freshman Team", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 5},
    "second_team_all_freshman_team": {"name": "All-Freshman Team", "criteria": {"min_games": 20, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 5},
}
TOURNAMENT_AWARDS = {
    "national_tournament_mop": {"name": "National Tournament Most Outstanding Player", "trophy_name": "Final Four Most Outstanding Player Trophy", "criteria": {"min_games": 5, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 1},
    "nit_tournament_mop": {"name": "NIT Tournament Most Outstanding Player", "trophy_name": "NIT Most Outstanding Player Trophy", "criteria": {"min_games": 3, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 1},
    "all_tournament_team": {"name": "National Tournament All-Tournament Team", "criteria": {"min_games": 3, "stat_weights": GENERAL_WEIGHTS}, "num_winners": 5},
    "conference_tournament_mvp": {"name": "Conference Tournament MVP", "criteria": { "stat_weights": GENERAL_WEIGHTS}, "num_winners": 1},
    "conference_all_tournament_team": {"name": "Conference All-Tournament Team", "criteria": {"stat_weights": GENERAL_WEIGHTS}, "num_winners": 5},
}

def calculate_player_of_year_score(player_stats) -> float:
    pass

def calculate_defensive_player_score(player_stats) -> float:
    pass

def calculate_coach_of_year_score(team_stats, preseason_expectations) -> float:
    pass

def select_all_conference_teams(player_stats, conference, num_teams=3) -> dict:
    pass

def select_all_american_teams(player_stats, num_teams=3) -> dict:
    pass

def select_tournament_mop(game_stats, tournament_type) -> player:
    pass

def determine_award_winners(player_stats, team_stats, conference, tournament_stats, preseason_expectations) -> dict:
    pass