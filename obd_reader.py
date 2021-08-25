import tkinter as tk
import obd


obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD('\\.\\COM5')  # auto-connects to USB or RF port

window = tk.Tk()
window.title("OBDII Reader")
window.configure(bg="Gray")

# c = obd.commands['RPM']
measurement_cmds = {
    "Speed": "SPEED",
    "RPM": "RPM",
    "Coolant Temp": "COOLANT_TEMP",
    "Oil Temp": "OIL_TEMP",
    "Throttle Position": "THROTTLE_POS",
    "Run Time": "RUN_TIME_MIL",
}

# Values to display in telemetry
speed_val = "0 mph"
rpm_val = "0 rpm"


# Configure weights on dimmensions for each cell used when resisigning window
window.rowconfigure(0, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=75)
window.columnconfigure(0, weight=1, minsize=50)
window.columnconfigure(1, weight=1, minsize=50)

# Create 6 frames to display telemetry
frame0 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame1 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame2 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame3 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame4 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame5 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)

# Pack the frames into a grid of 3 rows 2 columns
frame0.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
frame1.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")
frame2.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
frame3.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
frame4.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
frame5.grid(row=2, column=1, padx=1, pady=1, sticky="nsew")

keys = list(measurement_cmds.keys())
assert len(keys) == 6

# Create labels for each telemetry frame
label0 = tk.Label(master=frame0, text=keys[0], fg="white", bg="DimGray",
width=25, height=5 )
label1 = tk.Label(master=frame1, text=keys[1], fg="white", bg="DimGray",
width=25, height=5 )
label2 = tk.Label(master=frame2, text=keys[2], fg="white", bg="DimGray",
width=25, height=5 )
label3 = tk.Label(master=frame3, text=keys[3], fg="white", bg="DimGray",
width=25, height=5 )
label4 = tk.Label(master=frame4, text=keys[4], fg="white", bg="DimGray",
width=25, height=5 )
label5 = tk.Label(master=frame5, text=keys[5], fg="white", bg="DimGray",
width=25, height=5 )

# Add label to the top of each frame
label0.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label1.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label2.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label3.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label4.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label5.pack(fill=tk.BOTH, expand=1, side=tk.TOP)

# Create label for values of each cell
val_label0 = tk.Label(master=frame0, text=speed_val, fg="white", bg="DimGray",
width=25, height=2 )
val_label1 = tk.Label(master=frame1, text=rpm_val, fg="white", bg="DimGray",
width=25, height=2 )

# Add labels with the values of each cell
val_label0.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
val_label1.pack(fill=tk.BOTH, expand=1, side=tk.TOP)

# Methods to update telemetry values


def update_speed():
    global speed_val
    cmd = obd.commands.SPEED  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        speed_val = str(response.value.to('mph').magnitude) + " mph"

    val_label0.config(text=str(speed_val))  # Update label with next text.

    # calls update_label function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_speed)


def update_rpm():
    global rpm_val
    cmd = obd.commands.RPM  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        rpm_val = str(response.value.magnitude) + " rpm"

    val_label1.config(text=str(rpm_val))  # Update label with next text.

    # calls update_label function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_rpm)


update_speed()
update_rpm()
window.mainloop()
