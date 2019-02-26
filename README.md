# README

[![Anaconda-Server Badge](https://anaconda.org/darts-comp-bio/darts_bht/badges/version.svg)](https://anaconda.org/darts-comp-bio/darts_bht)
[![Anaconda-Server Badge](https://anaconda.org/darts-comp-bio/darts_bht/badges/installer/conda.svg)](https://conda.anaconda.org/darts-comp-bio)
[![Anaconda-Server Badge](https://anaconda.org/darts-comp-bio/darts_bht/badges/latest_release_date.svg)](https://anaconda.org/darts-comp-bio/darts_bht)
[![Anaconda-Server Badge](https://anaconda.org/darts-comp-bio/darts_bht/badges/platforms.svg)](https://anaconda.org/darts-comp-bio/darts_bht)
[![Anaconda-Server Badge](https://anaconda.org/darts-comp-bio/darts_bht/badges/downloads.svg)](https://anaconda.org/darts-comp-bio/darts_bht)
[![Anaconda-Server Badge](https://anaconda.org/darts-comp-bio/darts_bht/badges/license.svg)](https://anaconda.org/darts-comp-bio/darts_bht)

Version: "v0.1.0"

Author: "Zijun Zhang"

Date: "2.24.2019"


### Table of Contents
1. [Installation](#installation)
2. [Testing](#testing)
3. [Using Darts BHT](#using-darts-bht)


### Installation

#### Install via Anaconda
The recommended way to install `Darts_BHT` is through [Anaconda](https://anaconda.org/darts-comp-bio).
You can also create a new environment for Darts, because currently DARTS works in Python 2.7.

```bash
conda create -n darts python=2.7  # optional
source activate darts
conda install -c darts-comp-bio darts_bht
```

This will allow conda to do all the heavy-lifting and most often the easiest way to get things spinning.

#### Compile the source Rcpp package
Alternatively, to install `Darts_BHT` R package, you can browse to the BHT folder and
type the following command in terminal:
```
cd Darts_BHT/
R CMD build Darts
R CMD INSTALL Darts_{versionNumber}.tar.gz
```
This will compile a few Rcpp files and prepare for loading. 
If finished successfully, you will see the following message
```
** building package indices
** testing if installed package can be loaded
* DONE (Darts)
```

### Testing

#### Testing the Python wrapper
You can download the [testing_data](https://github.com/zj-zhang/DARTS-BleedingEdge/tree/doc/Darts_BHT/test_data) from the Github repo. If you installed through Anaconda, then type the following command and should
see the corresponding help message as below:

```bash
> Darts_BHT -h
usage: Darts_BHT [-h] [--version] {rmats_count,bayes_infer} ...

Darts_BHT -- DARTS - Deep-learning Augmented RNA-seq analysis of Transcript Splicing

positional arguments:
  {rmats_count,bayes_infer}
    rmats_count         Darts_BHT rmats_count: run rMATS-turbo to count
                        junction reads in BAM files
    bayes_infer         Dart_BHT bayes_infer: perform Bayesian hypothesis
                        testing inference

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

For command line options of each sub-command, type: Darts_BHT COMMAND -h
```

You can test run the installed `Darts_BHT` by:
```bash
Darts_BHT bayes_infer --darts-count test_data/test_norep_data.txt --od test_data/
```

#### Testing the R package
Now let's do a few quick checks to make sure the installed
`Darts_BHT` R package works. There are a few built-in testing 
functions in `Darts` package. Open a new R interactive session, 
and run following code:
```r
library(Darts)
set.seed(101)
t1=test_sim_darts(covg=200)
print(t1)
```
If you are not familiar with the RNA-seq splicing anlaysis, this is also a good time for
you to get to know what's going on. See [Here](#) for a quick tutorial.

Also a quick test on replicate model; we will dive deeper into it in the [Benchmarking](#benchmark) section:
```r
t2=test_sim_rdarts(n=10, outlier=F)
print(t2$eval_df)
```

### Using Darts BHT

Now let's use a more wrapped-up script to call `Darts BHT`. 
In the simplest case, you only need to give `Darts_BHT` the input file `-i` and output folder `-o`. The data files are
in the same format as rMATS, and can be generated by running rMATS w/ or w/o turning on the stat part.

For more concrete examples, please refer to the online doc `Get Started` at:
[here](#)