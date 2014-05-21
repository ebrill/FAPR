#!/bin/sh
#$-N hellolicious_job
#$-S /bin/sh
#$-V ##use all of our environment variables
#$-cwd ## use current working directory
#$-o $HOME/hellolicious_$JOB_ID.out
#$-q normal.q  ## options fast.q normal.q gpu.q all.q (normal isn't really slow, it's
#just slower than fast)


# Write your actual task code here
pip install luigi
python basicpipeline.py --local-scheduler StepTwo
