import tkinter as tk
import obd

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
width=25, height=10 )
label1 = tk.Label(master=frame1, text=keys[1], fg="white", bg="DimGray",
width=25, height=10 )
label2 = tk.Label(master=frame2, text=keys[2], fg="white", bg="DimGray",
width=25, height=10 )
label3 = tk.Label(master=frame3, text=keys[3], fg="white", bg="DimGray",
width=25, height=10 )
label4 = tk.Label(master=frame4, text=keys[4], fg="white", bg="DimGray",
width=25, height=10 )
label5 = tk.Label(master=frame5, text=keys[5], fg="white", bg="DimGray",
width=25, height=10 )

# Add label to the top of each frame
label0.pack(fill=tk.BOTH, expand=1, )
label1.pack(fill=tk.BOTH, expand=1, )
label2.pack(fill=tk.BOTH, expand=1, )
label3.pack(fill=tk.BOTH, expand=1, )
label4.pack(fill=tk.BOTH, expand=1, )
label5.pack(fill=tk.BOTH, expand=1, )

window.mainloop()
