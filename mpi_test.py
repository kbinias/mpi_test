#!/usr/bin/env python

from mpi4py import MPI
import sys

rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
name = MPI.Get_processor_name()

sys.stdout.write(
    "MPI: Test from %s, rank %d out of %d\n" % (name, rank, size))
