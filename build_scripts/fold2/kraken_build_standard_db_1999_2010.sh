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
 
echo "1999"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/1999

echo "2000"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2000

echo "2001"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2001

echo "2002"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2002

echo "2003"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2003

echo "2004"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2004

echo "2005"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2005

echo "2006"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2006

echo "2007"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2007

echo "2008"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2008

echo "2009"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2009

echo "2010"
/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build --build --db /scratch/djd378/kraken_db_fold2/2010
