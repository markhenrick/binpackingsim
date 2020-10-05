# binpackingsim
Quick script to simulate different bin packing strategies (e.g. for Unraid or mergerfs)

It's very WIP so parameters are hardcoded for the moment. Tk GUI coming eventually

# Example plots

Scenario: storing 4GB files on a system of (1, 4, 4, 2)TB drives

![First (mergerfs)/Fill-up (Unraid)](example_plots/first.png)

![High-water (Unraid)](example_plots/high_water.png)

![Least-free space (mergerfs)](example_plots/lfs.png)

![Least-used space (mergerfs)](example_plots/lus.png)

![Most-free space (mergerfs/Unraid)](example_plots/mfs.png)

![Percentage-free random distribution (mergerfs)](example_plots/pfrd.png)

![Random (mergerfs)](example_plots/random.png)