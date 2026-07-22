standings = {
    "ARG": {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "GD": 0, "Pts": 0},
    "MEX": {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "GD": 0, "Pts": 0},
    "POL": {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "GD": 0, "Pts": 0},
    "KSA": {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "GD": 0, "Pts": 0},
}


def process_match(standings, team1, team2, team1_goals, team2_goals):
    team1["P"] += 1
    team2["P"] += 1
    team1["GF"] += team1_goals
    team2["GA"] += team1_goals
    team2["GF"] += team2_goals
    team1["GA"] += team2_goals
    if team1_goals > team2_goals:
        team1["Pts"] += 3
        team1["W"] += 1
        team2["L"] += 1

    elif team1_goals == team2_goals:
        team1["Pts"] += 1
        team2["Pts"] += 1
        team1["D"] += 1
        team2["D"] += 1

    else:
        team2["Pts"] += 3
        team2["W"] += 1
        team1["L"] += 1

    team1["GD"] = team1["GF"] - team1["GA"]
    team2["GD"] = team2["GF"] - team2["GA"]


def print_standings(standings):

    sorted_teams = sorted(
        standings.items(),
        key=lambda item: (item[1]["Pts"], item[1]["GD"], item[1]["GF"]),
        reverse=True,
    )

    print(
        f"{'Team':<5} {'P':>2} {'W':>2} {'D':>2} {'L':>2} {'GF':>3} {'GA':>3} {'GD':>4} {'Pts':>4}"
    )
    for team, stats in sorted_teams:

        if stats["GD"] > 0:
            gd = f"+{stats['GD']}"
        else:
            gd = str(stats["GD"])

        print(
            f"{team:<5} "
            f"{stats['P']:>2} "
            f"{stats['W']:>2} "
            f"{stats['D']:>2} "
            f"{stats['L']:>2} "
            f"{stats['GF']:>3} "
            f"{stats['GA']:>3} "
            f"{gd:>4} "
            f"{stats['Pts']:>4}"
        )


matches = [
    ("ARG", "MEX"),
    ("ARG", "POL"),
    ("ARG", "KSA"),
    ("MEX", "POL"),
    ("MEX", "KSA"),
    ("POL", "KSA"),
]

for t1, t2 in matches:
    while True:
        result = input(f"Enter score for {t1} vs {t2} (format: 2-0): ")
        try:
            f_result = result.split("-")
            team1_goals = int(f_result[0])
            team2_goals = int(f_result[1])
            break
        except ValueError:
            print("Invalid input! Please enter the score like 2-0.")
    process_match(standings, standings[t1], standings[t2], team1_goals, team2_goals)

print_standings(standings)
