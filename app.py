import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Freer Sackler'
myheading1 = 'Whistler in Watercolor'
myheading2 = 'May 18, 2019–November 3, 2019 in galleries 10 and 11'
image1 = 'maxresdefault.jpg'
image2 = 'FS-F1902.158a-c_001.jpg'
textbody = "Recent research conducted by museum curators, scientists, and conservators now shines new light on Whistler’s materials, techniques, and artistic genius, as seen in this first major exhibition of his watercolors at the Freer Gallery."
sourceurl = 'https://www.freersackler.si.edu/exhibition/whistler-in-watercolor/'
githublink = 'https://github.com/caroleonor/dash-dc-layout/edit/master/app.py'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '12px',
                'font-size': '20px',
                'height': '120px',
                'border': 'rgb(255,255,255)',
                'color': 'rgb(255, 255, 255)',
                'backgroundColor': 'rgb(225, 215, 190)',
                'textAlign': 'left',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
