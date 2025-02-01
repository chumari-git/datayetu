from fasthtml.common import *
from monsterui.all import *
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


df = pd.read_csv('/src/KE-population-density.csv')

# Create the FastHTML app
app, rt = fast_app(
    hdrs = (
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
	return Body(cls='bg-gray-100')(
    Div(cls='flex')(

    	# Side Nav
        Div(cls='w-64 h-screen bg-blue-700 text-white fixed')(
            Div('Side Nav', cls='p-4 font-bold text-lg'),
            Ul(cls='mt-4 space-y-2')(
                Li(A('Dashboard', href='#', cls='block px-4 py-2 hover:bg-blue-500 rounded')),
                Li(A('Profile', href='#', cls='block px-4 py-2 hover:bg-blue-500 rounded')),
                Li(A('Settings', href='#', cls='block px-4 py-2 hover:bg-blue-500 rounded')),
                Li(A('Logout', href='#', cls='block px-4 py-2 hover:bg-blue-500 rounded')),
            )
        ),

        # Main Content
        Div(cls='ml-64 flex-1 p-8')(
            H1('Main Content Area', cls='text-2xl font-bold'),
            P('This is where the main content will go. The side navigation is fixed, and this section is scrollable.', cls='mt-4'),
            Div(content)
        )
    )
)

def map_of_kenya():
	fig = px.choropleth(

    )

# Define a simple route
@rt("/")
def home():
    body = Titled(
        "Hello, FastHTML!",
        P("Welcome to your first FastHTML app."),
        A(href="/about")("Learn more")
    )
    return layout(body)

@rt("/about")
def about():
    body =  Titled(
        "About This App",
        P("This is a simple app built with FastHTML."),
        A(href="/")("Go back Home")
    )
    return layout(body)

# Run the app
serve()