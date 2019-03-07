# MOTUS - The Handheld Security System
## Anthony Pacitto, Dariusz Kulpinski, Winston Vuong 
## CENG 355-0NC
![DeviceImage]()

# BUILD INSTRUCTIONS / How to make a MOTUS device yourself

These are the build instructions on how to make the device. Some items may be more complex to complete, as they need special equipement to complete (ex. PCB builders, CO2 Laser Cutter / Etcher, etc.)

To start off, we should determine what this should look like in the end. More suitably for this project, what should our output look like? Well, fist of all it must detect any security breaches. Such that it can detect if theres motion, or movement of the device itself. In terms of build time for this project, it's a good idea to prepare everything before hand, such as part ordering and source downloads of items and code, pre-manufacturing items and whatsoever. If you are ready to commence the build, you can find a good 3-4 weeks to assemble the entire thing together, as there are many components to review.

## What do we need to start off with?

Several components are required in order to make this project work. All required components for this project is listed below:

- Safety Glasses (Eye protection and other protection you prefer)
- Raspberry Pi 3 B+ Model (Must be I2C ready.)
- SD Card with Raspbian OS (Available Online or install image on own SD card.)
- ADXL345 3 Axis Accelerometer (This is the movement detector. Must be I2C ready.)
- HC-SR501 PIR Sensor Module (This is the motion detector. Must work with GPIo.)
- Standard LED (Used as an indicator for the device)
- 330 Ohm Resistor (To limit voltage on the LED)
- Rapsberry Pi External Camera (For the Photo Component of the device.)
- Breadboarding Platform (Any Size Works)
- USB mouse, USB Keyboard, HDMI cable and HDMI monitor to use the Pi With OR ethernet cable to use the remote desktop function.
- GPIo Cables (male to female connections between board and sensor)
- GPIo Pin Stacking Header (Something that allows you to connect a PCB itself to the Pi)
- 3 Pin Stacking Headers (Used to space the motion sensor from the board)
- Jumper Wires (Used for the PCB component or the breadboarding if preffered)
- Wire stripping / Cutting tools
- Soldering Equipment (Soldering Iron, Lead Free Solder, Proper Ventilation, Wet Sponge, Solder Sucker, etc)
- Printed Circuit Board (PCB. This will be discussed later.)
- PCB design software (Example. Fritzing. This will be discussed later.)
- Device Enclosure (Such as PVC boards. This will be discussed later.)
- Enclosure Design Software (Example, CorelDraw. This will be discussed later.)
- Some means of way to produce the PCB and the enclosure (This will be discussed later.)
- And of course, some money.

The estimated cost of building this device is around $245.95 CAD.

## Phase 1: Testing The Design.

To start off, we need to make sure that we know how to connect our device and how its going to work in the end.

Four connections are required to connect our accelerometer to the raspberry pi. First we need to supply 3.3V, connect the ground, and connect our I2C data bus and clock bus to the approprate SDA and SCL pins on the pi.
Three connections are required to connect the motion sensor to the pi. We need a 5V connection, a ground connection, and a connection to a GPIO pin. For this project, the GPIo pin we will connnect it to is GPIo7.
Two connections are required to connect the LED. A connection to the 5V pin, and to the ground. The Resistor can be connected inline with the LED anywhere.
To connect the camera, simply slide the ribbon cable into the appropriate cable slot on the pi's board.
Below is the breadboard. This is how it is supposed to be connected in the end:
![Breadboard image](https://github.com/pctn0007/Motus/blob/master/BuildInstImages/MOTUS_bb.jpg)
#### Pin locations may vary depending on the manufacturer of the sensor itself.
Basically in the end, your wiring must match the schematic as follows:
![Wiring Schematic](https://github.com/pctn0007/Motus/blob/master/BuildInstImages/MOTUS_schem.jpg)
Once this breadboarding is complete, You have the option to jump towards the Third Phase of the build, which powers on the system, or continue on to the Second Phase to design the circuit board for actual system itself.

## Phase 2: Building a Circuit Board

With our breadboard schematic done, we can now design a circuit board that will eliminate all our wiring in the device. A highly reccomended software for this part is Fritzing. Fritzing is a software that allows you to design a breadboard, wiring diagram, and the circuit board itself with ease.
<br />[Click here to visit Fritzing.org](http://fritzing.org/home/)
<br />Once fritzing is installed, build a breadboard design very similar to the design above. Once designed, a schematic of your board and a PCB template will automatically be generated. All you have to do is simply complete the connections.
<br />For the PCB, make sure that each of the connections are designed to fit the devices, and ensure that they can be soldered on depending on which side the contacts are.
<br />Below is a sample of how the PCB should look like in the end:
![PCB Design](https://github.com/pctn0007/Motus/blob/master/BuildInstImages/MOTUS_pcb.jpg)
<br />[Click here to learn more on how to design a PCB in Fritzing](http://fritzing.org/learning/tutorials/designing-pcb/)
<br />Ensure that the connection to the Pi Header can be soldered on the TOP of the board, and make sure that soldering on the sensor can be done on the BOTTOM of the board. Remember, Yellow lines indicate the TOP, while orange lines indicate the BOTTOM. To connect the bottom and the top together, use VIA'S to link them together. You also have access to the original fritzing file if you want to modify that for yourself. [You can click here to download the fritzing file.](https://github.com/pctn0007/Motus/blob/master/Fritzing_Hardware/MOTUS.fzz)
<br />If you are satisfied with the board design, export the PCB as an Extended Gerber File for manufacturing. If you have access to a PCB builder, you can use that. Otherwise, you need to send these Gerber files to a service that Prints out circuit boards, which may add to your budget.

Once you obtain your circuit board, you can proceed to soldering on the pins. Please ensure that you have proper ventilation for this part, and safety glasses are absolutely mandatory for this part.
[If you need help on soldering, a tutorial can be found here.](https://www.build-electronic-circuits.com/how-to-solder/)
<br />To solder the board, ensure that the sensors pins are soldered on the BOTTOM of the board. Ensure that the PI connectors are soldered on the TOP of the board. To Solder the Vias, take some jumper wire, strip it of its protection and stick it throuhg the via. Solder the jumper on both ends, and cut off the excess. That solders on the via and you linked top to bottom.
<br /> This is an example of how the soldering should be completed:
![Soldering Example]()
Once the board is fully soldered, it's time to move to Phase 3.

## Phase 3: Powering the Accelerometer

In this phase, we will test our design to see if it outputs values and reads from the sensors. This part will be majorly focused on the use of the PI, so this is where the monitor, mouse keyboard and HDMI cable Or Remote Desktop Connection come into play.
If you want to learn more about remote desktop connection and the pi, [you can click here.](http://www.circuitbasics.com/access-raspberry-pi-desktop-remote-connection/)
When you start up your Pi, make sure you complete setup if that has not happened already. The most important part to begin with is to ensure that we can read from our sensor's i2c address. First the Pi must be configured to activate I2C. To do this, go into your Raspberyy Pi Preferences:
![Pi Preferences](https://www.kiwi-electronics.nl/image/data/blog/5/jessie_cli_1.png)

Under your IO, ensure that the I2C interface is switched to on. That completes this step.
The next step is the i2c tools. To install this, open the terminal and type in:
#### sudo apt-get install -y i2c-tools
<br /> Input your credentials and allow the installation to complete. Once that's done, we check if our sensors i2c address is found on the GPIo. Run the following command in the terminal:
#### sudo i2cdetect -y 1
<br /> Running this, you should get the following result:
![GPIo I2C pickup](https://raw.githubusercontent.com/BlueDaroosh/handheldSpedometer/master/Documentation/IMG_9533.JPG)
<br />If you see the address of 0x53, you are all set and the accelerometer is ready. Otherwise you need to go back and see what mistakes you have done.

Let's understand how the code is supposed to work in the end. First of all, when working with I2C, we need to program the system to ensure that it will register and read I2C devices that are connected to the I2C bus. Next thing is how this data should be processed. It depends on how you want to display and store the information. Let's say for example we want to take data from a sensor, store it in a database, and have a mobile device read from that database to display the current values for the accelerometer. Below is some PSEUDO CODE that would demonstrate what we would like to do:
`<https://github.com/BlueDaroosh/handheldSpedometer/blob/master/PseudoCodeAssignment/WriteFromServer.txt>`
`<https://github.com/BlueDaroosh/handheldSpedometer/blob/master/PseudoCodeAssignment/ReadToClient.txt>`

The next part is programming the device itself to take inputs from the sensors. This is written under python, but should be simple to implement. Run Thonny on the pi. Once thonny runs, save a .py file anywhere. Below is a link to the source code.
<br />[Click here to access the source code.](https://github.com/pctn0007/Motus/blob/master/Hardware_Code/MOTUSLOGIC.py)
<br />Also, there is a shell script that is required in order to operate the camera function of the script. The shell script is a call to the raspistill command, and [can be accessed here.](https://github.com/pctn0007/Motus/blob/master/Hardware_Code/MOTUSCAMERA.sh)
<br />Please ensure that the database credentials are modified in the python script so that it connects to the database you configure in Phase 4 of the instructions.
<br />Once you format everything properly, and make sure the syntax is correct, you can run the script. By running the script, the device will search for motion or check for movement. If either are true, the device will emit a warning signal light, and activate the camera. The photo should be accessible under the home directory.
<br /> Feel free to look at the script, and modify it however you please.

## Phase 4: The Database and App

## Phase 5: The Enclosure

Do do the enclosure is totally up to you, but it is highly reccomended so that your components are secured and protected. The example case for this project was made using CorelDraw. Other design softwares can be used as well to create the enclosure.
[This is a link to the example closure, which can be modified to your circuit design.]()
NOTE: This is a coreldraw file, therefore you require coreldraw to edit this file. Unless you do not have a free trial, this may be an additional $600 CAD to the budget. Ridiculous price.
<br />Once you design your enclosure for the circuit, you can take the file and use a locally available CO2 laser etcher or other tool that corresponds to your design. Otherwise you may also require to use a service which will build the enclosure for you, but at an added cost for the budget. Once you get your enclosure parts, build the entire thing together, and that is your final result. Below are images of an example of the final result:
![Enclosure Top]()
![Enclosure Back]()
This marks the end of the project. This entire system is now yours to modify and cherish.

## Final Comments
Motus is a bit of a rough idea, however the entire system can be beneficial to the whole valuable protection scheme. Below are references on how the MOTUS platform was designed and built. MOTUS is under a GNU General Public License, so that it is available for you to use, change, modify or redistribute your modification.

#### Credits and Works Cited. Without these, the project would have not been possible:
Dcube Tech Ventures. (N.D.) 3-AXIS ACCELEROMETER, ADXL345 WITH RASPBERRY PI USING PYTHON. 
Obtained From: https://www.instructables.com/id/3-Axis-Accelerometer-ADXL345-With-Raspberry-Pi-Usi/
<br />AviV1. (N.D.) HOW TO USE THE ADXL345 ON RASPBERRY PI.
Obtained From: https://www.instructables.com/id/how-to-use-the-ADXL345-on-Raspberry-pi/
<br />GPIo: https://www.raspberrypi.org/documentation/usage/gpio/
<br />I2C Wiring: https://www.anstack.com/blog/2016/07/05/accelerometer-intro.html
<br /> Humber College - CENG 317 Hardware Production Tech Course
<br /> Humber College - CENG 355 Capstone Project Course
<br /> Humber School of Applied Technology - Computer Engineering Technology
