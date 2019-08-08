#!/bin/bash
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe mpich 1
#


# The  executable:
export KMC_EXE='/home/vlachos/wangyf/programs/Zacros_Wrapper/Zacros-Wrapper/zacros_ZW.x'

# Simple summary:
echo ""
echo "Running on ${HOSTNAME} with job id ${JOB_ID}"
echo ""

${KMC_EXE}
