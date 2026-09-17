"""IT0123 Module 1 starter file.

This program uses only fictional documentation-range IP addresses and performs
no network connections. It intentionally contains several defects for the
AI-assisted debugging activity.
"""

DEVICES = [
    {"name": "edge-router-1", "ip_address": "192.0.2.1", "status": "up", "latency_ms": 12},
    {"name": "core-switch-1", "ip_address": "192.0.2.2", "status": "up", "latency_ms": 150},
    {"name": "branch-router-1", "ip_address": "192.0.2.3", "status": "down", "latency_ms": None},
    {"name": "firewall-1", "ip_address": "192.0.2.4", "status": "up", "latency_ms": 25},
    {"name": "wireless-ap-1", "ip_address": "192.0.2.5", "status": "down", "latency_ms": None},
]


def count_online(devices):
    """Return the number of devices whose status is up."""
    count = 0
    for device in devices:
        if device["status"] == "up":
            count += 1
    return count


def average_online_latency(devices):
    """Return the mean latency of online devices, or 0.0 if none are online."""
    online_latencies = [
        device["latency_ms"]
        for device in devices
        if device["status"] == "up"
    ]
    if not online_latencies:
        return 0.0
    return sum(online_latencies) / len(online_latencies)


def find_slow_devices(devices, threshold=100):
    """Return online devices with latency greater than the threshold."""
    return [
        device
        for device in devices
        if device["status"] == "up" and device["latency_ms"] > threshold
    ]


def classify_device(device, threshold=100):
    """Return OFFLINE, SLOW, or HEALTHY for one device."""
    if device["status"] == "down":
        return "OFFLINE"
    if device["latency_ms"] > threshold:
        return "SLOW"
    return "HEALTHY"


def render_device_lines(devices):
    """Return one formatted report line for every device."""
    lines = []
    for index in range(len(devices)):
        device = devices[index]
        latency = "n/a" if device["latency_ms"] is None else f'{device["latency_ms"]} ms'
        lines.append(
            f'- {device["name"]} | {device["ip_address"]} | '
            f'{device["status"]} | {latency} | {classify_device(device)}'
        )
    return lines


def build_report(devices):
    """Build and return the complete inventory report as a string."""
    slow_devices = find_slow_devices(devices)
    lines = [
        "NETWORK DEVICE INVENTORY REPORT",
        f"Total devices: {len(devices)}",
        f"Online devices: {count_online(devices)}",
        f"Average online latency: {average_online_latency(devices):.2f} ms",
        f"Slow online devices (> 100 ms): {len(slow_devices)}",
    ]
    lines.extend(render_device_lines(devices))
    return "\n".join(lines)


if __name__ == "__main__":
    print(build_report(DEVICES))
