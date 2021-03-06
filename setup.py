#!/usr/bin/env python

from setuptools import setup
import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'

def main():
	install_requires = ['m2r'] if on_rtd else []
	setup(
		name='Darts_BHT',
		  
		version='0.1.0',
		  
		description='Deep-learning Augmented RNA-seq analysis of Transcript Splicing',

		author='Zijun Zhang',

		author_email='zj.z@ucla.edu',

		url='https://github.com/Xinglab/DARTS',

		packages=['Darts_BHT'],

		scripts=[],

		install_requires=install_requires
		#[
		#	#'rpy2',
		#	#'cython==0.27.0', # for compiling rmats-turbo
		#	'm2r',   # for doc build
		#	]
		 )
	if not on_rtd:
		from rpy2.robjects.packages import importr
		utils = importr('utils')
		utils.chooseCRANmirror(ind=1) 
		R_dependency_list = ['Rcpp', 'doSNOW', 'getopt', 'mixtools', 'ggplot2']
		from rpy2.robjects.vectors import StrVector
		import rpy2.robjects.packages as rpackages
		utils.chooseCRANmirror(ind=1) # select the first mirror in the list

		# Selectively install what needs to be install.
		names_to_install = [ x for x in R_dependency_list if not rpackages.isinstalled(x) ]
		if len(names_to_install) > 0:
			utils.install_packages(StrVector(names_to_install))

		utils.install_packages('Darts_BHT/Darts_0.1.0.tar.gz')
	return

if __name__ == '__main__':
	main()
