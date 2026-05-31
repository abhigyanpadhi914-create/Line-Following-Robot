from line_follower_robot.sensor import process_sensors
from line_follower_robot.movement import decide_movement

def main():
    sensor_values, active_count = process_sensors()
    robot_action = decide_movement(sensor_values)
    
    print(f"Sensor Values: {sensor_values}")
    print(f"Active Sensors: {active_count}")
    print(f"Robot Action: {robot_action}")

if __name__ == "__main__":
    main()