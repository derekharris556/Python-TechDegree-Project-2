import copy
import sys
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
def sort_players_by_experience(cleaned_players):
    experienced_players = []
    inexperienced_players = []
    for player in cleaned_players:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
            
    return experienced_players, inexperienced_players


# Assign experienced & inexperienced players equally to 3 teams
def balance_teams(experienced_players, inexperienced_players):
    teams = copy.deepcopy(constants.TEAMS)
    # Calculate players per team
    experienced_per_team = len(experienced_players) // len(teams)
    inexperienced_per_team = len(inexperienced_players) // len(teams)
    # Initialize team names
    team_names = ["Panthers", "Bandits", "Warriors"]
    # Alternating assignment of experienced players using dictionary comprehension
    team_rosters = {team: [] for team in team_names}
    team_rosters = {
        team: [
            experienced_players[i] 
            for i in range(len(experienced_players))
            if i % len(team_names) == idx
            ]
            for idx, team in enumerate(team_names)
            }
    # Alternating assignment of inexperienced players
    for idx, player in enumerate(inexperienced_players):
        team_name = team_names[idx % len(teams)]
        team_rosters[team_name].append(player)

    return team_rosters["Panthers"], team_rosters["Bandits"], team_rosters["Warriors"]


# Create a function for printing all team details when user selects a team
# Lay out the team details in a manner that is easy to read in the console
def display_team_details(team_name, team_roster):
    print()
    print("*" + ("-" * 33) + "*")
    print(f'{team_name.capitalize()}:\n')
    # Calculate total number of players and assign to num_players
    num_players = len(team_roster)
    # Print total number of players
    print(f'# of Players: {num_players}\n')
    # Calculate total number of experienced players and assign to num_experienced
    num_experienced = sum(player['experience'] for player in team_roster)
    # Print total number of experienced players for given team
    print(f'# of Experienced Players: {num_experienced}\n')
    # Calculate total number of inexperienced players and assign to num_inexperienced
    num_inexperienced = sum(not player['experience'] for player in team_roster)
    # Print total number of inexperienced players for given team
    print(f'# of Experience Players: {num_inexperienced}\n')
    # Avg height of all players (sum of player heights divided by # of players)
    avg_height = round(sum(player['height'] for player in team_roster) / num_players, 2)
    # Print average height for given team
    print(f'Average Height: {avg_height} inches\n')
    # Print names of all players on the team as a comma-separated string
    player_names = [player['name'] for player in team_roster]
    print("Players: ", ", ".join(player_names))
    print()
    # Print names of all guardians as string separated by commas
    guardian_names = [guardian for player in team_roster for guardian in player['guardians']]
    print("Guardians:", ", ".join(guardian_names))
    print()
    print("*" + ("-" * 33) + "*")


# Main menu to display team details based on user input or quit program
def main_menu(panthers, bandits, warriors):
    print()
    print("*---Treehouse Basketball League---*\n")
    print("Enter a team's corresponding # to view that team's roster:\n")
    print("1. Panthers\n2. Bandits\n3. Warriors\n")
    print("Press 'q' to quit.\n")

    while True:
        try:
            user_choice = input("Please make a selection: ").strip()
            if user_choice.lower() == 'q':
                print("\nGoodbye!")
                sys.exit()
            elif int(user_choice) == 1:
                display_team_details("Panthers", panthers)
                if return_to_main_menu():
                    main_menu(panthers, bandits, warriors)
            elif int(user_choice) == 2:
                display_team_details("Bandits", bandits)
                if return_to_main_menu():
                    main_menu(panthers, bandits, warriors)
            elif int(user_choice) == 3:
                display_team_details("Warriors", warriors)
                if return_to_main_menu():
                    main_menu(panthers, bandits, warriors)
        except ValueError:
            print("Invalid input. Valid Options: 1, 2, 3, or 'q'.")      


# Create func to return user to main_menu
def return_to_main_menu():
    print('\nPress ENTER to return to main menu.')
    while True:
        return_to_main_menu = input("").strip()
        # If user presses ENTER, func returns TRUE and returns to main menu
        if return_to_main_menu == "":
            return True
        else:
            print('Invalid input. Press ENTER to return to main menu.')


def main():
    # Call to clean the player data
    cleaned_players = clean_data()
    # Separate experienced and inexperienced players
    experienced, inexperienced = sort_players_by_experience(cleaned_players)
    # Balance the teams and capture the results
    panthers, bandits, warriors = balance_teams(experienced, inexperienced)
    # Call main_menu func & set sa loop so program runs until user quits
    while True:
        main_menu(panthers, bandits, warriors)




# main function called within dunder main
if __name__ == "__main__":
    main()