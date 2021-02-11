Chess.com Game Downloader

For competitive chess players, reviewing your games is instrumental in determining your weaknesses. Chess.com is the most popular server for playing chess, featuring the strongest competition. 

With the onset of the pandemic, practically all play shifted online, dramatically increasing the importance of online play and subsequently the studying of your online games. Chess.com's functionality for exporting your games allows you to download only 50 games at a time. Competitive players typically have thousands if not tens of thousands of games played, necessitating a faster method.

The script scrapes the Chess.com API to get a user's games in JSON format and load each game into a Pandas DataFrame, from where the games can be filtered (i.e. filtering out games played with non-standard rules). The output is a .pgn file, a text file that can be opened in chess software to play through games.

For demonstrative purposes, the Chess.com games of the World Champion Magnus Carlsen are included.

My future ambitions for this project are to implement some form of data visualization to show a user's openings (i.e. the first dozen or so moves of any game) and their score in each opening, allowing for a player to determine the areas they should focus on improving. Such a feature would cut down on the time a player would have to spend looking through thousands of games and immediately give them a clear target to work on.
