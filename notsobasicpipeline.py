#!/usr/bin/env python

import luigi
import os
from subprocess import call 

class FastQcGo(luigi.Task): 
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
