piCAN
----- 

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/yacotaco/piCAN.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yacotaco/piCAN/context:python)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/yacotaco/piCAN.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yacotaco/piCAN/context:javascript)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/yacotaco/piCAN.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yacotaco/piCAN/alerts/)

<img src="resources/webapp.jpg" width="30%">

Revolving can controlled by users via Flask web app.

Access to hardware can be granted to users one by at a time so website implements virtual queue.

Actions performed by user can be seen on webcam view.

### Software setup:

`main_server.py` web app adds user to queue and provides control buttons and view

`main_pi.py` Flask server on Raspberry Pi which provides access to hardware (REST API)

### Hardware setup:

- Raspberry Pi 2B+
- Raspberry Pi camera
- Pololu MP6500 Stepper Motor Driver
- Vexta px244m-01a-c7 

<img src="resources/hardware.jpg" width="40%">
