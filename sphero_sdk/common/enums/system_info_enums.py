#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x11-system_info.json
# Device ID:          0x11
# Device Name:        system_info
# Timestamp:          03/31/2020 @ 21:00:11.799967 (UTC)

from enum import IntEnum


class CommandsEnum(IntEnum): 
    get_main_application_version = 0x00
    get_bootloader_version = 0x01
    get_board_revision = 0x03
    get_mac_address = 0x06
    get_stats_id = 0x13
    get_processor_name = 0x1F
    get_sku = 0x38
    get_core_up_time_in_milliseconds = 0x39
