def decide_movement(sensor_values):
    # Ensure sensor_values has exactly 6 elements to prevent IndexError
    if len(sensor_values) < 6:
        sensor_values = sensor_values + [0] * (6 - len(sensor_values))
    else:
        sensor_values = sensor_values[:6]

    if all(v == 0 for v in sensor_values):
        return "Stop Robot"
    elif all(v == 1 for v in sensor_values):
        return "Junction Detected"
    elif sensor_values[2] == 1 or sensor_values[3] == 1:
        return "Move Forward"
    elif sensor_values[0] == 1 or sensor_values[1] == 1:
        return "Turn Left"
    elif sensor_values[4] == 1 or sensor_values[5] == 1:
        return "Turn Right"
    return "Unknown State"
