
########################################################### DASHBOARD | US BIKESHARE DATA ANALYSIS ######################################################################


############################################################ Loading the required libraries (modules) ###################################################################
#Basic Libraries
import pandas as pd
import datetime as dt

#Libraries for Charting and Dashboarding
import plotly.graph_objs as go
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
#########################################################################################################################################################################


############################################################ Invoke the Dash Application ################################################################################
app = dash.Dash()
#########################################################################################################################################################################


############################################################ Import the CSS Stylesheet from one of the Dash App Stylesheets #############################################
app.css.append_css({"external_url": "https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css"})
#########################################################################################################################################################################


############################################################ Define the application layout ##############################################################################
app.layout = (
#Overall Div
html.Div([

    #Div Enclosing the Author Name, Dashboard Title and Udacity Logo
    html.Div([
        #Author
        html.Div([
            html.H5('Created By: Avinash Manure')
                 ], className='two columns', style={'text-align':'center', 'margin-top':35}
                ),
        #Dashboard Title
        html.Div([
            html.H1('Dashboard - Bikeshare')
                 ],className='eight columns', style={'text-align':'center', 'margin-top':30}
                ),
        #Udacity Logo
        html.Div([
            html.Img(src='https://in.udacity.com/assets/images/svgs/logo_wordmark.svg')
                 ], className='two columns'
                )
             ],className='rows'
            ),

    #Div Enclosing the City Selector Title and Radio Buttons
    html.Div([
        html.Div([
            #Title
            html.H5('SELECT CITY', style={'text-align':'center'}),
            #Radio Selector
            dcc.RadioItems(
                id='city-selector',
                options=[
                    {'label': 'Chicago', 'value': 'chicago.csv'},
                    {'label': 'New York', 'value': 'new_york_city.csv'},
                    {'label': 'Washington', 'value': 'washington.csv'}
                        ],
                value='chicago.csv',
                labelStyle={'display': 'inline-block'},
                style={'text-align':'center'}
                          )
                 ], className='twelve columns')], className= 'rows'
             ),
    #Adding Line Breaks
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

    #Trip Duration Section
    html.Div([
        #Title
        html.H5('TRIP DURATION', style={'text-align':'center'}, className='twelve columns'),
             ], className='rows'
            ),
    html.Div([
        #Total Travel Time
        html.Div([
            html.H4('Total Travel Time', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0, 'font-weight': 'bold'}),
            html.H4(id='total-travel-time', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0})
                 ], className='six columns'
                ),
        #Average Travel Time
        html.Div([
            html.H4('Average Travel Time', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0, 'font-weight': 'bold'}),
            html.H4(id='avg-travel-time', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0})
                 ], className='six columns'
                )
             ], className='rows'
            ),
    #Adding Line Breaks
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

    #User Details Section
    html.Div([
        #Title
        html.H5('USER DETAILS', style={'text-align':'center'}, className='twelve columns'),
             ], className='rows'
            ),
        #Graphs
        html.Div([
            #User Type Frequency Bar Graph
            html.Div([
                dcc.Graph(id='user-type')
                     ], className='six columns'
                    ),
            #Gender Type Frequency Bar Graph
            html.Div([
                dcc.Graph(id='gender')
                     ], className='six columns'
                    )
                 ], className='rows'
                ),
        #Year of Birth Statistics
        html.Div([
            #Earliest Birth Year
            html.Div([
                html.H4('Earliest Year Of Birth', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0, 'font-weight': 'bold'}),
                html.H4(id='earliest-birth-year', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0})
                     ], className='four columns'
                    ),
            #Most Recent Birth Year
            html.Div([
                html.H4('Most Recent Year Of Birth', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0, 'font-weight': 'bold'}),
                html.H4(id='recent-birth-year', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0})
                     ], className='four columns'
                    ),
            #Most Common Birth Year
            html.Div([
                html.H4('Most Common Year Of Birth', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0, 'font-weight': 'bold'}),
                html.H4(id='common-birth-year', style={'text-align':'center', 'background':'#80808073', 'margin-top':0, 'margin-bottom':0})
                     ], className='four columns'
                    )
                 ], className='rows'
                ),
    #Adding Line Breaks
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

    #Popular Times Of Travel Section
    html.Div([
        #Title
        html.H5('POPULAR TRAVEL TIMES', style={'text-align':'center'}, className='twelve columns'),
             ], className='rows'
            ),
        #Graphs
        html.Div([
            #Most Common Months Frequency Bar Graph
            html.Div([
                dcc.Graph(id='month-graph')
                     ], className='four columns'
                    ),
            #Most Common Day Of Week Frequency Bar Graph
            html.Div([
                dcc.Graph(id='day-graph')
                     ], className='four columns'
                    ),
            #Most Common Hour Of Day Frequency Bar Graph
            html.Div([
                dcc.Graph(id='hour-graph')
                     ], className='four columns'
                    )
                 ], className='rows'
                ),
    #Adding Line Breaks
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),

    #Popular Stations And Trip Section
    html.Div([
        #Title
        html.Div([
           html.H5('POPULAR STATIONS AND TRIPS', style={'text-align':'center'}, className='twelve columns'),
                 ], className='rows'
                ),
        #Graphs
        #Top 50 Start And End Station Routes
        html.Div([
             dcc.Graph(id='start-end-stations-graph')
                 ], className='twelve columns'
                )
             ], className='rows'
            ),
    #Adding Line Breaks
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
    html.Br(), html.Br(),

       html.Div([
           #Top Start Stations Frequency Bar Graph
           html.Div([
               dcc.Graph(id='start-stations-graph')
                    ], className='six columns'
                   ),
           #Top End Stations Frequency Bar Graph
           html.Div([
               dcc.Graph(id='end-stations-graph')
                    ], className='six columns'
                   )
                ], className='rows'
              )

         ]
        )
             )
#########################################################################################################################################################################


############################################################ Define the Callback (Interactivity) and Visualization Details ##############################################

#Total Travel Time
@app.callback(Output('total-travel-time', 'children'), [Input('city-selector', 'value')])
def total_travel_time(selected_city):
    """
    This Function calculates the total travel time for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Total Travel Time in Hours, Minutes and Seconds for the selected city
    """
    df = pd.read_csv(selected_city)
    total_time = sum(df['Trip Duration'])
    minute = 60
    hour = 60 * 60
    HOURS = int(total_time // hour)
    MINUTES = int((total_time - (HOURS * hour)) // minute)
    SECONDS = int(total_time - ((HOURS * hour) + (MINUTES * minute)))
    return '{} hours {} minutes and {} seconds'.format(HOURS, MINUTES, SECONDS)

#Average Travel Time
@app.callback(Output('avg-travel-time', 'children'), [Input('city-selector', 'value')])
def avg_travel_time(selected_city):
    """
    This Function calculates the average travel time for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Average Travel Time in Hours, Minutes and Seconds for the selected city
    """
    df = pd.read_csv(selected_city)
    avg_time = sum(df['Trip Duration'])/len(df['Trip Duration'])
    minute = 60
    hour = 60 * 60
    HOURS = int(avg_time // hour)
    MINUTES = int((avg_time - (HOURS * hour)) // minute)
    SECONDS = int(avg_time - ((HOURS * hour) + (MINUTES * minute)))
    return '{} hours {} minutes and {} seconds'.format(HOURS, MINUTES, SECONDS)

#User Type Frequency Bar Graph
@app.callback(Output('user-type', 'figure'), [Input('city-selector', 'value')])
def user_type_graph(selected_city):
    """
    This Function plots the User Type Frequency Bar Graph for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: User Type Frequency Bar Graph for the selected city
    NOTE: There is only one count of 'Dependent' User Type for Chicago which has been filtered out for graph's aesthetic purpose
    """
    #Building User Type Frequency Table
    df = pd.read_csv(selected_city)
    user_type = df['User Type'].value_counts()[:2]
    user_type_df = pd.DataFrame(user_type).reset_index()
    user_type_df.columns = ['User_Type', 'Frequency']
    user_type_df = user_type_df.sort_values(ascending=True, by='Frequency')
    #Building User Type Frequency Graph
    graph1 = go.Bar(
                 x= user_type_df.Frequency,
                 y= user_type_df.User_Type,
                 orientation = 'h',
                 marker=dict(
                     color=['rgba(204,204,204,1)', 'rgba(255,107,107,1)']
                            )
                   )
    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='User Type',
                       xaxis=dict(title='Frequency'),
                       yaxis=dict(title='User Type')
                      )
           }

#Gender Type Frequency Bar Graph
@app.callback(Output('gender', 'figure'), [Input('city-selector', 'value')])
def gender_type_graph(selected_city):
    """
    This Function plots the Gender Type Frequency Bar Graph for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Gender Type Frequency Bar Graph for the selected city
    NOTE: If there is not Gender Column in the selected city dataset then the graph is blank
    """
    df = pd.read_csv(selected_city)
    if 'Gender' in df.columns:
        #Building Gender Type Frequency Table
        gender = df['Gender'].value_counts()
        gender_df = pd.DataFrame(gender).reset_index()
        gender_df.columns = ['Gender', 'Frequency']
        gender_df = gender_df.sort_values(ascending=True, by='Frequency')
        #Building Gender Type Frequency Graph
        graph1 = go.Bar(
                     x= gender_df.Frequency,
                     y= gender_df.Gender,
                     orientation = 'h',
                     marker=dict(
                         color=['rgba(204,204,204,1)', 'rgba(255,107,107,1)']
                                )
                      )
        #Returning the Graph Built
        return {
            'data': [graph1],
            'layout': dict(title='Gender',
                           xaxis=dict(title='Frequency'),
                           yaxis=dict(title='Gender')
                          )
               }
    else:
        #Building the Blank Graph when Gender column not available
        graph1 = go.Bar(
                     x= 0,
                     y= 0,
                     orientation = 'h',
                       )
        #Returning the Blank Graph Built
        return {
            'data': [graph1],
            'layout': dict(title='Gender details not available',
                           xaxis=dict(title='Frequency'),
                           yaxis=dict(title='Gender')
                          )
               }

#Earliest Birth Year
@app.callback(Output('earliest-birth-year', 'children'), [Input('city-selector', 'value')])
def earliest_birty_year(selected_city):
    """
    This Function calculates the earliest birth year for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Earliest Birth Year for the selected city
    """
    df = pd.read_csv(selected_city)
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(min(df['Birth Year']))
        return earliest_birth_year
    else:
        return 'Birth Year Details Not Available'

#Most Recent Birth Year
@app.callback(Output('recent-birth-year', 'children'), [Input('city-selector', 'value')])
def recent_birth_year(selected_city):
    """
    This Function calculates the most recent birth year for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Recent Birth Year for the selected city
    """
    df = pd.read_csv(selected_city)
    if 'Birth Year' in df.columns:
        recent_birth_year = int(max(df['Birth Year']))
        return recent_birth_year
    else:
        return 'Birth Year Details Not Available'

#Most Common Birth Year
@app.callback(Output('common-birth-year', 'children'), [Input('city-selector', 'value')])
def common_birth_year(selected_city):
    """
    This Function calculates the most common birth year for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common Birth Year for the selected city
    """
    df = pd.read_csv(selected_city)
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year'].value_counts().reset_index()
        birth_year.columns = ['Year', 'Frequency']
        common_birth_year = int(birth_year.Year[0])
        common_birth_year_frequency = int(birth_year.Frequency[0])
        return '{} (Frequency: {})'.format(common_birth_year, common_birth_year_frequency)
    else:
        return 'Birth Year Details Not Available'


#Most Common Months Frequency Bar Graph
@app.callback(Output('month-graph', 'figure'), [Input('city-selector', 'value')])
def common_months(selected_city):
    """
    This Function plots the Most Common Months Frequency Bar Graph for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common Months Frequency Bar Graph for the selected city
    """
    #Building Months Frequency Table
    df = pd.read_csv(selected_city)
    df['month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')
    month_table = df.month.value_counts(ascending=True)
    month_table_df = pd.DataFrame(month_table).reset_index()
    month_table_df.columns = ['Month', 'Frequency']
    #Building Most Common Months Frequency Graph
    graph1 = go.Bar(
                 x= month_table_df.Frequency,
                 y= month_table_df.Month,
                 orientation = 'h',
                 marker=dict(
                     color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(255, 107, 107, 1)'
                           ])
                   )
    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='Most Common Month: {}'.format(month_table_df.Month.iloc[-1]),
                       xaxis=dict(title='Frequency'),
                       yaxis=dict(title='Month')
                      )
           }

#Most Common Day Of Week Frequency Bar Graph
@app.callback(Output('day-graph', 'figure'), [Input('city-selector', 'value')])
def common_days(selected_city):
    """
    This Function plots the Most Common Days of Month Frequency Bar Graph for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common Days of Month Frequency Bar Graph for the selected city
    """
    #Building Days Frequency Table
    df = pd.read_csv(selected_city)
    df['day'] = pd.to_datetime(df['Start Time']).dt.strftime('%A')
    day_table = df.day.value_counts(ascending=True)
    day_table_df = pd.DataFrame(day_table).reset_index()
    day_table_df.columns = ['Day', 'Frequency']
    #Building Most Common Days of Month Frequency Graph
    graph1 = go.Bar(
                 x= day_table_df.Frequency,
                 y= day_table_df.Day,
                 orientation = 'h',
                 marker=dict(
                     color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(255, 107, 107, 1)'
                           ])
                  )
    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='Most Common Day of Week: {}'.format(day_table_df.Day.iloc[-1]),
                       xaxis=dict(title='Frequency'),
                       yaxis=dict(title='Day')
                      )
           }

#Most Common Hour Of Day Frequency Bar Graph
@app.callback(Output('hour-graph', 'figure'), [Input('city-selector', 'value')])
def common_hours(selected_city):
    """
    This Function plots the Most Common Hours of Day Frequency Bar Graph for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common Hours of Day Frequency Bar Graph for the selected city
    """
    #Building Hours Frequency Table
    df = pd.read_csv(selected_city)
    df['hour'] = pd.to_datetime(df['Start Time']).dt.strftime('%I %p')
    hour_table = df.hour.value_counts(ascending=True)
    hour_table_df = pd.DataFrame(hour_table).reset_index()
    hour_table_df.columns = ['Hour', 'Frequency']
    #Building Most Common Hours of Day Frequency Graph
    graph1 = go.Bar(
                 x= hour_table_df.Frequency,
                 y= hour_table_df.Hour,
                 orientation = 'h',
                 marker=dict(
                     color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(255, 107, 107, 1)'])
                  )
    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='Most Common Hour of Day: {}'.format(hour_table_df.Hour.iloc[-1]),
                       xaxis=dict(title='Frequency'),
                       yaxis=dict(title='Hour')
                      )
           }

#Top 50 Start And End Station Routes
@app.callback(Output('start-end-stations-graph', 'figure'), [Input('city-selector', 'value')])
def start_end_station_graph(selected_city):
    """
    This Function plots the Most Common Start-End Station Routes for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common Start-End Station Routes Graph for the selected city
    """
    #Building Top 50 Start-End Station Table
    df = pd.read_csv(selected_city)
    df_modified = df[['Start Station', 'End Station']]
    df_modified.columns = ['Start_Station', 'End_Station']
    cross_table = df_modified.groupby(['Start_Station', 'End_Station']).size().nlargest(50).reset_index(name='Frequency')
    #Building Top 50 Start-End Station Graph
    graph1 = go.Heatmap(
                 x= cross_table.End_Station,
                 y= cross_table.Start_Station,
                 z= cross_table.Frequency.values
                       )
    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='MOST COMMON START AND END STATIONS (Top 50)')
           }

#Top Start Stations Frequency Bar Graph
@app.callback(Output('start-stations-graph', 'figure'), [Input('city-selector', 'value')])
def start_station_graph(selected_city):
    """
    This Function plots the Most Common Start Stations for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common Start Stations Graph for the selected city
    """
    #Building Top Start Stations Table
    df = pd.read_csv(selected_city)
    popular_start_stations = df['Start Station'].value_counts()[:10]
    popular_start_stations_df = pd.DataFrame(popular_start_stations).reset_index()
    popular_start_stations_df.columns = ['Start_Station', 'Frequency']
    popular_start_stations_df = popular_start_stations_df.sort_values(ascending=True, by='Frequency')
    #Building Top Start Stations Graph
    graph1 = go.Bar(
                 x= popular_start_stations_df.Frequency,
                 y= popular_start_stations_df.Start_Station,
                 orientation = 'h',
                 marker=dict(
                     color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(255, 107, 107, 1)']
                            )
                   )
    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='Most Common Start Station: {}'.format(popular_start_stations_df.Start_Station.iloc[-1]),
                       xaxis=dict(title='Frequency'),
                       yaxis=dict(title=' ')
                      )
           }

#Top End Stations Frequency Bar Graph
@app.callback(Output('end-stations-graph', 'figure'), [Input('city-selector', 'value')])
def end_station_graph(selected_city):
    """
    This Function plots the Most Common End Stations for the selected city (through Radio Button)
    INPUT: City Selected through Radio Button
    OUTPUT: Most Common End Stations Graph for the selected city
    """
    #Building Top End Stations Table
    df = pd.read_csv(selected_city)
    popular_end_stations = df['End Station'].value_counts()[:10]
    popular_end_stations_df = pd.DataFrame(popular_end_stations).reset_index()
    popular_end_stations_df.columns = ['End_Station', 'Frequency']
    popular_end_stations_df = popular_end_stations_df.sort_values(ascending=True, by='Frequency')
    #Building Top End Stations Graph
    graph1 = go.Bar(
                 x= popular_end_stations_df.Frequency,
                 y= popular_end_stations_df.End_Station,
                 orientation = 'h',
                 marker=dict(
                     color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                            'rgba(204,204,204,1)', 'rgba(255, 107, 107, 1)']
                            )
                   )

    #Returning the Graph Built
    return {
        'data': [graph1],
        'layout': dict(title='Most Common End Station: {}'.format(popular_end_stations_df.End_Station.iloc[-1]),
                       xaxis=dict(title='Frequency'),
                       yaxis=dict(title=' ')
                      )
            }

#########################################################################################################################################################################


############################################################ Run The Application On Server ##############################################################################
if __name__ == '__main__':
    app.run_server(debug=False)
#########################################################################################################################################################################
