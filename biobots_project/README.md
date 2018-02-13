# BioBots Coding Challenge 

Mohit Nalavadi 

May 13-15, 2017

Thank you again for the opportunity to interview for the software engineering role at BioBots! I had a busy and insightful weekend teaching myself Flask, HTML, CSS and JavaScript to complete the task. While this was my first web development project, I think it is a good demonstration of my ability to learn quickly, efficiently design solutions, and set laser focus to get a task done. Even without starting with all the foundational knowledge required, I was able to source and weave together information to fill my gaps. I had a fun time building this tool, and most of the frustrations ended with solutions (exception explained below). So, here is how my tool works. I started by breaking the project into two sections: 

1) A dashboard for users to analyze and extract their data. 

2) A statistical analysis for the BioBots internal team to gain an understanding from the user data. 

## Ensure you have the following python 2.7 dependences: 

For the web app: os, json, pandas, flask 

For the stats analysis: jupyter, os, json, pandas, numpy, matplotlib, seaborn, statsmodels
 

## The User Dashboard

To run on command line: 'python server.py', visit local host url. 

The user dashboard is a website built on python's Flask module. The user visits the homepage and enters their unique serial number. They are redirected to a webpage displaying their unique data. On the back end, I used the pandas module, a data science framework, to convert the messy json to a tabular dataframe, which is much easier and quicker to handle. 

The dataframes were split up based on categories (cell viability, crosslinking, printer settings etc.) and fed into the 'highcharts' JavaScript module. I chose Time Series and Boxplots for UX reasons. Time Series shows specific information about prints against experiment iteration, while boxplots show distributions of the data and larger trends. I also included tabular data with numerical values (means, quartiles etc.) and a link to download selected user data. 

A cool feature of the charts is that the bottom right, where it says "need help?", routes to the software troubleshooting page on the real biobots.io site. This way the user can use the biowiki docs to troubleshoot or explain their data. All BioBots logo instances redirect to the biobots.io page. 

Unfortunately, the one problem I could not solve was getting the boxplots to appear. My troubleshooting process involved: isolating an individual boxplot (worked), trying the same plot as more Time Series charts (worked), and testing with dummy data (worked). But highcharts did not play nice with building multiple chart types from dynamically soured data. I predict the solution would involve something with JavaScript routing the data series variables. 

## Statistical Analysis

View on Github or from browser if you have jupyter installed. 

The Internal Team portion of the project is a statistical analysis of the data. I do an exploratory analysis, which is a data science approach to characterize, visualize and formulate hypotheses in the early stage of analysis. My methods are outlined in the Jupyter Notebook (.ipynb file). 

The core purpose of this is for the internal team to extract signal from noise, and glean trends from the data. These insights can be funneled back to the users, so they can alter their experiments to optimize results and save resources, and back to the BioBots engineers to design the printers with user results in mind. 

Though this data is fake, I suggest a future implementation from my conclusions. With more data on user results, a machine learning model could be employed to predict the best results from printer settings. This can exist as a web tool which makes suggestions to change variables like nozzle diameter, extruder pressure, or material viscosity to increase cell viability.

## Conclusions

I had a good time with this project and adding web development to my programming arsenal of data science and signal processing! I'm confident that my work here is a good demonstration of what I can contribute to BioBots. It displays my ability to learn quickly, ask the right questions for efficient problem solving, and my nature as a curious self-starter. I would be excited to work at the intersection of biology, hardware, and software at BioBots, and grateful to know that my work contributes to the future of science. Thanks again for the opportunity to interview, and I look forward to hearing about what you think of my work!
