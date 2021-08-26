# obdII Reader

This project provides a GUI to read relevant engine data from your car. It is
compatible with most modern cars that have an OBDII interface. An ELM 327 scan
tool is used in conjunction with the Python-OBD library to query your car's ECU.
We use a Windows 10 computer to run the code as the scan tool used is only
confirmed to work on Windows.

## Requirements
### 1. Scan Tool
An ELM 327 scan tool is the required hardware to use this program. The ELM 327
microcontroller is an open sourced hardware device that is used to send and read
commands from a car's ECU. The Python-OBD library provides a Python API for the
ELM 327 command set in a user friendly manner.

In our experience, bluetooth modules do not work well with the library and cause
the auto connect interface of the library to hang. For our testing we use a
wired scan tool on a Windows computer that has the respective drivers installed.

The following is a link to the scan tool used in this project.

[Wired Scan Tool](https://www.amazon.com/Forscan-Scanner-ELMconfig-FoCCCus-Diagnostic/dp/B07MQ8GHG3/ref=sr_1_10)

Follow the instructions included in the tool to install its drivers.

### 2. Python-OBD Library
Next you must install the Python-OBD library.
Please reference the documentation for usage.

[Python-OBD](https://python-obd.readthedocs.io/)

First, it is recommended that you use a virtual environment for installing all
of the libraries used in this project.

To create a virtual environment in your current directory:  
(Assuming your python3 symlink points to a recent python3 version)

`$ python3 -m venv venv`

Then activate the virtual environment on Windows running the following script

`$ .\venv\Scripts\activate`

Finally to install the Python-OBD library use the following command

`$ pip install obd`

### 3. Configure COM Port

Unfortunately the library's auto-connect feature did not work during our testing
and would hang or not find the right port for pairing with the scan tool. When
working properly, it is supposed to find the COM port the scan tool is connected
to and pair with it automatically.

To work around this we will manually configure the COM port in the startup code.

First connect the scan tool to a USB port on the computer. If drivers are
installed correctly a COM port will be assigned to the device. We will locate
which COM port is assigned to the scan tool.

1. Open up the Control Panel
2. Select "View Devices and Printers" located under "Hardware and Sound"
3. Find the OBDII device, right click and select "Properties"
4. Select the "Hardware" tab

In the Hardware window, the COM port will be listed under "Name".
Take note of the COM port number as we will use this in the code.

Edit the following line with the right COM port number:  
(In this example it is 5)

`connection = obd.OBD('\\.\\COM5')`

Now, the code will manually use the correct COM port instead of trying to
auto connect.

### 4 Run GUI

Now you are ready to use the GUI.
Connect one end of the scanner to your car and the other end to your Windows
laptop. Turn the car on.

Run the program using

`$ python obd_reader.py`
