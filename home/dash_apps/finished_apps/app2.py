import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from django_plotly_dash import DjangoDash

BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"

dd = DjangoDash("app2",
                add_bootstrap_links=True,external_stylesheets=[BS])

dd.layout = html.Div(
    [
        dbc.Alert("This is an alert", color="primary"),
        dbc.Alert("Danger", color="danger"),
        dbc.Checklist(id='check_switch', switch=True, options=[{"label": "An example switch", "value": 1}], value=[0]),
        dbc.Checklist(id='check_check', switch=False, options=[{"label": "An example checkbox", "value": 1}], value=[0]),
        ]
    )

