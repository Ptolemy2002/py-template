# A file for utility functions used by the uv script. You could put more utilities here as needed.
from datetime import datetime
import os

def get_latest_outputs_dir():
    now: datetime = datetime.now()
    result: str = f"outputs/main/{now.year}/{now.month:02d}/{now.day:02d}"

    # Find the folder representing the latest time with its name
    # Any errors happening here should be fatal, as it indicates the script
    # was not run properly (using the makefile)
    max_time: int = 0
    max_time_folder_name: str | None = None
    with os.scandir(result) as entries:
        for entry in entries:
            if entry.is_dir():
                # Convert HH-MM-SS to seconds
                split = entry.name.split("-")
                time = (int(split[0]) * 3600) + (int(split[1]) * 60) + int(split[2])
                if time >= max_time:
                    max_time = time
                    max_time_folder_name = entry.name

    if max_time_folder_name is not None:
        result = result + f"/{max_time_folder_name}"

    return result

def get_manual() -> str:
    man = "No manual available."
    try:
        with open("man.txt", "r") as f:
            man = f.read()
    except FileNotFoundError:
        # Just go with the default message
        pass

    return man