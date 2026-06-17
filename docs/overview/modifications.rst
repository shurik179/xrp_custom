Custom modifications
====================  
Better wheels
-------------
I made new wheels which work with Pololu's silicone tires https://www.pololu.com/product/3409. 


They have same diameter as original wheels, so they can be used without any modifications to the rest of the chassis.
Design files are here: https://www.printables.com/model/1275321-wheel-for-xrp-robot-pololu-tires

Display board
-------------
This add-on board contains a 135x240 TFT SPI display, 2 user buttons, a large on/off switch, and two neopixels. It plugs into the headers of the XRP controller. 


Source files are in `github <https://github.com/shurik179/XRPdisplay>`__, and full documentation at https://xrpdisplay.readthedocs.io/

Custom chassis
---------------
My final modification is creating a custom chassis for the robot. This is work in progress.

This chassis has the following features:

* Smaller size
* Uses two 18650 batteries
* Design in Fusion 360: https://a360.co/43SxnfM

Printable files: https://www.printables.com/model/1286151-small-xrp-frame

You will need:

* The XRP kit: controller, motors, wiring, sensors, caster balls, o-rings for tires
* The chassis itself (3d printed)
* Battery clip (3d printed)
* Two copies of controller support brackets (3d printed)
* Two wheels (3d printed - either  original from XRP kit or the customized ones above)
* Four M3 screws (8mm long - not longer!)

To power the chassis, you have two options: 

* Option 1: Two 18650 Li-Ion batteries and a holder. You will need to find a holder that provides barrel connector, e..g `this one <https://www.aliexpress.us/item/2255801007364672.html>`__  from AliExpress. 
* Option2: Alternatively, you can use a 2s (7.4V) Li-Ion or LiPo battery pack. The pack should be no larger than 70x40x19mm. I recommend using a pack which contains 2 18650 batteries wrapped together,  e.g. this one from Amazon, instead of a LiPo battery pack (which contains soft pouches).
You will need either to replace the connector (warning: replacing connector on a live battery requires great caution; any mistake can result in fire or explosion) or make an adapter from whatever connector is provided by the pack to the 5.5x2.1 mm barrel jack

Option 1 is easier and safer, but it requires you to remove the batteries every time you need to recharge them, which is annoying. Option 2 allows you to charge the batteries in place. 

