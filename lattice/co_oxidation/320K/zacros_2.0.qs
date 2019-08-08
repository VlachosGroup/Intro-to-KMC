#!/bin/bash
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe mpich 1
#


# The  executable:
export KMC_EXE="/home/vlachos/wangyf/programs/zacros_2.0/build_parallel/zacros.x"

# Simple summary:
echo ""
echo "Running on ${HOSTNAME} with job id ${JOB_ID}"
echo ""

${KMC_EXE}
