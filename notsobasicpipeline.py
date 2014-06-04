#!/usr/bin/env python

import luigi
import os
from subprocess import call 
from src.dependency_checker import *

class CheckDependencies(luigi.Task):
    def run(self):
        # Check that all programs necessary to the pipeline are installed
        # As an example, check out the function "fastqc_is_installed()" in
        # src/dependency_checker. The following code will terminate the run()
        # method if fastqc_is_installed() returns False.
        # Terminating the run() method means the output() thing doesn't get 
        # created, which means the rest of the pipeline fails. Which is what
        # we want, if fastqc isn't available...
        print "checkdependenciesrunning"
        if not fastqc_is_installed():
            return
        os.system("touch dependencies_checked")   

    def output(self):
        # TODO okay, figure out how to indicate that CheckDependencies.run()
        # completed without any errors (that is, all necessary programs are installed).
        # The hacky way would be to create a file at the end of run(), just an empty
        # file called "all_your_shit_is_installed.txt", then that would be the output.
        # If any dependency wasn't installed, the run() method would exit early and the
        # file wouldn't get created. But that's hacky.
        # So maybe go read Luigi docs to see if there's a non-file-creating way to implement
        # the output() method, some way just to say "hey we're good" like setting a variable
        # to True or something. IDK
        return luigi.LocalTarget("dependencies_checked")


class FastQcGo(luigi.Task): 

    def requires(self):
       return CheckDependencies()

    def run(self): 
        print("hello")
	os.system("mkdir fastqcrap")
	os.system("fastqc -t 20 -o fastqcrap rawreads/*.fastq")

    def output(self):
        return luigi.LocalTarget("fastqcrap")
	#TODO MAKE SURE FASTQC ACTUALLY WROTE FILES 


class FastQcSummary(luigi.Task):

    def run(self):
        print("goodbye")
	os.system("stupidscripts/scrape_fastqc.py fastqcrap fastqcrap/fastqc.summary.txt")

    def requires(self):
        return FastQcGo()

if __name__ == '__main__':
        luigi.run() 
