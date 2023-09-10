"""Constants for the echonetlite integration."""
from homeassistant.const import (
    CONF_ICON,
    CONF_TYPE,
    CONF_SERVICE,
    CONF_SERVICE_DATA,
    CONF_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_GAS,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_VOLTAGE,
    PERCENTAGE,
    VOLUME_CUBIC_METERS,
    DEVICE_CLASS_BATTERY,
)
from homeassistant.components.sensor import ATTR_STATE_CLASS, SensorStateClass
from pychonet.HomeAirConditioner import (
    ENL_HVAC_MODE,
    ENL_FANSPEED,
    ENL_AIR_VERT,
    ENL_AIR_HORZ,
    ENL_AUTO_DIRECTION,
    ENL_SWING_MODE,
    FAN_SPEED,
    AIRFLOW_VERT,
    AIRFLOW_HORIZ,
    AUTO_DIRECTION,
    SWING_MODE,
)
from pychonet.EchonetInstance import ENL_STATUS, ENL_ON, ENL_OFF

DOMAIN = "echonetlite"
CONF_STATE_CLASS = ATTR_STATE_CLASS
CONF_ENSURE_ON = "ensureon"
CONF_OTHER_MODE = "other_mode"
CONF_FORCE_POLLING = "force_polling"
CONF_ON_VALUE = "on_val"
CONF_OFF_VALUE = "off_val"
CONF_DISABLED_DEFAULT = "disabled_default"
CONF_MULTIPLIER = "multiplier"
CONF_MULTIPLIER_OPCODE = "multiplier_opcode"
CONF_MULTIPLIER_OPTIONAL_OPCODE = "multiplier_optional_opcode"
CONF_ICON_POSITIVE = "icon_positive"
CONF_ICON_NEGATIVE = "icon_negative"
CONF_ICON_ZERO = "icon_zero"
DATA_STATE_ON = "On"
DATA_STATE_OFF = "Off"
TYPE_SWITCH = "switch"
TYPE_DATA_DICT = "type_data_dict"
TYPE_DATA_ARRAY_WITH_SIZE_OPCODE = "type_data_array_with_size_opcode"
SERVICE_SET_ON_TIMER_TIME = "set_on_timer_time"
SERVICE_SET_INT_1B = "set_value_int_1b"
OPEN = "open"
CLOSE = "close"
STOP = "stop"
DEVICE_CLASS_ECHONETLITE_LIGHT_SCENE = "echonetlite_light_scene"
SWITCH_POWER = {DATA_STATE_ON: ENL_ON, DATA_STATE_OFF: ENL_OFF}
SWITCH_BINARY = {DATA_STATE_ON: 0x41, DATA_STATE_OFF: 0x42}
SWITCH_BINARY_INVERT = {DATA_STATE_ON: 0x42, DATA_STATE_OFF: 0x41}

HVAC_SELECT_OP_CODES = {
    0xA0: FAN_SPEED,
    0xA1: AUTO_DIRECTION,
    0xA3: SWING_MODE,
    0xA5: AIRFLOW_HORIZ,
    0xA4: AIRFLOW_VERT,
}

FAN_SELECT_OP_CODES = {0xA0: FAN_SPEED}

COVER_SELECT_OP_CODES = {0xE0: {OPEN: 0x41, CLOSE: 0x42, STOP: 0x43}}

ENL_OP_CODES = {
    0x00: {
        0x11: {
            0xE0: {
                CONF_ICON: "mdi:thermometer",
                CONF_TYPE: DEVICE_CLASS_TEMPERATURE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
        }
    },
    0x01: {
        0x30: {
            0x84: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0x85: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xB4: {  # Humidity setting in dry mode
                CONF_ICON: "mdi:water-percent",
                CONF_TYPE: DEVICE_CLASS_HUMIDITY,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                CONF_SERVICE: [SERVICE_SET_INT_1B],
            },
            0xBA: {
                CONF_ICON: "mdi:water-percent",
                CONF_TYPE: DEVICE_CLASS_HUMIDITY,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xBE: {
                CONF_ICON: "mdi:thermometer",
                CONF_TYPE: DEVICE_CLASS_TEMPERATURE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xBB: {
                CONF_ICON: "mdi:thermometer",
                CONF_TYPE: DEVICE_CLASS_TEMPERATURE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
        },
        0x35: {
            0x84: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0x85: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
        },
    },
    0x02: {
        0x6F: {  # Electric lock
            0xE0: {
                CONF_ICON: "mdi:lock",
                CONF_SERVICE_DATA: SWITCH_BINARY_INVERT,
                CONF_ENSURE_ON: ENL_STATUS,
                CONF_ON_VALUE: "unlock",
                CONF_OFF_VALUE: "lock",
                TYPE_SWITCH: True,
            },
            0xE1: {
                CONF_ICON: "mdi:lock",
                CONF_SERVICE_DATA: SWITCH_BINARY_INVERT,
                CONF_ENSURE_ON: ENL_STATUS,
                CONF_ON_VALUE: "unlock",
                CONF_OFF_VALUE: "lock",
                TYPE_SWITCH: True,
            },
            0xE6: {
                CONF_ICON: None,
                CONF_SERVICE_DATA: SWITCH_BINARY,
                CONF_ENSURE_ON: ENL_STATUS,
                CONF_ON_VALUE: "on",
                CONF_OFF_VALUE: "off",
                TYPE_SWITCH: True,
            },
        },
        0x72: {  # Hot water generator
            0x90: {
                CONF_ICON: "mdi:timer",
                CONF_SERVICE_DATA: SWITCH_BINARY,
                CONF_ENSURE_ON: ENL_STATUS,
                TYPE_SWITCH: True,
            },
            0xE3: {
                CONF_ICON: "mdi:bathtub-outline",
                CONF_SERVICE_DATA: SWITCH_BINARY,
                CONF_ENSURE_ON: ENL_STATUS,
                TYPE_SWITCH: True,
            },
            0xE4: {
                CONF_ICON: "mdi:heat-wave",
                CONF_SERVICE_DATA: SWITCH_BINARY,
                CONF_ENSURE_ON: ENL_STATUS,
                TYPE_SWITCH: True,
            },
            0x91: {  # Sensor with service
                CONF_ICON: "mdi:timer-outline",
                CONF_TYPE: None,
                CONF_SERVICE: [SERVICE_SET_ON_TIMER_TIME],
            },
            0xD1: {  # Sensor
                CONF_ICON: "mdi:thermometer",
                CONF_TYPE: DEVICE_CLASS_TEMPERATURE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                CONF_SERVICE: [SERVICE_SET_INT_1B],
            },
            0xE1: {
                CONF_ICON: "mdi:thermometer",
                CONF_TYPE: DEVICE_CLASS_TEMPERATURE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                CONF_SERVICE: [SERVICE_SET_INT_1B],
            },
            0xE7: {CONF_UNIT_OF_MEASUREMENT: "L"},
            0xEE: {CONF_UNIT_OF_MEASUREMENT: "L"},
        },
        0x79: {
            0xE0: {
                CONF_ICON: "mdi:solar-power-variant-outline",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                CONF_ICON_POSITIVE: "mdi:solar-power-variant",
                CONF_ICON_NEGATIVE: "mdi:solar-power-variant-outline",
                CONF_ICON_ZERO: "mdi:solar-power-variant-outline",
            },
            0xE1: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xE3: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING
            },
            0xE5: {
                CONF_ICON: "mdi:percent",
                CONF_TYPE: PERCENTAGE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xE6: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xE8: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xE9: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
        },
        0x7C: {
            0xC2: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xC4: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xC5: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xCC: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xCD: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xC7: {
                CONF_ICON: "mdi:gas-burner",
                CONF_TYPE: DEVICE_CLASS_GAS,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                CONF_UNIT_OF_MEASUREMENT: "L/h",
            },
            0xC8: {
                CONF_ICON: "mdi:gas-burner",
                CONF_TYPE: DEVICE_CLASS_GAS,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "L",
            },
        },
        0x7D: {
            0xA0: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xA1: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xA2: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xA3: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xA4: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xA5: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xA6: {
                CONF_ICON: "mdi:percent",
                CONF_TYPE: PERCENTAGE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xA7: {
                CONF_ICON: "mdi:percent",
                CONF_TYPE: PERCENTAGE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xA8: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xA9: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xAA: {
                CONF_ICON: "mdi:battery",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xAB: {
                CONF_ICON: "mdi:battery",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xD0: {
                CONF_ICON: "mdi:battery",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xD3: {
                CONF_ICON_POSITIVE: "mdi:battery-arrow-up",
                CONF_ICON_NEGATIVE: "mdi:battery-arrow-down",
                CONF_ICON_ZERO: "mdi:battery",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xD6: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xD8: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
            },
            0xE0: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xE2: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xE4: {
                CONF_ICON: "mdi:battery",
                CONF_TYPE: PERCENTAGE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xE5: {
                CONF_ICON: "mdi:percent",
                CONF_TYPE: PERCENTAGE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xE7: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xE8: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL,
            },
            0xEB: {
                CONF_ICON: "mdi:battery",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xEC: {
                CONF_ICON: "mdi:battery",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
        },
        0x80: {
            0xE0: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "kWh",
                CONF_MULTIPLIER_OPCODE: 0xE2,
            }
        },
        0x81: {
            0xE0: {
                CONF_ICON: "mdi:water",
                CONF_TYPE: VOLUME_CUBIC_METERS,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_MULTIPLIER_OPCODE: 0xE1,
            }
        },
        0x82: {
            0xE0: {
                CONF_ICON: "mdi:gas-burner",
                CONF_TYPE: DEVICE_CLASS_GAS,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_MULTIPLIER: 0.001
            }
        },
        0x87: {
            0xB3: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "kWh",
                TYPE_DATA_ARRAY_WITH_SIZE_OPCODE: 0xB1,
                CONF_MULTIPLIER_OPCODE: 0xC2,
            },
            0xB7: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                TYPE_DATA_ARRAY_WITH_SIZE_OPCODE: 0xB1,
            },
            0xC0: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "kWh",
                CONF_MULTIPLIER_OPCODE: 0xC2,
            },
            0xC1: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "kWh",
                CONF_MULTIPLIER_OPCODE: 0xC2,
            },
            0xC6: {
                CONF_ICON: "mdi:flash",
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xC7: {
                CONF_TYPE: DEVICE_CLASS_CURRENT,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                TYPE_DATA_DICT: ["r_phase_amperes", "t_phase_amperes"],
                CONF_DISABLED_DEFAULT: True,
            },
            0xC8: {
                CONF_TYPE: DEVICE_CLASS_VOLTAGE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                TYPE_DATA_DICT: ["r_sn_voltage", "sn_t_voltage"],
                CONF_DISABLED_DEFAULT: True,
            },
        },
        0x88: {
            0xE0: {
                CONF_ICON: None,
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "kWh",
                CONF_MULTIPLIER_OPCODE: 0xE2,
                CONF_MULTIPLIER_OPTIONAL_OPCODE: 0xD3,
            },
            0xE3: {
                CONF_ICON: None,
                CONF_TYPE: DEVICE_CLASS_ENERGY,
                CONF_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
                CONF_UNIT_OF_MEASUREMENT: "kWh",
                CONF_MULTIPLIER_OPCODE: 0xE2,
                CONF_MULTIPLIER_OPTIONAL_OPCODE: 0xD3,
            },
            0xE7: {
                CONF_ICON: None,
                CONF_TYPE: DEVICE_CLASS_POWER,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
            },
            0xE8: {
                CONF_ICON: None,
                CONF_TYPE: DEVICE_CLASS_CURRENT,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                TYPE_DATA_DICT: ["r_phase_amperes", "t_phase_amperes"],
            },
            0xD3: {CONF_DISABLED_DEFAULT: True},
            0xE1: {CONF_DISABLED_DEFAULT: True},
        },
        0xA3: {
            0xC0: { # Set scene
                CONF_ICON: "mdi:palette",
                CONF_TYPE: DEVICE_CLASS_ECHONETLITE_LIGHT_SCENE,
                CONF_STATE_CLASS: SensorStateClass.MEASUREMENT,
                CONF_SERVICE: [ SERVICE_SET_INT_1B ],
            },
        },
    },
    "default": {
        CONF_ICON: None,
        CONF_TYPE: None,
        CONF_STATE_CLASS: None,
    },
}

ATTR_STATE_ON = "on"
ATTR_STATE_OFF = "off"

FAN_SPEED_OPTIONS = {
    "auto": "Auto",
    "minimum": "Minimum",
    "low": "Low",
    "medium-low": "Medium-Low",
    "medium": "Medium",
    "medium-high": "Medium-High",
    "high": "High",
    "very-high": "Very-High",
    "max": "Max",
}

AIRFLOW_HORIZ_OPTIONS = {
    "rc-right": "Right Center + Right",
    "left-lc": "Left + Left Center",
    "lc-center-rc": "Left + Center + Right Center",
    "left-lc-rc-right": "Left + Left Center + Right Center + Right",
    "right": "Right",
    "rc": "Right Center",
    "center": "Center",
    "center-right": "Center + Right",
    "center-rc": "Center + Right Center",
    "center-rc-right": "Center + Right Center + Right",
    "lc": "Left Center",
    "lc-right": "Left Center + Right",
    "lc-rc": "Left Center + Right Center",
    "left": "Left",
    "left-right": "Left + Right",
    "left-rc": "Left + Right Center",
    "left-rc-right": "Left + Right Center + Right",
    "left-center": "Left + Center",
    "left-center-right": "Left + Center + Right",
    "left-center-rc": "Left + Center + Right Center",
    "left-center-rc-right": "Left + Center + Right Center + Right",
    "left-lc-right": "Left + Left Center + Right",
    "left-lc-rc": "Left + Left Center + Right Center",
}

AIRFLOW_VERT_OPTIONS = {
    "upper": "Upper",
    "upper-central": "Upper Central",
    "central": "Central",
    "lower-central": "Lower Central",
    "lower": "Lower",
}

AUTO_DIRECTION_OPTIONS = {
    "auto": "Auto",
    "non-auto": "Non-Auto",
    "auto-vert": "Auto-vert",
    "auto-horiz": "Auto-horiz",
}

SWING_MODE_OPTIONS = {
    "not-used": "Not Used (Off)",
    "vert": "Vertical",
    "horiz": "Horizontal",
    "vert-horiz": "Vertical-Horizontal",
}

SILENT_MODE_OPTIONS = {
    "normal": "Normal",
    "high-speed": "High Speed",
    "silent": "Silent",
}

HVAC_MODE_OPTIONS = {"as_off": "As Off", "as_idle": "As Idle"}

USER_OPTIONS = {
    ENL_FANSPEED: {"option": "fan_settings", "option_list": FAN_SPEED_OPTIONS},
    ENL_AIR_HORZ: {"option": "swing_horiz", "option_list": AIRFLOW_HORIZ_OPTIONS},
    ENL_AIR_VERT: {"option": "swing_vert", "option_list": AIRFLOW_VERT_OPTIONS},
    ENL_AUTO_DIRECTION: {
        "option": "auto_direction",
        "option_list": AUTO_DIRECTION_OPTIONS,
    },
    ENL_SWING_MODE: {"option": "swing_mode", "option_list": SWING_MODE_OPTIONS},
    ENL_HVAC_MODE: {
        "option": CONF_OTHER_MODE,
        "option_list": [
            {"value": "as_off", "label": "As Off"},
            {"value": "as_idle", "label": "As Idle"},
        ],
    },
}

TEMP_OPTIONS = {
    "min_temp_heat": {"min": 10, "max": 25},
    "max_temp_heat": {"min": 18, "max": 30},
    "min_temp_cool": {"min": 15, "max": 25},
    "max_temp_cool": {"min": 18, "max": 30},
    "min_temp_auto": {"min": 15, "max": 25},
    "max_temp_auto": {"min": 18, "max": 30},
}

MISC_OPTIONS = {CONF_FORCE_POLLING: {"type": bool, "default": False}}
