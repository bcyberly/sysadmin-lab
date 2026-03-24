#!/usr/bin/env python3
# Project: sysadmin-lab - System Inventory Tool
# Purpose: Collect and display system information (OS, CPU, memory)
# Created: 2026-03-24
# Complexity/Performance: O(1) - uses psutil to query kernel stats efficiently

import platform
import psutil
import datetime

def get_system_info() -> dict:
    """
    Gather core system hardware and OS information.

    Returns:
        dict: A dictionary containing hostname, OS details, CPU counts,
              memory statistics, and formatted system boot time.
    """
    # We query virtual_memory once and store it to avoid multiple expensive system calls
    mem = psutil.virtual_memory()

    info = {
        # Using the built-in 'platform' module here because it natively handles
        # OS-level string formatting better across Windows and Linux
        'hostname': platform.node(),
        'os_name': platform.system(),
        'os_release': platform.release(),
        'architecture': platform.machine(),

        # logical=True counts hyperthreaded/virtual cores, which is what the OS schedule tasks on
        'cpu_count_logical': psutil.cpu_count(logical=True),
        # logical=False counts only actual physical hardware cores
        'cpu_count_physical': psutil.cpu_count(logical=False),

        'memory_total': mem.total,
        'memory_available': mem.available,
        'memory_percent': mem.percent,

        # boot_time returns a raw Unix timestamp. We parse it into a datetime object
        # and format it to ISO 8601 standard so it's instantly readable by a human.
        'boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
    }
    return info

def bytes_to_human(bytes_val: float) -> str:
    """
    Convert raw byte values into dynamically scaled human-readable formats.

    Args:
        bytes_val (foat/int): The raw size in bytes

    Returns: 
        str: A formatted string representing the scaled size with its appropiate unit (e.g., '16.00 GB').
    """
    # Using a loop here instead of hardcoded if/elif blocks makes the function
    # highly scalable. It automatically formats to the highest whole unit.
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        # We use 1024 instead of 1000 because operating systems calculate RAM and storage in base-2.
        if bytes_val < 1024:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024

    #Fallback for extremely large data sets (Petabytes)
    return f"{bytes_val:.2f} PB"

def main():
    """
    Main execution block to format and print the system inventory report.
    """
    print("=" * 60)
    print("SYSTEM INVENTORY REPORT")
    print("=" * 60)

    info = get_system_info()

    print(f"Hostname              : {info['hostname']}")
    print(f"OS                    : {info['os_name']} {info['os_release']}")
    print(f"Architecture          : {info['architecture']}")
    print(f"CPU cores (phys)      : {info['cpu_count_physical']}")
    print(f"CPU cores (logical)   : {info['cpu_count_logical']}")
    print(f"Memory total          : {bytes_to_human(info['memory_total'])}")
    print(f"Memory available      : {bytes_to_human(info['memory_available'])}")
    print(f"Memory used           : {bytes_to_human(info['memory_total'] - info['memory_available'])}")
    print(f"Memory percent        : {info['memory_percent']}%")
    print(f"Boot time             : {info['boot_time']}")
    print("=" * 60)

    
if __name__ == "__main__":
    main()