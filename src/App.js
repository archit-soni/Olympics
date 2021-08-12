import React from "react";
import Accordion from "./Accordion";
import { accordionData } from "./utils/content";
import Table from "csv-react-table";

const App = () => {
  return (
    <div>
      <h1>Olympics 2020 - A Probability based analysis</h1>
      <h6>
        An analysis of results in Tokyo Olympics 2020 using a Statistical model
        based on 110 years of historic results (1896-2016).
        <br />
        <br />
        Each Olympic Discipline listed below is accompanied by a link for Raw
        Predicted Values, along with a Regression Scatter Plot for Predicted vs
        Actual results and a Clustered-Stack Bar Graph for comparisons.
        <br />
        <br />
        At the end is an "OVERALL" option, which contains a table with Total
        Medals Won and Total Medals Predicted for each NOC, Unit Variance and
        Percentage Variance between the two.
        <br />
        <br />
        OBSERVATION - As the training set includes ALL Olympics, countries which
        have performed considerably well in recent years but not throughout
        history have more varied and inaccurate predicted statistics. A
        modification to this model would include only the last few Olympics as
        training set; that however is not the point of this analysis.
        <br />
        <br />
        NOTE - For the purpose of this project, Soviet Union and Unified Team
        have been considered as Russia; West Germany, East Germany and United
        German Team have been considered as Germany; Czechoslovakia has been
        considered as Czech Republic.
        <br />
        <br />
        Source code is available at{" "}
        <a href="https://github.com/archit-soni/Olympics">GitHub</a>, including{" "}
        <a href="https://github.com/archit-soni/Olympics/blob/main/Scraper.py">
          Scraper
        </a>
        ,{" "}
        <a href="https://github.com/archit-soni/Olympics/blob/main/Probability.py">
          Code for estimating statistics
        </a>{" "}
        and{" "}
        <a href="https://github.com/archit-soni/Olympics/blob/main/Plotter.py">
          Code for plotting Graphs
        </a>
        . Other relevant code/csv files/Front-End code available at the GitHub
        source linked.
      </h6>
      <div className="accordion">
        {accordionData.map(({ title, content, image, image2 }) => (
          <Accordion
            title={title}
            content={content}
            image={image}
            image2={image2}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
