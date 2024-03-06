from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge_weights = 0
    on_bridge = deque([0 for _ in range(bridge_length)]) # [0, 0]
    waiting_trucks = deque(truck_weights)

    while on_bridge:
        time += 1
        on_bridge_weights -= on_bridge.popleft()
        if waiting_trucks:
            if on_bridge_weights + waiting_trucks[0] <= weight:
                truck = waiting_trucks.popleft()
                on_bridge.append(truck)
                on_bridge_weights += truck
            else:
                on_bridge.append(0)

    return time