#!/bin/bash
#$ -cwd
#$ -j y
#$ -N CO_ox
#$ -S /bin/bash
#$ -pe openmpi-smp 16
#$ -o CO_ox.out

# Get our environment setup:
vpkg_require -q python-ase/3.15.0-python3 openmpi/1.6.3-gcc libxc hdf5/1.8.11-gcc
#vpkg_require "python/2.7.8"
#vpkg_require "openmpi/1.6.3-gcc"
#vpkg_require "python-numpy"
#vpkg_require "matplotlib"
#vpkg_require "python-scipy"
#vpkg_require "python-mpi4py"
#vpkg_rollback all
#vpkg_require python-networkx

# The  executable:
python3 Single_trajectory.py

# Simple summary:
echo ""
echo "Running on ${HOSTNAME} with job id ${JOB_ID}"
echo ""

time ${PYTHON_EXE}