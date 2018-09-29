import requests
from bs4 import BeautifulSoup
import threading
from prettytable import PrettyTable
import time

start_time = time.time()

allowed_teams = ['afghanistan', 'australia', 'bangladesh', 'england', 'india', 'ireland', 'new zealand',
                 'pakistan', 'south africa', 'sri lanka', 'west indies', 'zimbabwe', 'nepal', 'netherlands',
                 'scotland', 'united arab emirates', 'hong kong', 'oman', 'bermuda', 'swwitzerland',
                 'east africa', 'west africa', 'cuba', 'windies']

def search_for_internnational_series(year, input_team):
    url = "https://www.cricbuzz.com/cricket-scorecard-archives/" + year

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find('div', class_="cb-col-84 cb-col")

    data = data.find_all('a')

    international_series = [data[i]['href'] for i in range(len(data))]

    check_for_bilateral_or_tournament(international_series, input_team)


def check_for_bilateral_or_tournament(international_series, input_team):
    for url in international_series:
        new_url = "https://www.cricbuzz.com" + str(url[:-7]) + "squads"
        page = requests.get(new_url)
        soup = BeautifulSoup(page.content, "html.parser")
        data = soup.find('div', class_="list-group cb-list-group")

        data = data.find_all('a')

        teams = []
        for i in range(len(data)):
            if str(url[:-7]) in data[i]['href']:
                team = data[i].find('h3').contents[0]
                if team.lower() in allowed_teams:
                    teams.append(team.lower())

        calculate_win_or_loss(teams, input_team, url)


def calculate_win_or_loss(teams, input_team, url):
    win_count, losses_count, drawn_count, tie_count = 0, 0, 0, 0
    if input_team in teams and len(teams)==2:
        result_url = "https://www.cricbuzz.com" + str(url)
        page = requests.get(result_url)
        soup = BeautifulSoup(page.content, "html.parser")
        data = soup.find('div', class_="cb-bg-white cb-col-100 cb-col cb-hm-rght")

        data = data.find_all("a", class_="cb-text-link")

        for i in range(len(data)):
            print(data[i].contents[0].lower())
            if input_team in data[i].contents[0].lower():
                win_count+=1
            elif data[i].contents[0].lower()=="match drawn":
                drawn_count+=1
            elif data[i].contents[0].lower()=="match tied":
                tie_count+=1
            else:
                losses_count+=1

        print(data)
        print(win_count, losses_count, drawn_count, tie_count)

print("Enter the year- ")
year = input()
print("Enter the Team- ")
input_team = input()

input_team = input_team.lower() # Convert it into Lower Case to handle exceptions.

search_for_internnational_series(year, input_team)

end_time = time.time()

print(end_time - start_time)

