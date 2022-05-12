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
