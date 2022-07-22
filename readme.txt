The NBA top scorers project analyzes NBA data from years 1950 - 2017 using csv data files from www.kaggle.com. 
Data web link location: https://www.kaggle.com/datasets/drgilermo/nba-players-stats
There are 3 data files available. The "Seasons_Stats.csv" file will be used for this project.
This projects analyzes the top NBA scores from 1950 - 2017 and creates visual scatter plot graphs displaying
the top scores for all seasons combined 1950 - 2017 and the top 2 scores for each season 1950 - 2017.
The first graph displays a scatter plot of the top scores for all players in seasons 1950 - 2017.
The second graph displays a scatter plot of the top scores for each season 1950 - 2017.
The third graph displays a scatter plot of the runner up (2nd) top scores for each season 1950 - 2017.

The project is organized in a Jupiter notebook using Python version 3.9.12. The Anaconda application 
should be installed to run this analysis so that the pandas, matplotlib, numpy, and seaborn libraries 
can be utilized.

Project features:

1. - A csv file is read into a dataframe for analysis ("Seasons_Stats.csv" from kaggle.com).
   - The data frame of player demographics is put into a library.

2. - Nan and null values are removed from the data. Also columns with statistics that will not be 
     used in this analysis, are removed.
   - The data is put into a condensed frame that focuses on player demographics including player name, 
     team played, season year, point scored during that year, position, and age.

3. - Total player count, mean age, youngest age, oldest age, maximum points scored, minimum points scored
     and age / point at 25%, 50%, and %75 points in the data analysis.
   - Functions are used to organize the players in the data by season and top scorers for each season. 
     A function also sort and creates new data list with the top and runner-up (2nd) top scorer for each 
     season.

4. - Three graphs are created from the analyzed data. The first graph shows the top scores for all
     seasons, 1950- 2017. The second graph shows the top scores for each season, 1950 - 2017. The third graph 
     shows the runner up top score for each season, 1950 - 2017.

5. - The project was built using a Jupiter notebook. Jupiter can be installed by going to the 
     site https://jupyter.org/install. Refe to the reference.txt document for install directions.
     The project notebook follows step by step the process using to analyze and represent the data 
     in this project.

