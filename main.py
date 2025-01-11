from fasthtml.common import *
from monsterui.all import *
import plotly.express as px
from fh_plotly import plotly2fasthtml, plotly_headers
import pandas as pd
import json

# read files
df = pd.read_csv("src/KE-population-density.csv")
with open('src/kenyan-counties.geojson', 'r') as f:
	counties = json.load(f)

# Create the FastHTML app
app, rt = fast_app(
    hdrs = (
    	plotly_headers,
        Theme.blue.headers(),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css'),
        Script(src='https://unpkg.com/franken-ui@1.1.0/dist/js/core.iife.js', type='module'),
        Script(src='https://unpkg.com/franken-ui@1.1.0/dist/js/icon.iife.js', type='module')),
    pico = True,
    Live = True
)

# simple re-usable layout
def layout(content):
    return Div(
        NavBarContainer(
            NavBarLSide(P('Home')),
            NavBarRSide(P('Menu'))),
        Div(content)
    )

def map_of_kenya():
	fig = px.choropleth_mapbox(
	    df,
	    geojson=counties,
	    locations=df["County"],        # Column in DataFrame that matches GeoJSON `id`
	    color=df["Population_Density"],    # Column to color by
	    featureidkey=counties["COUNTY"],  # GeoJSON key for `id` (adjust as needed)
	    hover_name=df["County"],   # Column for hover information
	    color_continuous_scale="Viridis",  # Color scale
	    mapbox_style="carto-positron",     # Mapbox style
	    zoom=6,                # Initial zoom level
	    center={"lat": -1.286389, "lon": 36.817223},  # Center of Kenya
	    title="Kenya Population by County"
	)

	return plotly2fasthtml(fig)


# Define a simple route
@rt("/")
def home():
    body = Titled(
        "Hello, FastHTML!",
        P("Welcome to your first FastHTML app."),
        A(href="/about")("Learn more"),
        Div(map_of_kenya())
    )
    return layout(body)




@rt("/about")
def about():
    body =  Titled(
        "About This App",
        P("This is a simple app built with FastHTML."),
        A(href="/")("Go back Home"),
    )
    return layout(body)

# Run the app
serve()