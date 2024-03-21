# Run this app with `python app.py` and
# visit http://127.0.0.1:3050/ in your web browser.

from dash import Dash, dcc, html

#initialise the app
app=Dash(__name__)

markdown_text='''
# Dash and Markdown - a pip ;)
Dash apps **can be written in Markdown**. Dash uses the [CommonMark](http://commonmark.org/) 
specification of Markdown.

10 Markdown concepts are discussed here within [_examples_][1]. 

Is this the first time you have been introduced to Markdown? You're home.  

   > ### Did you know?
   > Why do programmers prefer dark mode?
   >
   > *Because light attracts bugs!* **Ha...!**

[1]:(https://commonmark.org/help/tutorial/index.html)
'''

app.layout=html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run(debug=True, port=3050)
