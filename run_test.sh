export MPI_NUM_PROCS=4

mpirun -np $MPI_NUM_PROCS -H localhost,localhost,localhost,localhost ./build/mpi_test 2>&1 | tee build/output.txt
#mpirun -np $MPI_NUM_PROCS ./build/mpi_test 2>&1 | tee build/output.txt
