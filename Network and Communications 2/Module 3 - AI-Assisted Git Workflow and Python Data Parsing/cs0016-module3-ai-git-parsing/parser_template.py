"""Module 3 combined lab starter.

Complete each function with help from an approved AI tool, then verify every
claim and code change using the supplied unit tests. The files contain only
fictional classroom data.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

# The XML declares this as an unprefixed default namespace on <rpc>, so every NETCONF
# element below it carries the namespace even though no element names a prefix. A local
# prefix is bound here because ElementTree cannot search for an unprefixed default.
NETCONF_NAMESPACE = "urn:ietf:params:xml:ns:netconf:base:1.0"
_NETCONF = {"nc": NETCONF_NAMESPACE}


def _required_text(parent: ET.Element, path: str) -> str:
    """Return the stripped text of one required NETCONF element, or explain what is missing."""
    element = parent.find(path, _NETCONF)
    if element is None:
        raise ValueError(f"required NETCONF element {path!r} is missing")
    if element.text is None:
        raise ValueError(f"required NETCONF element {path!r} has no text content")
    return element.text.strip()


def parse_xml(path: str | Path) -> dict:
    """Return default_operation and test_option from the NETCONF-style XML."""
    root = ET.parse(path).getroot()
    edit_config = root.find("nc:edit-config", _NETCONF)
    if edit_config is None:
        raise ValueError("required NETCONF element 'nc:edit-config' is missing")
    return {
        "default_operation": _required_text(edit_config, "nc:default-operation"),
        "test_option": _required_text(edit_config, "nc:test-option"),
    }


def parse_json(path: str | Path) -> dict:
    """Return site, device_count, enabled_devices, and roles from the JSON."""
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    devices = data["devices"]
    return {
        "site": data["site"],
        "device_count": len(devices),
        # "enabled" arrives as a real Python bool, so a truthiness test is safe here.
        "enabled_devices": [device["hostname"] for device in devices if device["enabled"]],
        # dict.fromkeys de-duplicates while keeping order of first appearance. A set would
        # de-duplicate too, but its iteration order is not stable between interpreter runs.
        "roles": list(dict.fromkeys(device["role"] for device in devices)),
    }


def parse_yaml(path: str | Path) -> dict:
    """Return name, approved, duration_minutes, devices, and action from YAML."""
    with open(path, encoding="utf-8") as handle:
        # safe_load resolves only standard YAML tags, so the document cannot construct
        # arbitrary Python objects the way the unsafe loader can.
        data = yaml.safe_load(handle)
    # "window" is a nested mapping, while "devices" and "action" sit at the top level.
    window = data["window"]
    return {
        "name": window["name"],
        "approved": window["approved"],
        "duration_minutes": window["duration_minutes"],
        # Copied so a caller cannot mutate the list held by the parsed document.
        "devices": list(data["devices"]),
        "action": data["action"],
    }


def build_summary(xml_path: str | Path, json_path: str | Path, yaml_path: str | Path) -> dict:
    """Combine the three parser results into one dictionary."""
    # Each value comes from its own file. The YAML device list and the JSON enabled-device
    # list happen to hold the same two hostnames, so the sources are kept strictly separate.
    return {
        "xml": parse_xml(xml_path),
        "json": parse_json(json_path),
        "yaml": parse_yaml(yaml_path),
    }


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    summary = build_summary(
        base / "network_config.xml",
        base / "devices.json",
        base / "maintenance.yaml",
    )
    print(json.dumps(summary, indent=2))
