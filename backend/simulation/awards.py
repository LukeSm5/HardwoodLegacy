# Awards.py
# Define awards
# Help determine award winners based on player stats and team performance
# Awards
# National:
    # All-American Teams
    # National Player of the Year
    # Coach of the Year
    # Top Center (Kareem Abdul-Jabbar)
    # Top Point Guard (Bob Cousy)
    # Top Small Forward (Julius Erving)
    # Top Shooting Guard (Jerry West)
    # Top Power Forward (Karl Malone)
    # National Tournament MOP
    # National Tournament All-Tournament Team
    # NIT Tournament MOP
# Conference:
    # Conference Player of the Year
    # Conference Defensive Player of the Year
    # All-Conference Teams
    # Conference Coach of the Year
    # Conference Freshman of the Year
    # All Conference Freshman Teams
    # Conference Rookie of the Year
    # Conference 6th Man of the Year
    # Conference Tournament MVP
    # Conference Tournament All-Tournament Team

NATIONAL_AWARDS = {
    "player_of_year": {
        "name": "National Player of the Year",
        "trophy_name": "Golden Award",
        "criteria": {
            "min_games": 25,
            "stat_weights": {
                "points": 0.45,
                "assists": 0.2,
                "rebounds": 0.15,
                "steals": 0.1,
                "blocks": 0.1
            },
            "bonus_factors": {
                "team_success": 0.1,
                "schedule_strength": 0.05
            }
        },
        "num_winners": 1
    }, "defensive_player_of_year": {
        "name": "National Defensive Player of the Year",
        "trophy_name": "Leonard Award",
        "criteria": {
            "min_games": 25,
            "stat_weights": {
                "steals": 0.4,
                "blocks": 0.4,
                "assists": 0.2
            },
            "bonus_factors": {
                "team_success": 0.1,
                "schedule_strength": 0.05
            }
        },
        "num_winners": 1
    }, "coach_of_year": {
        "name": "National Coach of the Year",
        "trophy_name": "Coach's Trophy",
        "criteria": {
            "min_games": 25,
            "stat_weights": {
                "win_percentage": 0.6,
                "team_improvement": 0.4
            },
            "bonus_factors": {
                "team_success": 0.1,
                "schedule_strength": 0.05
            }
        },
        "num_winners": 1
    }, "first_team_all_american": {

    }, "second_team_all_american": {

    }, "third_team_all_american": {
    }
}
CONFERENCE_AWARDS = {}
POSITION_AWARDS = {
    "point_guard": {},
    "shooting_guard": {},
    "small_forward": {},
    "power_forward": {},
    "center": {}
}
TOURNAMENT_AWARDS = {}

def determine_awards(): 
    pass
