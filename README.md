# AutoCruise

## Prerequisites
 * CAN Interface - [CANable](https://canable.io)
 * `Can-utils`
 * `Pyserial`
 * `CANard`
 * `libbluetooth-dev`
## Installation

AutoCruise can be installed on any distro of Linux - Debian based is recommended

It is recommended that AutoCruise is isolated in a virtual environment if the device has other uses.
It is also recommmended that AutoCruise runs on root

#### Install AutoCruise
```
git clone https://github.com/blairburns/AutoCruise.git
```

#### Install the dependencies

```
apt-get install can-utils
pip install Pyserial
pip install CANard
```

## Supported Vehicles

* Toyota (Aurion)
