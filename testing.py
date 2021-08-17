import tkinter as tk
import obd

window = tk.Tk()
window.title("OBDII Reader")
window.configure(bg="Gray")

#c = obd.commands['RPM']
measurement_cmds = {
    "Speed": "SPEED",
    "RPM": "RPM",
    "Coolant Temp": "COOLANT_TEMP",
    "Oil Temp": "OIL_TEMP",
    "Throttle Position": "THROTTLE_POS",
    "Run Time": "RUN_TIME_MIL",
}
"""
frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5, width=250, height=250)
frame.pack()

lbl_display = tk.Label(
    master=frame,
    text="RPM",
    fg="white",
    bg="DimGray",
    width= 5,
    height=4,
)
lbl_display.pack(side=tk.LEFT)
"""

val_cnt = 0
for i in range(3):
    window.rowconfigure(i, weight=1, minsize=75)

    for j in range(2):
        window.columnconfigure(j, weight=1, minsize=50)
        keys = list(measurement_cmds.keys())
        val_text = keys[val_cnt]

        frame = tk.Frame(
            master=window,
            relief=tk.RIDGE,
            borderwidth=2,
        )
        frame.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
        lbl_display = tk.Label(
            master=frame,
            text=val_text,
            fg="white",
            bg="DimGray",
            width=25,
            height=10,
        )
        lbl_display.pack(fill=tk.BOTH, expand=1)
        val_cnt += 1

window.mainloop()
