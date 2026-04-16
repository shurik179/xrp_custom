.. _buildguide:
*****************
Build guide
*****************


This section documents building the customized XRP robot. 

Needed parts
============

* `DIY XRP kit <https://www.sparkfun.com/experiential-robotics-platform-xrp-diy-kit.html>`__ 
  from Sparkfun. Make sure that you buy this kit and not the beta version! 
* Battery and related parts. You have two choices: 
  - Option A:  using two 18650 LiIon batteries. In this case, you will need two such batteries 
    (buy from a brand name vendor!) and battery holder with barrel connector.  
    We recommend this one: https://www.aliexpress.us/item/2255801007364672.html
  - Option B: a 2s (7.4V) Li-Ion or LiPo battery pack. The pack should be no larger 
    than 70x40x19mm. I recommend using a pack which contains 2 18650 batteries wrapped 
    together,  e.g. `this one <>`__ from Amazon, instead of a LiPo battery pack
    (which contains soft pouches). 
    You  will also need a separate barrel connector; you can cut it off the battery holder 
    included with the kit, or you can buy one separately  
    Note that if you go with this option, you will need to resolder the connector (see next section)
* 3d printed parts; the files are available in 3d printed folder 
  in |github|.  
  - Chassis 
  - Conroller support (2 copies)
  - If you use option A for the battery, you will also need to 3d print the battery clip 
* XRP display, available from FIXME 
* Optional: if you choose to replace stock tires with Pololu ones as discussed here, you 
  will also  need two 3d printed wheels (again, from |github|) and the `Pololu tires 
  <https://www.pololu.com/product/3409>`__  (1 pair).
* Misc: zipties (8 inch or longer), screws (M3, 10mm length, 4 pcs)

Building the battery pack 
=========================


Assembly
========

