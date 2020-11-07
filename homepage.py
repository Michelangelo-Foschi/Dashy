import plotly.express as px
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64
from jupyter_dash import JupyterDash
from navbar import Navbar
from dash.dependencies import Input, Output
import plotly.express as px
nav = Navbar()
BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])

def drawFigure1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                             dcc.Graph(
                         figure={"data": [{"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], "y": [1,2,2,3,7,3,3,2,5,3,8,2,6,2,2,2,6,2,6,3,6,2,9], 'type':'bar'},{'x':[3,6,9,12,15,18,21,24],'y':[3,3,3,3,3,3,3,3]}],
            
                
                         }
                         
                            ),        
            ])
        )
    ])
def drawFigureReturns():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                             dcc.Graph(
                         figure={"data": [{"x": [1,2,3,4,5,6], "y": [2,4,2,1,2,6],'type':'line'},{'x':[1,2,3,4,5,6],'y':[8,9,7,6,5.5,4],'type':'line'},{'x':[1,2,3,4,5,6],'y':[3,3,3,3,3,3]}]}
            
                
                         
                         
                            ),        
            ])
        )
    ])
def drawFigureRolling():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                             dcc.Graph(
                         figure={"data": [{"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], "y": [1,2,2,3,7,3,3,2,5,3,8,2,6,2,2,2,6,2,6,3,6,2,9]}]}
            
                
                         
                         
                            ),        
            ])
        )
    ])
def drawFigureDrawDown():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                             dcc.Graph(
                         figure={"data": [{"x": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], "y": [1,2,2,3,7,3,3,2,5,3,8,2,6,2,2,2,6,2,6,3,6,2,9], 'type':'bar'},{'x':[3,6,9,12,15,18,21,24],'y':[3,3,3,3,3,3,3,3]}]}
            
                
                         
                         
                            ),        
            ])
        )
    ])

def drawFigureMonthlyRets():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                             dcc.Graph(
                         figure={"data": [{"x": [1,1.3,1.6,1.9,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], "y": [1,1.3,1.4,1.8,2,2,3,7,3,3,2,5,3,8,2,6,2,2,2,6,2,6,3,6,2,9]}]}
            
                
                         
                         
                            ),        
            ])
        )
    ])

def drawTextReturns():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Returns"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])


def drawTextDrawdown():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Drawdown"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])
def drawTextMonthlyRets():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("MonthlyRets"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])
def drawTextRolling():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Rolling"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])
df = px.data.iris()


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

tabs_styles = {
    'height': '44px'
}
body = dbc.Container(
    [
    dcc.Tabs([
        dcc.Tab(label='Attribution Summary Tab', children=[
        dbc.Row(
            [
                dbc.Card(
        dbc.CardBody([

            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawTextReturns(),
                    drawFigureReturns() 
                ], width=5),
                dbc.Col([
                    drawTextDrawdown(),
                    drawFigure1()
                ], width=7),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawTextRolling(),
                    drawFigureRolling()
                ], width=6),
                dbc.Col([
                    drawTextMonthlyRets(),
                    drawFigure1()
                ], width=6),
            ], align='center'),      
        ]), color = 'dark'

                )
           
           ]
        ),



        ]),
        
        dcc.Tab(label='Attribution Tab', children=[
        dbc.Row(
            [
                dbc.Card(
        dbc.CardBody([

            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawTextMonthlyRets(),
                    drawFigureMonthlyRets() 
                ], width=6),
                dbc.Col([
                    drawTextReturns(),
                    drawFigureReturns()
                ], width=6),
                dbc.Col([
                    drawTextDrawdown(),
                    drawFigureDrawDown() 
                ], width=6),
            ], align='center'), 
            html.Br(),
          
        ]), color = 'dark'

                )
           
           ]
        ),



        ]),
        dcc.Tab(label='Data Tab', children=[
        dbc.Row(
            [
                dbc.Card(
        dbc.CardBody([

            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawTextRolling(),
                    drawFigureRolling()
                ], width=6),
             
                dbc.Col([

                    drawTextMonthlyRets(),
                    drawFigureMonthlyRets()
                ], width=6),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawTextRolling(),
                    drawFigure1()
                ], width=6),
                dbc.Col([
                    drawTextMonthlyRets(),
                    drawFigureDrawDown()
                ], width=5),
            ], align='center'),      
        ]), color = 'dark'

                )
           
           ]
        ),
        ]),
        dcc.Tab(label='EarningsLiveBreakdown Tab', children=[
        dbc.Row(
            [
                dbc.Card(
        dbc.CardBody([

            html.Br(),
            dbc.Row([
    
                dbc.Col([
                    drawTextMonthlyRets(),
                    drawFigureDrawDown()
                ], width=6),
                 dbc.Col([
                    drawTextRolling(),
                    drawFigureRolling()
                ], width=6)           
            ], align='center'), 
            html.Br(),
           
           
        ]), color = 'dark'

                )
           
           ]
        ),
        ]),
    ])
])


def Homepage(): 
    layout = html.Div([
    nav,
    body
    ])


    
    return layout

app.layout = Homepage() 
  


if __name__ == '__main__':
    app.run_server(debug=True)

