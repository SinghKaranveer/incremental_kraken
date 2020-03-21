#!/bin/bash
#
### tell SGE to use bash for this script
#$ -S /bin/bash
### execute the job from the current working directory, i.e. the directory in which the qsub command is given
#$ -cwd
### join both stdout and stderr into the same file
#$ -j y
### set email address for sending job status
#$ -M ks3379@drexel.edu
### project - basically, your research group name with "Grp" replaced by "Prj"
#$ -P rosenclassPrj
### select parallel environment, and number of job slots
#$ -pe openmpi_ib 1
### request 15 min of wall clock time "h_rt" = "hard real time" (format is HH:MM:SS, or integer seconds)
#$ -l h_rt=04:00:00
### a hard limit 8 GB of memory per slot - if the job grows beyond this, the job is killed
#$ -l h_vmem=32G
### want nodes with at least 6 GB of free memory per slot
#$ -l m_mem_free=32G
### want nodes with Intel CPUs
#$ -l vendor=intel
### select the queue all.q
#$ -q all.q

. /etc/profile.d/modules.sh

### These four modules must ALWAYS be loaded
module load shared
module load proteus
module load sge/univa
module load gcc

### Whatever modules you used, in addition to the 4 above,
### when compiling your code (e.g. proteus-openmpi/gcc)
### must be loaded to run your code.
### Add them below this line.
# module load FIXME
/home/ks3379/incremental_kraken/add_files_scripts/add_files.py /lustre/scratch/djd378/kraken_db_fold2/2015/ 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015
/home/ks3379/incremental_kraken/add_files_scripts/add_files.py /lustre/scratch/djd378/kraken_db_fold2/2016/ 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016
/home/ks3379/incremental_kraken/add_files_scripts/add_files.py /lustre/scratch/djd378/kraken_db_fold2/2017/ 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017
/home/ks3379/incremental_kraken/add_files_scripts/add_files.py /lustre/scratch/djd378/kraken_db_fold2/2018/ 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018
/home/ks3379/incremental_kraken/add_files_scripts/add_files.py /lustre/scratch/djd378/kraken_db_fold2/2019/ 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 
