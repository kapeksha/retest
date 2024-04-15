'''
Suppose there is a sports tournament, and you have a dictionary representing the current points of teams in the tournament. Each team is represented by its name (a string) and its points (an integer). Write a Python program to perform the following tasks:
- Implement a function 'add_team' which takes the team's name and points as an input and adds it to the dictionary if it doesn't exist.
- Implement a function 'remove_team' which takes the team's name as input and
deletes it from the dictionary if it exists. - Implement a function 'update points' which takes existing team's names and points as input and updates it to the dictionary.
- Implement a function 'get_top_teams' which takes n as an input and gives top n teams from the dictionary.
- Implement a function 'write_to_file' that takes the dictionary and a filename as input and writes the information to the given filename in the format: "Team: Points".
Example:
('Team1': 120, 'Team2': 150, Team3': 170, Team4': 140, Team5': 200)
'''



class Tournament:
    def __init__(self):
        self.teams = {}

    def add_team(self, tname, points):
        if tname not in self.teams:
            self.teams[tname] = points
        else:
            print("already exists!")

    def remove_team(self, tname):
        if tname in self.teams:
            del self.teams[tname]
        else:
            print("does not exist")

    def update_points(self, tname, points):
        if tname in self.teams:
            self.teams[tname] = points
        else:
            print("does not exist")

    def top_teams(self, n):
        sorted_teams = sorted(self.teams.items(), key=lambda x: x[1], reverse=True)
        return sorted_teams[:n]

    def write_file(self, filename):
        with open(filename, "w") as file:
            for team, points in self.teams.items():
                file.write(f"{team}: {points}\n")


tournament = Tournament()

while True:
    print("1. Add Team")
    print("2. Remove Team")
    print("3. Update Points")
    print("4. Get Top Teams")
    print("5. Write to File")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        tname = input("Enter team name: ")
        points = int(input("Enter points: "))
        tournament.add_team(tname, points)
        print("Team added.")

    elif choice == 2:
        tname = input("Enter team name to remove: ")
        tournament.remove_team(tname)
        print("Team removed.")

    elif choice == 3:
        tname = input("Enter team name to update: ")
        points = int(input("Enter new points: "))
        tournament.update_points(tname, points)
        print("Points updated.")

    elif choice == 4:
        n = int(input("Enter number of top teams to display: "))
        top_teams = tournament.top_teams(n)
        print(f"Top {n} teams:")
        for team, points in top_teams:
            print(f"{team}: {points}")

    elif choice == 5:
        filename = input("Enter filename to write to: ")
        tournament.write_file(filename)
        print(f"Team information written to '{filename}'")

    elif choice == 6:
        print("Exiting!!")
        break

    else:
        print("Invalid choice!!")


