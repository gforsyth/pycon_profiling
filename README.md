# Python Performance (for Poets, Dreamers, and Doers)

We use Python 3.7 and a few extra packages in this tutorial:

For demonstration/pedagogy:
* jupyter - to present notebooks

For visualization of code profiles:
* snakeviz - Graphical visualization 
* line_profiler - Line-level illustration

## `binder` (option 1)

Just click and run!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gforsyth/pycon_profiling/master)

## `conda` setup (option 2)
You can install all of these in one fell swoop using `conda` and running

```console
conda create -n pycon_poets python=3.7 jupyter snakeviz line_profiler
```

or you can use the provided `environment.yml` file

```console
conda env create -f environment.yml
```

Then, in any terminal session where you'd like to use this environment, start with:

```
source activate pycon_poets
``` 

## `pip` setup (option 3)

If you don't use `conda` you can use `pip` or the tool of your choice to install `jupyter`, `line_profiler`, and `snakeviz`:

```console
pip install jupyter line_profiler snakeviz
```

or use the `requirements.txt` file

```console
pip install -r requirements.txt
```

