FAPR
========

Full Assembly Pipeline for RNA 

to run type python notsobasicpipeline.py --local-scheduler 


Still a work in progress, but the finished pipeline will:

* Do summary analysis of Raw Data
* Perform ALLPATHS-LG assembly
* Fill gaps with ATLAS GAP-FILL
* Build Training sets for functional annotation
* Generate species specific repeat database with RepeatModeler
* Perform Maker Annotation (or wait while it's run on a beefy cluster)
* Filter Maker annotation, functional annotations, etc.
* Generate a .tbl file for NCBI submission, prepare submissions for SRA and WGS.

Stay tuned.
