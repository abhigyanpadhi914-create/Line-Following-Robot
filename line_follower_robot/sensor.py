def process_sensors():
    user_input = input("Enter 6 sensor values (e.g., 001100): ")
    # Robustly handle spaces if any, and filter to keep only digits
    cleaned_input = "".join(c for c in user_input if c.isdigit())
    
    # Ensure it maps each digit to an integer
    sensor_values = list(map(int, cleaned_input))
    
    # Use filter() to get active sensors (value == 1)
    active_sensors = list(filter(lambda x: x == 1, sensor_values))
    active_count = len(active_sensors)
    
    return sensor_values, active_count
