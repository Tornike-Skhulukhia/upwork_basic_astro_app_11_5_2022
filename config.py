# change/add data here if necessary
CITIES_INFO = {
    "India, Kavalur": {
        "timezone": "Asia/Kolkata",
        "coordinates": ("12.5780° N", "78.8130° E"),
    },
    "Georgia, Tbilisi": {
        "timezone": "Asia/Tbilisi",
        "coordinates": ("41.7151° N", "44.8271° E"),
    },
    "Kansas, United States": {
        "timezone": "US/Central",
        "coordinates": ("39.0119° N", "98.4842° W"),
    },
}


# change this text to make time formatted differenty
# like instead of 12.31.2022 to show 31 December 2022
# for formatting info, visit: https://strftime.org/

# TIME_FORMAT_FOR_FRONT = "%d.%m.%Y %H:%M:%S"  # example outpt: 13.05.2022 01:13:11
TIME_FORMAT_FOR_FRONT = "%H:%M:%S"  # example outpt: 01:13:11
