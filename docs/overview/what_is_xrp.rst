Preliminaries: what is  XRP?
============================
XRP is a robotics kit created by consortium of several organizations, including Sparkfun, Worcester Polytechnic Institute, FIRST, and many more; see https://experientialrobotics.org/. It is primarily intended for use in education. 

It has been in beta for about 2 years, but recently (March 2025) they released version 1, which has significant improvements.

Useful links:
-------------

* `Main page <https://experientialrobotics.org/>`__
* `Sparkfun product page <https://www.sparkfun.com/experiential-robotics-platform-xrp-diy-kit.html>`__; 
  you can buy it there or from Digikey (currently, Digikey only stocks beta version)
* `User guide <https://xrpusersguide.readthedocs.io/en/latest/course/introduction.html>`__ (needs updating).
* Hardware - controller: `documentation <https://docs.sparkfun.com/SparkFun_XRP_Controller/hardware_overview/>`__, 
  `pinout <https://docs.sparkfun.com/SparkFun_XRP_Controller/assets/img/XRP-Controller-Expansion-Pinout-Table.jpg>`__, 
  `github <https://github.com/sparkfun/SparkFun_XRP_Controller>`__
* Hardware - 3d printed: `files for 3d printing <https://www.printables.com/model/1216372-xrp-robot-kit>`__, 
  `source CAD (OnShape) <https://cad.onshape.com/documents/9bf1dfe68ee7a0325b55874b/w/ce3df1692e8bea96311ada3c/e/74b13b5b748084e43addbe27?renderMode=0&uiState=69e76dd17e34b23865a6b982>`__
* Software: `online IDE (XRPcode) <https://xrpcode.wpi.edu//>`__, `API docs <https://open-stem.github.io/XRP_MicroPython/>`__, `github <https://github.com/Open-STEM/XRP_MicroPython>`__
* Firmware: Micropython `.uf2 file <https://www.micropython.org/resources/firmware/SPARKFUN_XRP_CONTROLLER-20250415-v1.25.0.uf2>`__  (normally not needed, as the IDE has built-in tools for updating firmware);  in case your firmware is completely messed up, use  flash_nuke .uf2 file that erases the flash memory 
* Some projects using XRP: https://www.printables.com/model/1216372-xrp-robot-kit/related

Features:
---------
XRP is a typical 2-motor small differential drive robot, programmable in micropython. In addition to basic features, it also has:

* Motor encoders
* IMU and code to use it for turns
* Support (connectors and code) for additional motors and servos

Main feature of XPR is that it is easily customizable (unlike, say, Zumo, 3pi+, or Alvik). Chassis is 3d printed (and it has been designed with great care), making it easy to modify; there are numerous attachment points for adding extra actuators or sensors.  

It also comes with a well-supported library and a whole course curriculum, and the price is reasonable - if you are willing to 3d print your own parts, the rest is just $99, and they offer discount to educators/robotics teams, which brings it down to $73. 

