# Matplotlib practice scripts

A small collection of standalone Matplotlib demos: line plots, scatter plots, and random walk visualizations.

## Requirements
- Python 3.10+ (likely works on older 3.x)
- matplotlib

Install:
```bash
python -m pip install matplotlib
```

## IMPORTANT
Some scripts loop and prompt:
```text
Make another walk? (y/n):
```

## Scripts
- `mpl_squares.py` - line plot of square numbers.
- `scatter_squares.py` - scatter plot of square numbers with a color map.
- `cubes.py` - line plot of cubes.
- `scatter_qubes.py` - scatter plot of cubes with a color map.
- `random_walk.py` - RandomWalk class for 2D walks.
- `rw_visual.py` - scatter visualization of `RandomWalk`.
- `molecural_motion.py` - line visualization of `RandomWalk`.
- `modified_rw.py` - alternative random walk with larger step sizes.
- `modified_rwvisual.py` - scatter visualization of `MRandomWalk`.
- `practicing_matplotlib.py` - bar chart of two D6 dice rolls (depends on `die.py`, which is not in this folder).

## Run
Each file is standalone:
```bash
python mpl_squares.py
```

## Notes
- `practicing_matplotlib.py` expects a `die.py` with a `Die` class 
