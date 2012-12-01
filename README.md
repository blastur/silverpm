silverpm - Python interface to Gembird Silvershield power manager devices
-------------------------------------------------------------------------------
This is a simple python-script to set & get the status of each outlet for the
Gembird silvershield power manager.

Credits go out to the sispmctl [http://sispmctl.sourceforge.net] project for 
all the protocol details. If you need more advanced features than just turning
outlets on or off, check it out.

Run the script without any parameters for detailed usage help.

Known limitations:
==================

- Currently supports ONE connected device, if multiple devices are present in 
the system, the first found will be used.

- Only tested with the 4 outlet Silvershield power manager. There are several
other similar models, which may or may not work. If you wish to try them out,
instanciate the power_manager() class with a different USB product ID.

- Does not support hardware timer schedule.

Dependencies:
=============
- Python 3.x (2.x is unsupported, but may work)
- pyusb 1.x (http://sourceforge.net/projects/pyusb/)
