import copy

import constants

# Save player height as int, experience as True/False, guardians as list of str.
# Append clean_players to new list
def clean_data():
    cleaned_players = []
    for player in constants.PLAYERS:
        clean_player = copy.deepcopy(player)
        clean_player['height'] = int(player['height'].split()[0])
        if clean_player['experience'] == 'YES':
            clean_player['experience'] = True
        else:
            clean_player['experience'] = False
        clean_player['guardians'] = clean_player['guardians'].split(' and ')    
        cleaned_players.append(clean_player)
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

            
#TODO: Assign players equally to the 3 teams, ensure that teams have equal num experieneced players
def balance_teams():
    teams = {team: [] for team in copy.deepcopy(constants.TEAMS)}
    num_teams = len(teams)
    num_experienced_players = len(experienced_players)
    num_inexperienced_players = len(inexperienced_players)
    for team in teams:
        for experienced_players in range(num_experienced_players):
            teams[team].append(experienced_players.pop(0))
    
        return teams


#TODO: Create a function to find the average height of each team
