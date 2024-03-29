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

global win_count, losses_count, drawn_count, tie_count
win_count, losses_count, drawn_count, tie_count = 0, 0, 0, 0

def search_for_international_series(year):
    url = "https://www.cricbuzz.com/cricket-scorecard-archives/" + year

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find('div', class_="cb-col-84 cb-col")

    data = data.find_all('a')

    international_series = [data[i]['href'] for i in range(len(data))]

    return international_series


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
    global win_count, losses_count, drawn_count, tie_count
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

        # print(data)
        # print(win_count, losses_count, drawn_count, tie_count)

def table(input_team, year):
    columns = ["Team", "Year", "Wins", "Losses", "Draws", "Tie"]
    relation = PrettyTable(columns)
    relation.add_row([input_team, year, win_count, losses_count, drawn_count, tie_count])

    return relation


def main():
    print("Enter the year- ")
    year = input()
    print("Enter the Team- ")
    input_team = input()

    input_team = input_team.lower()  # Convert it into Lower Case to handle exceptions.

    if 1900<=int(year)<=2018:
        if input_team in allowed_teams:
            print("Wait while the program is scraping Cricbuzz.")
        else:
            print("No data Found")
            return 1
    else:
        print("Please Enter the year between 1900 to 2018.")
        return 1

    series = search_for_international_series(year)

    thread_1 = threading.Thread(target=check_for_bilateral_or_tournament, args=(series[:len(series)//4], input_team))
    thread_2 = threading.Thread(target=check_for_bilateral_or_tournament, args=(series[len(series)//4 + 1:2*len(series)//4], input_team))
    thread_3 = threading.Thread(target=check_for_bilateral_or_tournament, args=(series[2*len(series)//4 + 1:3*len(series)//4], input_team))
    thread_4 = threading.Thread(target=check_for_bilateral_or_tournament, args=(series[3*len(series)//4 + 1:], input_team))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    if not thread_1.isAlive() and not thread_2.isAlive() and not thread_3.isAlive() and not thread_4.isAlive():
        print(table(input_team, year))


if __name__ == '__main__':
    main()

