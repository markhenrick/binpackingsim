#!/usr/bin/env python3
from drive import Drive
import strategies

def simulate(drive_sizes, file_size, strategy):
    drives = list(map(lambda drive_size: Drive(drive_size), drive_sizes))
    candidates = list(filter(lambda drive: drive.free() >= file_size, drives))
    while candidates:
        for drive in drives:
            drive.tick()
        selection = strategy(candidates)
        selection.store(file_size)
        if selection.free() < file_size:
            candidates.remove(selection)
    return drives

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use("tkagg")

    # TODO runtime input, GUI
    param_drive_sizes = [ 12, 16, 12, 7 ]
    param_file_size = 4
    param_strategy = strategies.strategy_high_water
    
    drives = simulate(param_drive_sizes, param_file_size, param_strategy)

    fig, ax = plt.subplots()
    for i, drive in enumerate(drives):
        print(drive)
        ax.plot(drive.graph_relative(), label = f'Drive {i} ({drive.size()})')
    ax.set_title(param_strategy.__name__) 
    ax.set_xlabel("No. files stored")
    ax.set_ylabel("Usage (relative)")
    ax.legend()
    plt.show()