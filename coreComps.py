# Run this app with `python app.py` and
# visit http://127.0.0.1:4050/ in your web browser.

#import the necessary modules
from dash import Dash, html, dcc 

#Initialise the app
app=Dash(__name__)

#define the layout-arrangement of the components in web browser.
app.layout=html.Div([
    html.Div(className='row', children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['JKUAT','DeKUT', 'UON', 'KCA'], value='JKUAT', style={'width':'250px'}),
        
        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['GEGIS', 'CIVIL', 'MARINE', 'ELECTRICAL'],
                     ['Procurement', 'BBIT','BMA','Enterpreneurship'],
                     multi=True, style={'width':'250px'}),
        
        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(options=['COETEC','COHES','COHRED'],
                       value='COHES',
                       style={'padding':10,'flex':1}),
    ]),
    html.Div(className='row', children=[
        html.Label('Check Boxes'),
        dcc.Checklist(['SPA','EMB','ELB','NSC'],
                      ['IEET', 'NCLB','BEED']),

        html.Br(),
        html.Label('Whats your age?'),
        dcc.Input(value='enter text', type='text')
    ], style={'padding':10, 'flex':1})
])

if __name__ == '__main__':
    app.run(debug=True, port=4050)
