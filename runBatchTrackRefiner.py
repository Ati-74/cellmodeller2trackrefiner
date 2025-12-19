import glob
import os
from pathlib import Path
import subprocess
import logging
logging.getLogger('matplotlib').setLevel(logging.WARNING)


if __name__ == '__main__':
    root_folder_path = '../output/sim1/'

    # interval time (unit: minute)
    dt = 3

    # doubling time (unit: minute)
    doubling_time = 20

    for sim_folder in glob.glob(f'{root_folder_path}/*/*/*/*'):

        output_dir = sim_folder

        subprocess.run([
            "trackrefiner-cli",
            "-i", f"{output_dir}/Objects_properties.csv",
            "-n", f"{output_dir}/Object_relationships.csv",
            "-t", str(dt),
            "-d", str(doubling_time),
            "-dc",
            "-k"
        ], check=True)
