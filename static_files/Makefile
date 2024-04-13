# Define the C++ compiler
CXX = g++

# Define the CUDA compiler
NVCC = nvcc

# Define any compile-time flags for C++
CXXFLAGS = -Wall -Wextra -std=c++17 -O2

# Define any compile-time flags for CUDA
NVCCFLAGS = -O2

# Define any directories containing header files
INCLUDES = -I.

# Output directory
OUTDIR = output

# Subtask 1 files and executable
CUDA_SRCS1 = src/assignment2_subtask1.cu
MAIN1 = subtask1

# Subtask 1 files and executable
CPP_SRCS1a = src/assignment2_subtask1.cpp
MAIN1a = subtask1a


# Subtask 2 files and executable
CUDA_SRCS2 = src/assignment2_subtask2.cu 
MAIN2 = subtask2

# Subtask 3 files and executable
CUDA_SRCS3 = src/assignment2_subtask3.cu 
MAIN3 = subtask3

# Subtask 4 files and executable
CUDA_SRCS4 = src/assignment2_subtask4.cu 
MAIN4 = subtask4

FILES = $(python3 preprocessing.py)

.PHONY: clean all subtask1 subtask2 subtask3 subtask4 subtask1a

all: subtask1a subtask1 subtask2 subtask3 subtask4 

subtask1a: $(MAIN1a)
$(MAIN1a): $(OBJS1)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $(MAIN1a) $(CPP_SRCS1a)

subtask1: $(MAIN1)
$(MAIN1): $(OBJS1)
	$(NVCC) $(NVCCFLAGS) $(INCLUDES) -o $(MAIN1) $(CUDA_SRCS1)


subtask2: $(MAIN2)
$(MAIN2): $(OBJS2)
	$(NVCC) $(NVCCFLAGS) $(INCLUDES) -o $(MAIN2) $(CUDA_SRCS2) 

subtask3: $(MAIN3) run_python_script
$(MAIN3): $(OBJS3)
	$(NVCC) $(NVCCFLAGS) $(INCLUDES) -o $(MAIN3) $(CUDA_SRCS3) 

run_python_script:
	python3 preprocess.py

subtask4: $(MAIN4)
$(MAIN4): $(OBJS4)
	$(NVCC) $(NVCCFLAGS) $(INCLUDES) -o $(MAIN4) $(CUDA_SRCS4) 

clean:
	$(RM) *.o *~ $(MAIN1) $(MAIN2) $(MAIN3) $(MAIN4) $(MAIN1a)