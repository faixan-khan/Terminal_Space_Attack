# Space-Invaders
    A simple python 2d game with pygame
    
# Prerequisites
   * python 3.0
   * pygame(Install using pip3 install pygame)
   
    
### Features
      Spaceship​ :. The spaceship can only be moved horizontally on Row number 1.
      That is, it’s movement is restricted from 1x1 to 1x8. Move it using key ‘A’ to move
      left and key ‘D’ to move it to the right.
      
      b. Aliens​ : The must be randomly spawned anywhere in rows 8 and 7. A new alien must be spawned every 10
      seconds and each alien must last for 8 seconds, after which it self destructs.
      
      c. Missiles​ : There are two types of missiles:
      
      1. A missile is spawned each time the spacebar is clicked and is always spawned in the (row+1, column)
      block if the spaceship is in (row, column) when spacebar is clicked. For
      example, if the spaceship is in (1, 2) when spacebar is hit, the missile
      spawns in (2,2). The missile must move one row up every second. If a
      missile and alien collide, the alien gets destroyed.
      
      2.This missile is shot when the ‘S’ key is clicked, and unlike the first kind of bullet, will
      move two rows up every second. If this bullet collides with an alien, the
      alien will exist on the board for another 5 seconds. Also slightly change
      the look of the alien when this missile collides with it.
