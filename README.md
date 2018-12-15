# silverpm

This is a Python module to the Gembird Silvershield programmable power outlet
strips. The interface allows setting, getting and toggling each individual
outlet.

NOTE: Gembird Silvershield SIS-PMS is no longer produced and is not available
for purchase. The replacement device, EnerGine Programmable Surge Protector
(EG-PMS) has not been tested with this Python module.

Credits go out to the sispmctl [http://sispmctl.sourceforge.net] project for
all the protocol details. If you need more advanced features than just turning
outlets on or off, check it out.

Run the script without any parameters for detailed usage help.

This script was developed for Python 3.x, but should also work for Python 2.x.

## Installation

Install using pip:
```
	$ pip install .
```

If you prefer installing it for your user only, pass the --user argument to pip.

## Known limitations
- Currently supports ONE connected device, if multiple devices are present in
the system, the first found will be used.

- Only tested with the 4 outlet Silvershield power manager. There are several
other similar models, which may or may not work. If you wish to try them out,
instanciate the power_manager() class with a different USB product ID.

- Does not support hardware timer schedule.
