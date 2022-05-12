from dash import html


def _get_background_style_based_on_time(datetime_obj):
    """
    get python datetime object(showing time in some place)
    and return style that we want browser page to have.

    Change numbers after/before <= to decide what times should be
    dark and what times lighter, or add more css styles if necessary.
    """
    # if city is selected and hour is between 5 and 20, white background(day) with black text
    if datetime_obj is not None and 5 <= datetime_obj.hour <= 20:
        # day
        background_color = "white"
        text_color = "black"
    # otherwise, black background, with white text
    else:
        # night
        background_color = "black"
        text_color = "white"

    # some more styles for web element, like using full page
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

    return styles


def _get_visible_objects_web_elements_for_location(time, coordinates):
    """
    Get elements that are visible from given city and time
    in a format that can be directly used in Dash to display it
    """

    info = {
        "Stars": ["star 1", "star 12", "start 23", "star 24"],
        "Planets": [],
        "Satellite (man made)": ["sat 2", "sat 3"],
        "Satellite (natural)": ["nat 4", "nat 5"],
        "Constellation": [],
    }

    # populate result with actual data...

    # convert result into format that Dash can display
    result = []
    for name, list_items in info.items():
        # actual items
        li_elements = []
        for i in list_items:
            li_elements.append(html.Li(i))

        result.append(
            html.Div(
                children=[
                    html.Div(name),
                    html.Ul(li_elements),
                ],
                className="visible_object_div",
            ),
        )

    return result
