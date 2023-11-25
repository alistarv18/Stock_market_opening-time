import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from plyer import notification

icon_path = plt.imread("bursa.ico")

notif_title = "PIATA SE VA DESCHIDE IN CURAND"

# Specify the target opening time
target_opening_time = datetime.strptime("16:30", "%H:%M").time()
target_closing_time = datetime.strptime("23:00", "%H:%M").time()

# Get the current day
dt = datetime.now()
day_of_the_week = dt.isoweekday()

# Get the current time
current_time = datetime.now().time()

# Calculate the time difference
time_difference1 = timedelta(
    hours=target_opening_time.hour - current_time.hour,
    minutes=target_opening_time.minute - current_time.minute
)
time_difference2 = timedelta(
    hours=target_closing_time.hour - current_time.hour,
    minutes=target_closing_time.minute - current_time.minute
)

if day_of_the_week in [1, 2, 3, 4, 5]:
    notif_message = f"Tranzactiile vor incepe in {time_difference1} si se vor termina in {time_difference2}"
else:
    # Dacă time_difference1 este negativ, ajustăm numărul de zile
    days_until_opening = max(0, 7 - day_of_the_week)
    notif_message = f"Tranzactiile vor incepe in {days_until_opening} zile și {time_difference1 + timedelta(days=days_until_opening)} și se vor încheia in {time_difference2}"

notification.notify(
    title=notif_title,
    message=notif_message,
    app_name='Stock Alert',
    app_icon=None,
    timeout=10,
    toast=True
)
