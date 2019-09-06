cmake_minimum_required(VERSION 3.1)

project(mpi_test C CXX)

if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "RelWithDebInfo" CACHE STRING
        "Choose the type of build, options are: Debug, Release, RelWithDebInfo and MinSizeRel"
        FORCE)
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g")
else()
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
endif()

set(CMAKE_CXX_STANDARD 11)

find_package(MPI REQUIRED)

add_executable(${CMAKE_PROJECT_NAME} mpi_test.cpp)

target_link_libraries(${CMAKE_PROJECT_NAME} ${MPI_LIBRARIES})
