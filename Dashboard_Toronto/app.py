# -*- coding: utf-8 -*-

# Run this app with `python app.py` and visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime as dt

# Load Data
toronto_df = pd.read_csv('toronto_data.csv')
toronto_df['episode_date'] = pd.to_datetime(toronto_df['episode_date'])

# Calculating Fatality Rate by Area
fatal_by_area = pd.DataFrame(toronto_df[toronto_df['outcome'] == 'FATAL'].groupby(['neighbourhood_name']).count()['outcome'])
fatal_by_area.columns = ['fatality']
cases_by_area = pd.DataFrame(toronto_df[toronto_df['outcome'] != 'ACTIVE'].groupby(['neighbourhood_name']).count()['outcome'])
cases_by_area.columns = ['total_cases']
fatality_rate_by_area = cases_by_area.merge(fatal_by_area, left_index=True, right_index=True)
fatality_rate_by_area['fatality_rate'] = fatality_rate_by_area['fatality']/fatality_rate_by_area['total_cases']*100
fatality_rate_by_area = fatality_rate_by_area.sort_values('fatality_rate', ascending=False).reset_index()

# Chart for Outcome by Age
fig_age_outcome = px.histogram(
    toronto_df, x="episode_date", y="age_group", 
    histfunc="count", color='outcome', barmode='group', orientation='h',
    labels={"episode_date": "cases", "age_group": "age"},
    template="simple_white"
)
fig_age_outcome.update_layout(yaxis={'categoryorder':'category descending'})

# Chart for Outcome by Gender
fig_gender_outcome = px.histogram(
    toronto_df, x="episode_date", y="gender", 
    histfunc="count", color='outcome', barmode='group', orientation='h',
    labels={"episode_date": "cases", "gender": "gender"},
    template="simple_white"
)
fig_gender_outcome.update_layout(
    yaxis={'categoryorder':'category descending'}
)

# Chart for Fatality by Gender
fig_fatality_area = px.bar(
    fatality_rate_by_area, x="neighbourhood_name", y="fatality_rate",
    labels={"neighbourhood_name": "neighbourhood name", "fatality_rate": "fatality rate"},
    template="simple_white"
)
fig_fatality_area.update_layout(xaxis_tickangle=-45)


# Load CSS Style
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Navigation Bar
NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(
                        dbc.NavbarBrand("Team-3 COVID-19 Dashboard", className="ml-2")
                    ),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://github.com/tenley8/Team-3",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)

# Card to hold graphs for number of cases
TORONTO_CASE = dbc.Card(
    [
        dbc.CardHeader(html.H5("Toronto COVID-19 - Number of Cases")),
        dbc.CardBody([
            html.Div(id='tab_toronto_case_text'),
            dcc.Tabs(
                id="tab_toronto_case", value='tab-1',
                children=[
                    dcc.Tab(
                        label="Age Group", value='tab-1',
                        children=[dcc.Graph(id='toronto_case_by_age'),]
                    ),
                    dcc.Tab(
                        label="Gender", value='tab-2',
                        children=[dcc.Graph(id="toronto_case_by_gender"),]
                    )
                ]
            ),
            html.Label("Select Date Since the First Case", style={"marginTop": 10}, className="lead"),
            dcc.Slider(
                id='date-slider',
                min=toronto_df['date_since_first_case'].min(),
                max=toronto_df['date_since_first_case'].max(),
                value=toronto_df['date_since_first_case'].max(),
                marks={str(date): str(date) for date in pd.Series(np.arange(0,toronto_df['date_since_first_case'].max(),5))},
                step=None
            )
        ])
    ]        
)

# Card to hold graphs for outcome of COVID-19
TORONTO_OUTCOME = dbc.Card(
    [
        dbc.CardHeader(html.H5("Toronto COVID-19 - Outcomes")),
        dbc.CardBody(
            dcc.Tabs(
                id="tab2",
                children=[
                    dcc.Tab(
                        label="Age Group",
                        children=[dcc.Graph(id="toronto_outcome_by_age", figure=fig_age_outcome)]
                    ),
                    dcc.Tab(
                        label="Gender",
                        children=[dcc.Graph(id="toronto_outcome_by_gender", figure=fig_gender_outcome)]
                    )
                ]
            )
        )
    ]        
)

NEIGHBOURHOOD = dbc.Card([
    dbc.CardHeader(html.H5("Fatality Rate by Area")),
    dbc.CardBody(
        children=[dcc.Graph(id="fatality_by_area", figure=fig_fatality_area)]
    )
])

BODY = dbc.Container(
    [
        dbc.Col(dbc.Card(TORONTO_CASE), style={"marginTop": 20}),
        dbc.Col(dbc.Card(TORONTO_OUTCOME), style={"marginTop": 20}),
        dbc.Col(dbc.Card(NEIGHBOURHOOD), style={"marginTop": 20,"marginBottom": 40})
    ]
)

app.layout = html.Div(children=[NAVBAR, BODY])


@app.callback(
    Output('toronto_case_by_age', 'figure'),
    [Input('date-slider', 'value')])
def update_age_figure(selected_date):
    filtered_df = toronto_df[toronto_df.date_since_first_case <= selected_date]

    fig = px.histogram(
        filtered_df, x="age_group", y="episode_date", histfunc="count",
        labels={"episode_date": "cases", "age_group": "age"},
        template="simple_white"
    )

    fig.update_layout(transition_duration=500, xaxis={'categoryorder':'category ascending'})

    return fig


@app.callback(
    Output('toronto_case_by_gender', 'figure'),
    [Input('date-slider', 'value')])
def update_gender_figure(selected_date):
    filtered_df = toronto_df[toronto_df.date_since_first_case <= selected_date]

    fig = px.histogram(
        filtered_df, x="gender", y="episode_date", histfunc="count",
        labels={"episode_date": "cases"},
        template="simple_white"
    )

    fig.update_layout(transition_duration=500, xaxis={'categoryorder':'category ascending'})

    return fig


@app.callback(Output('tab_toronto_case_text', 'children'),
              [Input('tab_toronto_case', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.P('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.P('Tab content 2')
        ])



# Running Application
if __name__ == '__main__':
    app.run_server(debug=True)