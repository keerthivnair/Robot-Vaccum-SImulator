# 🤖 Robot Vacuum Simulator

A 2D simulator of an intelligent vacuum-cleaning robot built using **Python + OpenCV**, with realistic physics, sensors (bumpers, laser), and autonomous navigation algorithms like **boustrophedon coverage**.

> This project simulates how a robot navigates and cleans an environment by avoiding obstacles and covering all areas — just like a real Roomba!

---

## 🧠 Features

- ✅ **Realistic robot kinematics**
- ✅ **Obstacle detection** using laser and bumper sensors
- ✅ **Collision handling**
- ✅ **Coverage path algorithms** (random walk, boustrophedon, spiral — in progress)
- ✅ **2D GUI visualization** using OpenCV
- ✅ Custom environment builder (`map.py`)

---

## 🚀 Technologies Used

- 🐍 Python 3
- 🖼️ OpenCV
- 🧮 NumPy
- 💡 Custom-built simulation engine (no ROS or Gazebo)

---


git clone https://github.com/your-username/robot-vacuum-sim.git
cd robot-vacuum-sim
pip install -r requirements.txt
python3 main.py


## 📁 Project Structure


```bash
robot-vacuum-sim/
├── main.py         # Main loop (simulation control)
├── hal.py          # Simulates hardware: motors, sensors, lasers
├── gui.py          # Renders robot + map using OpenCV
├── map.py          # Environment and obstacle setup
├── planner.py      # Path planning and coverage algorithms
├── config.py       # Constants (map size, speed, etc.)


