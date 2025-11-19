def control_traffic(light_color):
    light_color = light_color.lower()
    if light_color == "red":
        return "STOP: All vehicles Stop."
    elif light_color == "yellow":
        return "CAUTION: Proceed carefully"
    elif light_color == "green":
        return "GO: Vehicles move."
    else:
        return "ERROR: Invalid traffic light color."


if __name__ == "__main__":
    color = input("Enter the traffic light color (red/yellow/green): ")
    action = control_traffic(color)
    print(action)
