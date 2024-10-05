import copy

import constants

# Save player height as int, experience as True/False, guardians as list of str.
# Append clean_players to new list
def clean_data():
    players = copy.deepcopy(constants.PLAYERS)
    cleaned_players = []
    
    for player in players:
        player['height'] = int(player['height'].split()[0])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
            
        player['guardians'] = player['guardians'].split(' and ')    
        cleaned_players.append(player)
        
    return cleaned_players


#Sort cleaned_players based on experience, return lists
def sort_players_by_experience():
    experienced_players = []
    inexperienced_players = []

    for player in cleaned_players:
        if player['experience'] == True:
            experienced_players.append(player)
        elif player['experience'] == False:
            inexperienced_players.append(player)
            
    return experienced_players, inexperienced_players

            
# Assign players equally to the 3 teams, ensure that teams have equal num experieneced players
def balance_teams(experienced_players, inexperienced_players):
    teams = copy.deepcopy(constants.TEAMS)

    # Calculate players per team
    experienced_per_team = len(experienced_players) // len(teams)
    inexperienced_per_team = len(inexperienced_players) // len(teams)

    # Initialize team names
    team_names = ["Panthers", "Bandits", "Warriors"]

    # Round-robin assignment of experienced players using dictionary comprehension
    team_rosters = {team: [] for team in team_names}

    team_rosters = {team: [experienced_players[i] for i in range(len(experienced_players)) if i % len(team_names) == idx]
                    for idx, team in enumerate(team_names)}

    # Round-robin assignment of inexperienced players
    for idx, player in enumerate(inexperienced_players):
        team_name = team_names[idx % len(teams)]
        team_rosters[team_name].append(player)

    return team_rosters["Panthers"], team_rosters["Bandits"], team_rosters["Warriors"]

    
#TODO: Create a function to find the average height of each team
def average_height(team_rosters):
    


