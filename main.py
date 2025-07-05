# main.py

from map import create_world
from hal import HAL
from gui import GUI
from config import *
import time

def main():
    
    world = create_world()

    
    hal = HAL(world)
    gui = GUI(world)

    
    hal.setV(LINEAR_SPEED)
    hal.setW(0)

    while True:
        
        bumper = hal.getBumperData()
        if bumper["state"]:

            print('Crash detected!!')
            
            hal.setV(0)
            hal.setW(ANGULAR_SPEED)
            t0=time.time()
            while(time.time()-t0<1.0):
                hal.update()
                gui.render(hal.getPose3d(), laser_values=hal.getLaserData()["values"])
                time.sleep(TIME_STEP) 

                
            hal.setW(0)
            hal.setV(LINEAR_SPEED)

        
        hal.update()

        
        laser = hal.getLaserData()["values"]
        gui.render(hal.getPose3d(), laser_values=laser)

        
        time.sleep(TIME_STEP)

if __name__ == "__main__":
    main()
