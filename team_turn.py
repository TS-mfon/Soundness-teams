import datetime

TEAMS = ["Zippy", "Bloop", "Blu", "Wava", "Echo"]
BASE_DATE = datetime.date(2025, 9, 8)
BASE_TEAM_INDEX = 3  # Wava

def get_team_of_the_day():
    today = datetime.date.today()
    delta_days = (today - BASE_DATE).days
    current_team_index = (BASE_TEAM_INDEX + delta_days) % len(TEAMS)
    return TEAMS[current_team_index]

def get_next_turn_date(team_name):
    if team_name not in TEAMS:
        return None

    today = datetime.date.today()
    
    target_team_index = TEAMS.index(team_name)

    delta_days = (today - BASE_DATE).days
    current_team_index = (BASE_TEAM_INDEX + delta_days) % len(TEAMS)
    
    days_until_turn = (target_team_index - current_team_index + len(TEAMS)) % len(TEAMS)
    
    next_turn_date = today + datetime.timedelta(days=days_until_turn)
    return next_turn_date

if __name__ == "__main__":
    print(f"Today's team is: {get_team_of_the_day()}")

    try:
        team_name_input = input("Enter a team name to find their next turn: ").strip()
        
        next_date = get_next_turn_date(team_name_input)
        
        if next_date:
            day_name = next_date.strftime('%A')
            if next_date == datetime.date.today():
                print(f"It's {team_name_input}'s turn today, {day_name}!")
            else:
                print(f"{team_name_input}'s next turn is on {day_name}, {next_date.strftime('%Y-%m-%d')}.")
        else:
            print(f"Team '{team_name_input}' not found. Available teams are: {', '.join(TEAMS)}")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")