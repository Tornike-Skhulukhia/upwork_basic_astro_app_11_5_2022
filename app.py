from itertools import count
from dash import Dash, html, dcc, Input, Output

from datetime import datetime, timedelta

app = Dash(__name__)

COUNTRIES_AND_CITIES = {
    "Georgia": [
        "Tbilisi",
        "Rustavi",
        "Batumi",
        "Kutaisi",
        "Zugdidi",
        "Telavi",
    ],
    "India": [
        "Kavalur",
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Ahmedabad",
        "Chennai",
        "Kolkata",
        "Surat",
        "Pune",
    ],
}

TIME_FORMAT_FOR_FRONT = "%d.%m.%Y %H:%M:%S"


def _get_background_style_based_on_time(datetime_obj):
    if 5 <= datetime_obj.hour <= 20:
        # day
        background_color = "white"
        text_color = "black"
    else:
        # night
        background_color = "black"
        text_color = "white"

    styles = {
        "background": background_color,
        "color": text_color,
        "width": "100vw",
        "height": "100vh",
        "overflow": "hidden",
        "position": "absolute",
        "left": "0",
        "top": "0",
        "transition": "all ease-in-out 500ms",
    }

    # print(f"Returning {styles=}")

    return styles


def _get_current_time_in(country, city):
    """
    Temporary implementation, add real data later
    """
    if country == "Georgia":
        res = datetime.today()

        if city == "Rustavi":
            res += timedelta(hours=5)

        if city == "Kutaisi":
            res -= timedelta(hours=5)

    else:
        if city == "Chennai":
            res = datetime(2022, 5, 11, 0, 0)
        else:
            res = datetime.today() + timedelta(hours=12)

    return res


app.layout = html.Div(
    id="outer_div",
    children=[
        html.H1(
            id="h1",
            children="Select city and country to view results",
            style={"textAlign": "center"},
        ),
        html.Div(
            id="",
            children=[
                dcc.Dropdown(
                    list(COUNTRIES_AND_CITIES.keys()),
                    value=None,
                    placeholder="Select Country",
                    id="selected_country",
                ),
                html.Br(),
                dcc.Dropdown(
                    options=[],
                    value=None,
                    placeholder="Select City",
                    id="selected_city",
                ),
                html.Br(),
                html.H1(id="current_selections_text", style={"textAlign": "center"}),
                html.Br(),
            ],
            style={"width": "80%", "margin": "auto"},
        ),
    ],
)


@app.callback(
    Output(component_id="selected_city", component_property="options"),
    Input(component_id="selected_country", component_property="value"),
)
def update_dropdown_list_of_cities_on_country_change(country):
    return COUNTRIES_AND_CITIES.get(country, [])


@app.callback(
    Output(component_id="current_selections_text", component_property="children"),
    Output(component_id="outer_div", component_property="style"),
    Input(component_id="selected_country", component_property="value"),
    Input(component_id="selected_city", component_property="value"),
)
def update_selection_text(country, city):
    city_time = _get_current_time_in(
        country=country,
        city=city,
    )

    if country and city and (city in COUNTRIES_AND_CITIES[country]):
        output_1_text = (
            f"Time in {city}, {country} is {city_time.strftime(TIME_FORMAT_FOR_FRONT)}"
        )
    else:
        output_1_text = ""

    output_2_styles = _get_background_style_based_on_time(city_time)

    return output_1_text, output_2_styles


if __name__ == "__main__":
    app.run_server(debug=True)
