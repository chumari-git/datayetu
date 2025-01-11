from fasthtml.common import *
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

# Initialize FastHTML app
app, rt = fast_app(hdrs=(Script(src="https://cdn.plot.ly/plotly-2.32.0.min.js"),))

# Load GeoJSON data
with open("C:/Users/USER/Desktop/Upwork Projects/DataYetu/src/KENYA GEO JSON.json", "r") as file:
    counties = json.load(file)  # Ensure this is a GeoJSON object, not a DataFrame

# Load population density data
df = pd.read_csv("C:/Users/USER/Desktop/Upwork Projects/DataYetu/src/KE-population-density.csv")

# Function to create the Plotly choropleth figure
def create_figure():
    fig = px.choropleth_mapbox(
        df,
        geojson=counties,
        locations="County",  # Ensure this column matches the GeoJSON's `featureidkey`
        featureidkey="properties.name",  # Match the GeoJSON's key for county names
        color="Population_Density",
        color_continuous_scale="Viridis",
        range_color=(df["Population_Density"].min(), df["Population_Density"].max()),
        mapbox_style="carto-positron",
        zoom=6,
        center={"lat": -1.286389, "lon": 36.817223},  # Center over Kenya
        opacity=0.5,
        labels={"Population_Density": "Population Density"},
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

@rt("/")
def index():
    # Create figure and convert it to HTML
    fig = create_figure()
    return Titled(
        "Population Density by County",
        Div(id="map-container"),
        Script(f"Plotly.newPlot('map-container', {fig.to_json()});")
    )

serve()
