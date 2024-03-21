#Run this app with `python app.py` and
# visit http://127.0.0.1:3020/ in your web browser.
#import the necessary modules
from dash import Dash, dash_table, html
import pandas as pd

#connect to the data
df=pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
#initialize the app
app=Dash(__name__)
#define the app layout
app.layout=html.Div([
    html.Div(className='row',children='Our Data', style={'textAlign':'center', 'fontSize':'50px','color':'red'}),
    html.Hr(),
    html.Div(className='row', children=[
        dash_table.DataTable(data=df.to_dict('records'), page_size=10, style_table={'overflowX':'auto'})
    ])
])
#run the app
if __name__ == '__main__':
    app.run(debug=True,port=3020)
