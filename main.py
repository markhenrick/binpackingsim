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
    param_drive_sizes = [ 1000, 4000, 4000, 2000 ]
    param_file_size = 4
    param_strategy = strategies.strategy_least_used_space
    
    drives = simulate(param_drive_sizes, param_file_size, param_strategy)

    fig, ax = plt.subplots()
    for i, drive in enumerate(drives):
        print(drive)
        ax.plot(drive.graph_absolute_free(), label = f'Drive {i} ({drive.size()})')
    ax.set_title(param_strategy.__name__) 
    ax.set_xlabel(f"No. files of size {param_file_size} stored across all drives")
    ax.set_ylabel("Free space")
    ax.legend()
    plt.show()