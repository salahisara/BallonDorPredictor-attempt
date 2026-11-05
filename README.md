# BallonDorPredictor-attempt
This was an Attempt to see whether a simple machine learning could predict 2026 Ballon dor winner with the help of Claude. 

After choosing Ridge and Random forest as the primary two algorythms, I did the tiresome task of Data Entry and preparing the data set that they were trained on. (BSO2.xlsx) Unfortunately, gathering this Dataset wasn't as easy as simply asking Claude, because resources differed and I had to enter many of them by hand. This dataset contains the top ten list of the BD list from 2018 to 2025. Here is an overview:

Players Personal Data:
-
Name: The players name and last name

Age: The players age at the time of the ceremony

Nationality: The National team the player played for which sometime differed from the place they were born.

Position: the position they played either Forward, Defender, Midfielder, or Goalkeeper.

Club_Country: The league they played in.	
Club: The club they played in. Sometimes for older years a player played for two teams in one calender year, I chose the first team because it was usually the one they played the important UCL games in and/or won their domestic league.

Votes: The total votes in the Ballon Dor (If I managed to find it from a credible source)	

Rank: Their final Rank	

Players Club Data:
-
UEFA_Club_coefficient: This is the coefficient given to every club each season. I found and entered it directly from the UEFA website over in UEFA.com

League_finish: Their clubs final rank in their domestic league.

Won_league: Whether they won the league(1) or didnt (0)

UCL_result: The final position on UCL. I turned this data into a numerical data. Winners=1, Runnerup=2, Semifinal=4, Quarterfinal=8, Round of 16=16, League phase=32 and didnt participate=99.

Won_UCL: Whether they won (1) or didnt (0)

Appearances: How many times they played for the club that season including UCL and domestic League and Eueropa league if they had fallen there. (Eventually didnt use it.) (As written on Transfermarkt)

Goals: The amount of goals they scored. (As written on Transfermarkt)

Assists: The amount of assists.(As written on Transfermarkt)

Is_Forward: If the players played as Forward (1) or not(0)

Is_Club_Cap: If the players played as National team Captain (1) or not(0)

Is_National_Cap: If the players played as Club team Captain (1) or not(0)

For the last two, I only added (1) if they were the first Captain or the Captain for the majority of the games.

National Team data:
-
WC_year:  Whether there was a World Cup that year (1) or wasnt (0)

WC_finish: Their final ranking in the world cup. Winners=1, Runnerup=2, Semifinal=4, Quarterfinal=8, Round of 16=16, Round of 32 for 2026/Groupstage=32, Groupstage for 2026WC=64, and didnt participate=99. If there was no WC that year=NA

CC_year: Whether there was a Euro or Cupa America that year (1) or wasnt (0). I did not include other Continental cups.

CC_finish: Their final ranking in the world cup. Winners=1, Runnerup=2, Semifinal=4, Quarterfinal=8, Round of 16=16, Groupstage=32, and didnt participate=99, or Participated in a different Cup=NA

WC_Goals

WC_Assists

CC_goals

CC_Assists
(Finding the last four was a bit tricky. For example I found All the data for 2026 on the Fifa World cup website but didnt for the 2022 or 2018 one. Eventually had to chose ESPN and news outlets to find my missing data.(https://www.espn.com/soccer/stats/_/league/FIFA.WORLD/season/2022) for example)


N_1= Whether they won something with the National Team (1) or didnt (0)

Club_1= Whether they won something with their club Team (1) or didnt (0)
  
There are alot of Data entered into the excel file that I eventually chose not to use, such as Appeareances, WC_Appeareances, CC_Appeareances, Due to uncertain resources or reduce my Non-Numerical Data as much as possible.
-



The model has great trouble predicting the years where there was a World Cup, Euros, or Copa America. Otherwise it worked well on predicting the First place winner.
-

<img width="1051" height="856" alt="Screenshot 2026-11-05 113346" src="https://github.com/user-attachments/assets/b513baa1-9ce9-4691-8f35-1f8016992c20" />
<img width="1036" height="847" alt="Screenshot 2026-11-05 113837" src="https://github.com/user-attachments/assets/3d63f5ca-193e-44af-8498-47b939a6c024" />
<img width="1024" height="847" alt="Screenshot 2026-11-05 113819" src="https://github.com/user-attachments/assets/7da2e4b7-1030-44b7-bf61-003194283b08" />
<img width="1083" height="849" alt="Screenshot 2026-11-05 113732" src="https://github.com/user-attachments/assets/8455a491-42de-4c5e-9da6-93e13ea515f3" />






And The years that had No CC or WC the model turned out pretty well:
-
<img width="1073" height="850" alt="Screenshot 2026-11-05 113409" src="https://github.com/user-attachments/assets/7ceffd12-c391-4ac5-aa54-9cf5c23ad33f" />
<img width="1048" height="860" alt="Screenshot 2026-11-05 113759" src="https://github.com/user-attachments/assets/b41c8e0d-3ed5-4188-8fe3-d3b2b4169eb3" />
<img width="1066" height="862" alt="Screenshot 2026-11-05 113930" src="https://github.com/user-attachments/assets/3cb8f15e-9c16-461e-914c-cc74deb5828b" />


Which is Why I was hesitant to post it before the answers were anounces as I was certain Yamal was going to win it and there was some Huge problem that my model kept saying Harry Kane. Eventually I gave up, and it turns out it wasnt all that wrong lol.

Regardless, the margin of error is still far too high. I havent considered the effects of Social Media, Public campains, or any other data outside of football really. There is also a need to expand the data set to inclube more WC and CC so that it works well for those years as well. 
I am open to constructive criticims but please keep in mind Machine learning is not my specialty.
-Thank you.

<img width="1001" height="594" alt="Screenshot 2026-11-05 113958" src="https://github.com/user-attachments/assets/d66d5509-cc80-4a06-af4c-ab02d17dfd3e" />


