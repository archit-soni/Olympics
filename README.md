# Olympics

Website - https://olympicsstatistic.web.app

An analysis of results in Tokyo Olympics 2020 using a Statistical model based on 110 years of historic results (1896-2016).

Each Olympic Discipline listed below is accompanied by a link for Raw Predicted Values, along with a Regression Scatter Plot for Predicted vs Actual results and a Clustered-Stack Bar Graph for comparisons.

At the end is an "OVERALL" option, which contains a table with Total Medals Won and Total Medals Predicted for each NOC, Unit Variance and Percentage Variance between the two.

OBSERVATION - As the training set includes ALL Olympics, countries which have performed considerably well in recent years but not throughout history have more varied and inaccurate predicted statistics. A modification to this model would include only the last few Olympics as training set; that however is not the point of this analysis.

NOTE - For the purpose of this project, Soviet Union and Unified Team have been considered as Russia; West Germany, East Germany and United German Team have been considered as Germany; Czechoslovakia has been considered as Czech Republic.

## Files

***Scraper.py*** - Scrapes Wikipedia URLs to save data inside csv files in Data folder. Data/Historic is training set data, Data/Original is test set data of 2020 Olympics
