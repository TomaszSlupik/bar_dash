import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div (children=
                       [
                           html.H2("Sprzedaż w latach 2017 do 2019 r."),
                           dcc.Graph(
    figure=go.Figure ([
        go.Bar(
        x=['2017', '2018', '2019'],
        y=[150, 209, 90],
        name='lokalnie'
        ),
        go.Bar(
        x=['2017', '2018', '2019'],
        y=[280, 220, 180],
        name='online'
        )
    ])
    
)

])

if __name__ == '__main__':
    app.run_server(debug=True)