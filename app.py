# imports
from datetime import datetime, timedelta

import pytz
from dash import Dash, Input, Output, dcc, html

from config import CITIES_INFO, TIME_FORMAT_FOR_FRONT
from functions import (
    _get_background_style_based_on_time,
    _get_visible_objects_web_elements_for_location,
)

# create dash app to work with
app = Dash(__name__)


# define app/web page should look in browser
app.layout = html.Div(  # outer div for everything that this app has
    id="outer_div",  # id element, needed to identify it and change its style, like dark/white background
    children=[  # all the following elements are children of current outer_div, so they are inside of outer_div element
        # page header text
        html.H1(id="h1", children="Select city and country to view results"),
        html.Div(  # another div, but in previous div
            id="content",  # id is needed to change style in assets/index.cee file
            children=[
                # actual dropdown on page
                dcc.Dropdown(
                    options=list(CITIES_INFO.keys()),  # options in dropdown
                    value=None,  # selected by default when page loads(None means blank, or no selection)
                    placeholder="Select City",
                    id="selected_city",
                ),
                html.H1(id="current_selections_text"),
                html.Div(id="visible_objects_div"),
            ],
        ),
    ],
)


# code after this will automatically run by Dash for us
@app.callback(
    # we want to change following elements on page
    Output(component_id="current_selections_text", component_property="children"),
    Output(component_id="outer_div", component_property="style"),
    Output(component_id="visible_objects_div", component_property="children"),
    # every time when element with id selected_city changes (when we select different city)
    Input(component_id="selected_city", component_property="value"),
)
def handle_city_change(city):

    # only show text if some city is selected
    if city:
        # get text to dispay
        timezone_of_city = CITIES_INFO[city]["timezone"]

        city_time = datetime.now().astimezone(pytz.timezone(timezone_of_city))

        output_1_text = f"Time in {city} is {city_time.strftime(TIME_FORMAT_FOR_FRONT)}"

        # get styles for city and time
        output_2_styles = _get_background_style_based_on_time(city_time)

        # get output info for list of objects that are visible
        output_3_visible_objects_web_elements = (
            _get_visible_objects_web_elements_for_location(
                time=city_time, coordinates=CITIES_INFO[city]
            )
        )
    else:
        output_1_text = ""
        output_2_styles = _get_background_style_based_on_time(None)
        output_3_visible_objects_web_elements = ""

    # what we return from this function, will change things that were defined after @app.callback as outputs:

    # output_1_text will change children element of element with id current_selections_text,
    # output_2_styles will change styles of outer_div,
    # output_3_visible_objects_web_elements will change children of visible_objects_div.

    return output_1_text, output_2_styles, output_3_visible_objects_web_elements


if __name__ == "__main__":
    app.run_server(debug=True)
