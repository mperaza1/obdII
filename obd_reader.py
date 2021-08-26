import tkinter as tk
import obd


# obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD('\\.\\COM5')  # auto-connects to USB or RF port

window = tk.Tk()
window.title("OBDII Reader")
window.configure(bg="DimGray")

# c = obd.commands['RPM']
# Dictionary of "Command Label String" to "OBD library command string"
measurement_cmds = {
    "Speed": "SPEED",
    "RPM": "RPM",
    "Coolant Temp": "COOLANT_TEMP",
    "Intake Temp": "INTAKE_TEMP",
    "Throttle Position": "THROTTLE_POS",
    "Run Time": "RUN_TIME_MIL",
}

# Values to display in telemetry
speed_val = "0 mph"
rpm_val = "0 rpm"
coolant_val = "0 C"
intake_val = "0 C"
throttle_val = "0 degrees"
run_time_val = "0 minutes"
user_command_val = ""


# Configure weights on dimmensions for each cell used when resisigning window
window.rowconfigure(0, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=75)
window.rowconfigure(2, weight=1, minsize=75)
window.rowconfigure(3, weight=1, minsize=75)
window.columnconfigure(0, weight=1, minsize=50)
window.columnconfigure(1, weight=1, minsize=50)

# Create 6 frames to display telemetry
frame0 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame1 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame2 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame3 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame4 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)
frame5 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)

# Create 1 frame for custom command input
frame6 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2,)

# Configure its weights to use grid to pack the frame
frame6.rowconfigure(0, weight=1, minsize=25)
frame6.rowconfigure(1, weight=1, minsize=25)
frame6.rowconfigure(2, weight=1, minsize=25)
frame6.columnconfigure(0, weight=1, minsize=50)
frame6.columnconfigure(1, weight=1, minsize=50)

# Pack the frames into a grid of 4 rows 2 columns
frame0.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
frame1.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")
frame2.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
frame3.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
frame4.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
frame5.grid(row=2, column=1, padx=1, pady=1, sticky="nsew")

# Pack Custom Command frame to span 2 columns
frame6.grid(row=3, column=0, padx=1, pady=1, sticky="nsew", columnspan=2)

# Create label for values of each cell
val_label0 = tk.Label(master=frame0, text=speed_val, fg="white", bg="DimGray",
            width=25, height=2 )
val_label1 = tk.Label(master=frame1, text=rpm_val, fg="white", bg="DimGray",
            width=25, height=2 )
val_label2 = tk.Label(master=frame2, text=coolant_val, fg="white", bg="DimGray",
            width=25, height=2 )
val_label3 = tk.Label(master=frame3, text=intake_val, fg="white", bg="DimGray",
            width=25, height=2 )
val_label4 = tk.Label(master=frame4, text=throttle_val, fg="white", bg="DimGray",
            width=25, height=2 )
val_label5 = tk.Label(master=frame5, text=run_time_val, fg="white", bg="DimGray",
            width=25, height=2 )
val_label6 = tk.Label(master=frame6, text=user_command_val, fg="white", bg="DimGray",
            width=50, height=2 )

# Methods to update telemetry values


def update_speed():
    global speed_val
    cmd = obd.commands.SPEED  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        speed_val = str(int(response.value.to('mph').magnitude)) + " mph"

    val_label0.config(text=str(speed_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_speed)


def update_rpm():
    global rpm_val
    cmd = obd.commands.RPM  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        rpm_val = str(int(response.value.magnitude)) + " rpm"

    val_label1.config(text=str(rpm_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_rpm)


def update_coolant_temp():
    global coolant_val
    cmd = obd.commands.COOLANT_TEMP  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        coolant_val = str(int(response.value.magnitude)) + " C"

    val_label2.config(text=str(coolant_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_coolant_temp)


def update_intake_temp():
    global intake_val
    cmd = obd.commands.INTAKE_TEMP  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        intake_val = str(int(response.value.magnitude)) + " C"

    val_label3.config(text=str(intake_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_intake_temp)


def update_throttle_pos():
    global throttle_val
    cmd = obd.commands.THROTTLE_ACTUATOR  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        throttle_val = str(int(response.value.magnitude)) + " percent"

    val_label4.config(text=str(throttle_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_throttle_pos)


def update_run_time():
    global run_time_val
    cmd = obd.commands.RUN_TIME  # select an OBD command (sensor)
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        run_time_val = str(int(response.value.magnitude)) + " seconds"

    val_label5.config(text=str(run_time_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_run_time)


def update_user_command():
    # String user entered as a command
    global user_command_str
    # Value returned to be displayed
    global user_command_val
    cmd = obd.commands.RUN_TIME  # TODO send custom command using user string
    response = connection.query(cmd)  # send the command, parse the response
    if not response.is_null():
        user_command_val = response.value

    val_label6.config(text=str(user_command_val))  # Update label with next text.

    # calls update function again after 1 second. (1000 milliseconds.)
    window.after(1000, update_user_command)


def set_user_command():
    global user_command_str
    user_command_str = user_command6.get()
    update_user_command()

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

# Label for custom command
label6 = tk.Label(master=frame6, text="Custom Command Entry", fg="white", bg="DimGray",
        width=50, height=3 )
# StringVar object to store user command
user_command6 = tk.StringVar(frame6)
# Text entry widget for user command
entry6 = tk.Entry(master=frame6, textvariable=user_command6, fg="black",
        bg="LightGrey", width=25, relief=tk.GROOVE)
# Button Widget to set user_command
submit_button6 = tk.Button(master=frame6, text='Submit Command', command=set_user_command,
                fg="white", bg="SlateGray", width=25, height=1 )


# Pack label to the top of each frame
label0.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label1.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label2.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label3.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label4.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
label5.pack(fill=tk.BOTH, expand=1, side=tk.TOP)

# Pack custom command cell using grid
label6.grid(row=0, column=0, padx=1, pady=1, sticky="nsew", columnspan=2)
entry6.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
submit_button6.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")


# Pack labels with the values of each cell
val_label0.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
val_label1.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
val_label2.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
val_label3.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
val_label4.pack(fill=tk.BOTH, expand=1, side=tk.TOP)
val_label5.pack(fill=tk.BOTH, expand=1, side=tk.TOP)

val_label6.grid(row=2, column=0, padx=1, pady=1, sticky="nsew", columnspan=2)

# Start Updating each value in real time
update_speed()
update_rpm()
update_coolant_temp()
update_intake_temp()
update_throttle_pos()
update_run_time()

window.mainloop()
