# US bikeshare dashboard using Dash (by plotly)
  
  This is part of my submission to the Udacity's Machine Learning Nanodegree program wherein I have submitted a web application (dashboard) on US bikeshare data using Dash by Plotly.
  
![](https://raw.githubusercontent.com/avinax/us-bikeshare-dashboard-using-plotly-dash/master/bikeshare-dashboard.png) 

**REQUIRED PACKAGES**

1. pandas (pip install pandas)

2. plotly (pip install plotly)

3. dash (pip install dash)

4. dash_core_components (pip install dash_core_components)

5. dash_html_components (pip install dash_html_components)

6. dash-renderer (pip install dash-renderer)


**INSTRUCTIONS**

1. After installing the above packages, run the bikeshare.py file (command: python bikeshare.py) on your terminal (command window) attached along with this document. Please run it through command prompt/terminal only. It will give issues when run through Jupyter/IPython (https://community.plot.ly/t/dash-server-not-updating-through-examples/6419/7) 
2. If everything is alright then you will see the following message in your terminal
      * Serving Flask app "bikeshare" (lazy loading)
      * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
      * Debug mode: off
      * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
3. Now, paste the address http://127.0.0.1:8050/ onto your browser to open the dashboard
4. The application contains the following details/graphs:
* Set of Radio Buttons to choose the city for which you want to get the statistics
* Trip duration (KPI boxes)
  * Total travel time
  * Average travel time
* User info (Bar Charts and KPI boxes)
  * Counts of each user type
  * Counts of each gender (only available for NYC and Chicago)
  * Earliest, most recent, most common year of birth (only available for NYC and Chicago)
* Popular times of travel (Bar Charts)
  * Most common month
  * Most common day of week
  * Most common hour of day 
* Popular stations and trip (Bar Charts and Heatmap)
  * Most common start stations
  * Most common end stations
  * Most common trip from start to end (i.e., most frequent combination of start station and end station)
5. The statistics/graphs change (are updated) as per the user input city (radio button)
6. The graphs are interactive and one can zoom/pan/select etc.


**REFERENCES**

* Pandas Official Documentation: https://pandas.pydata.org/pandas-docs/stable/
* Dash User Guide: https://dash.plot.ly/ 
* Dash App Gallery : https://dash.plot.ly/gallery 
* Dash Oil and Gas App source code: https://github.com/plotly/dash-oil-and-gas-demo 
* Plotly Graphs in Python: https://plot.ly/python/ 
* Plotly Bar Charts in Python: https://plot.ly/python/bar-charts/ 
* Plotly Heatmaps in Python: https://plot.ly/python/heatmaps/ 
* Plotly Dash Tutorial by Adriano Yoshino (YouTube videos):
* https://www.youtube.com/watch?v=yPSbJSblrvw&t=3s 
* https://www.youtube.com/watch?v=f2qUWgq7fb8&t=1s 
* https://www.youtube.com/watch?v=o5fgj1AIq4s&t=1s 
* Converting Seconds to Hours, Minutes and Seconds: https://stackoverflow.com/questions/48573444/python-converting-seconds-to-hours-minutes-seconds 
* HTML (elements, attributes etc.): https://www.w3schools.com/html/default.asp 
* CSS: https://www.w3schools.com/css/default.asp 


        



        

