from astral import LocationInfo
from astral.sun import sun
from datetime import date
import pytz
import pyautogui
import time

# Define Melbourne's location
city = LocationInfo("Melbourne", "Australia", "Australia/Melbourne", -37.8136, 144.9631)

# Timezone object for Melbourne
melbourne_tz = pytz.timezone(city.timezone)

# Predefined days of the month
days_of_month = [5, 10, 15, 20, 25, 30]

# Year to calculate
year = 2025

time.sleep(3) #Delay to allow window switching

# Print tab-separated table header
print("Date\tSunrise (hrs)\tSunset (hrs)\tDaylight Hours")

# Generate data for each required date
for month in range(1, 13):  # Loop through months
    for day in days_of_month:
        try:
            current_date = date(year, month, day)
            s = sun(city.observer, date=current_date)

            # Convert sunrise and sunset times to Melbourne local time
            sunrise = s["sunrise"].replace(tzinfo=pytz.utc).astimezone(melbourne_tz)
            sunset = s["sunset"].replace(tzinfo=pytz.utc).astimezone(melbourne_tz)

            # Convert to decimal hours
            sunrise_decimal = sunrise.hour + (sunrise.minute / 60)
            sunset_decimal = sunset.hour + (sunset.minute / 60)

            # Compute total daylight hours
            daylight_hours = sunset_decimal - sunrise_decimal

            # Print tab-separated values
            print(f"{current_date}\t{sunrise_decimal:.2f}\t{sunset_decimal:.2f}\t{daylight_hours:.2f}")

            #Type values in word document
            pyautogui.write(f"{daylight_hours:.2f}", interval=0.05)
            pyautogui.press('down')

        except ValueError:
            continue  # Skip invalid dates (e.g., Feb 30)
