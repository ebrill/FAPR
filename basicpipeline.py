#!/usr/bin/env python

import luigi
from subprocess import call 

class StepOne(luigi.Task): 
    def run(self): 
        print("hello")
        call(["touch", "junkfile"])

    def output(self):
        return luigi.LocalTarget("junkfile")

class StepTwo(luigi.Task):
    def run(self):
        print("goodbye")

    def requires(self):
        return StepOne()

if __name__ == '__main__':
        luigi.run() 
