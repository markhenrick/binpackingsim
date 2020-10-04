from drive import Drive
import random

# strategy :: [Drive] -> Drive
# precondition: ∀ drive ∈ drives · drive.free() >= file_size
# precondition: drives != []
# postcondition: output ∈ drives
# contract: non-mutating

def strategy_random(drives):
    return random.choice(drives)
 
def strategy_first(drives): # AKA fill-up
    return drives[0]

def strategy_most_free_space(drives):
    return max(drives, key = Drive.free)

def strategy_least_free_space(drives):
    return min(drives, key = Drive.free)

def strategy_least_used_space(drives):
    return min(drives, key = Drive.usage_absolute)

def strategy_pfrd(drives):
    weights = map(lambda drive: 1 - drive.usage_relative(), drives)
    return random.choices(drives, weights = weights)[0]

def strategy_high_water(drives):
    hwm = max(drives, key = Drive.size).size() // 2
    selection = None
    while not selection:
        candidates = list(filter(lambda drive: drive.free() > hwm, drives))
        if candidates:
            selection = candidates[0]
        else:
            hwm //= 2
    return selection