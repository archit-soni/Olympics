# Olympics

Website - https://olympicsstatistic.web.app

An analysis of results in Tokyo Olympics 2020 using a Statistical model based on 110 years of historic results (1896-2016).

Each Olympic Discipline listed below is accompanied by a link for Raw Predicted Values, along with a Regression Scatter Plot for Predicted vs Actual results and a Clustered-Stack Bar Graph for comparisons.

At the end is an "OVERALL" option, which contains a table with Total Medals Won and Total Medals Predicted for each NOC, Unit Variance and Percentage Variance between the two.

OBSERVATION - As the training set includes ALL Olympics, countries which have performed considerably well in recent years but not throughout history have more varied and inaccurate predicted statistics. A modification to this model would include only the last few Olympics as training set; that however is not the point of this analysis.

NOTE - For the purpose of this project, Soviet Union and Unified Team have been considered as Russia; West Germany, East Germany and United German Team have been considered as Germany; Czechoslovakia has been considered as Czech Republic.

ALL GRAPHS CAN BE FOUND INSIDE src/utils

ALL RAW DATA CAN BE FOUND INSIDE data/

## Files

***Scraper.py*** - Scrapes Wikipedia URLs to save data inside csv files in Data folder. Data/Historic is training set data, Data/Original is test set data of 2020 Olympics

***CountryFix.py*** - Renames defunct countries and other minor format unifications

***Probability.py*** - Calculates probabilities of a country winning a gold, silver and bronze medal in each discipline separately using training set. Formula used is (avail-1)\*(m/Tm) + t/T + (1/206) which roughly translates to (gold/silver/bronze available medals in 2020 - 1)\*(gold/silver/bronze respectively medals won by country in this sport historically) + (total medals won by country in this sport historically)/(total medals given out in this sport) + Additive Laplace smoothing for outlier outcomes.

***Plotter.py*** - Generates Scatter Plots and double-clustered triple-stacked Bar Graphs using Matplotlib


Files inside src/ are used for front end display of website using React. Design of website has been modified using https://github.com/myogeshchavan97/react-accordion-demo/ as base.
