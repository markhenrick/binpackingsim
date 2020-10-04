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
    # TODO proper interface with graphical output
    param_drive_sizes = [ 12, 16, 12, 7 ]
    param_file_size = 4
    param_strategy = strategies.strategy_first

    drives = simulate(param_drive_sizes, param_file_size, param_strategy)
    print("\n".join(map(Drive.__str__, drives)))