Servos
======

XRP has two ports for connecting servos. In software, they are represented by obejects `servo_one` and `servo_two`.
You can use the function below to control the servos; e.g. use `servo_one.set_angle(100)` to set servo 1 to middle position.

.. function:: set_angle(angle)

   Sets servo  to given position (in degrees). Position ranges between 0 and 200;
   value of 100 corresponds to middle (neutral) position.


   **Warning**: please remember that if a servo is unable to reach the set
   position because of some mechanical obstacle (e.g., grabber claws can not
   fully close because there is an object between them), it will keep trying,
   drawing significant current. This can lead to servo motor overheating quickly;
   it can also lead to voltage drop of XRP battery, interfering with
   operation of motors or other electronics. Thus, it is best to avoid such
   situtations.

.. function:: free()
  
    Allows the servo to spin freely without holding position

