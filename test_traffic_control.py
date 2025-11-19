from traffic_control import control_traffic


def test_red_light():
    assert control_traffic("red") == "STOP: All vehicles must stop."


def test_yellow_light():
    assert control_traffic("yellow") == "CAUTION: proceed carefully."


def test_green_light():
    assert control_traffic("green") == "GO: Vehicles may proceed"


def test_invalid_color():
    assert control_traffic("blue") == "ERROR: Invalid traffic light color."
