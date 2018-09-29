# signzy_hiring_challenge
Cricket Record Search


## Getting started with development
Dependencies:
- Python 3.6.x
- Any Opearting System.

### 1. Clone this repository
```bash
git clone https://github.com/vishuvish/signzy_hiring_challenge.git
# in the cloned directory goto signzy_hiring_challenge directory i.e.
cd signzy_hiring_challenge
```

### 2. Install python packages
pip install -r requirements.txt

### 3. Run the programm
```bash
## Steps-
1. Open the Terminal
2. # in the cloned directory goto signzy_hiring_challenge directory i.e.
cd signzy_hiring_challenge
3. Type - python cricket_record_search.py (Windows User)
   Type - python3 cricket_record_search.py (Linux & IOS User)
4. Input the year and the nation. Make sure not to use abbreviated form of the nation.
```

## Work Flow-

1. As soon as the user run the program.
2. [Line Number - 121](https://github.com/vishuvish/signzy_hiring_challenge/blob/c93f02e5070dc5bb68fe7b9fc532a9820a1df4a0/cricket_record_search.py#L121) executes and it will call the [main function](https://github.com/vishuvish/signzy_hiring_challenge/blob/c93f02e5070dc5bb68fe7b9fc532a9820a1df4a0/cricket_record_search.py#L82). 
3. As the main function executes, the program asks for users input (year and team).
4. Checks for the correctness of the user input.
5. If the user input is within the specified range, then the program will call the function [search_for_international_series](https://github.com/vishuvish/signzy_hiring_challenge/blob/c93f02e5070dc5bb68fe7b9fc532a9820a1df4a0/cricket_record_search.py#L17) . This function will scrape the International Series from the [Cricbuzz Archive Page](https://www.cricbuzz.com/cricket-scorecard-archives/) . 
6. Then the list of all the international series is returned and the main function will creates 4 threads and calls the [check_for_bilateral_or_tournament](https://github.com/vishuvish/signzy_hiring_challenge/blob/c93f02e5070dc5bb68fe7b9fc532a9820a1df4a0/cricket_record_search.py#L31)
7. And then checks whether the series is bilateral or tourament. To check that it will scrape the [squads](https://www.cricbuzz.com/cricket-series/2489/england-tour-of-india-2016-17/squads) page.
8. If there is only 2 teams in the series. Then it will scrape the [schedule and results](https://www.cricbuzz.com/cricket-series/2489/england-tour-of-india-2016-17/matches) page.
9. Then calculate the total number of wins, losses, draws and ties of the team in the specified year.
10. At the end, [table](https://github.com/vishuvish/signzy_hiring_challenge/blob/c93f02e5070dc5bb68fe7b9fc532a9820a1df4a0/cricket_record_search.py#L74) fun will run which will convert the records of the team in the specified year into tabular form.