#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Luis Quintero | luis-eduard@dsv.su.se
# Created Date: 2021/06/14
# =============================================================================
"""
Configuration file for experiment
"""
# =============================================================================
# Imports
# =============================================================================

import sys,os,argparse
from enum import Enum, IntEnum, unique

from kinemats.ts_classification import EnumDistMetrics


# =============================================================================
# Enums with variables for each step of the analysis
# =============================================================================

@unique
class Datasets(Enum): # Folder name where all the analysis of the dataset will store temp files
    IMT = "IMT" 
    Tsinghua = "Tsinghua"

    def __str__(self):
        return self.value

@unique
class DataRepresentation(Enum):
    Quaternion      = 'quaternion'  # 4D
    Euler           = 'euler'       # 3D
    Spherical       = 'spherical'   # 2D
    Yaw             = 'yaw'         # 1D
    All             = 'all'
    def __str__(self):
        return self.value

@unique
class Classifiers(IntEnum):
    HIVE_COTEv1 = -1
    STSF = -2
    ROCKET = -3
    MiniRocket = -4
    MrSEQL = -5
    TDE = -6

    KNN = 0     # Used in general, not tied to num of neighbors
    KNN_1 = 1
    KNN_7 = 7   # IMT has 5 classes
    KNN_9 = 9   # UCR UWaveGesture has 8 classes
    KNN_11 = 11 # Tsinghua has 9 classes
    DT = 20   # Decision Tree
    RF = 21   # Random Forest
    GBM = 22  # Gradient Boosting Machine
    
    # Add more classifiers here

# =============================================================================
# GENERAL SETUP
# =============================================================================

# MAIN FOLDERS FOR OUTPUT FILES
ROOT = "./"                 # Root folder for all files respect to the notebook: Use "../" to run IPython, or "./" to run from VSCode

SHOW_PLOTS = True           # Flag to avoid time-consuming plots that are already generated
EXPORT_PLOTS = True         # Flag to generate files of the plots. Requires SHOW_PLOTS=True

DATASET_FOLDER = ROOT + "dataset/"  # Main directory for datasets

PLOT_FOLDER = ROOT+"plots/" # Main folder for plots
IMG_FORMAT = ".png"         # Format to export the plots

TEMP_FOLDER = ROOT+"temp/"  # Main folder for temp files with intermediate calculations
TEMP_FORMAT = ".npy"     # Extension for temp files created with pickle

RESULTS_FOLDER = ROOT+"results/"

# CSV files for cross-similarity matrices for each possible pair {Data Rep, Distance Measure}
PREFIX_DATASET = "dataset_"
PREFIX_CDIST_MATRIX = "cdistmat_"

# CSV file with classification result
RESULTS_FILENAME = "classif_results"
# Columns of the DataFrame with the results of the classification
COLUMNS_LABELS = ['dataset', 'classifier','fold']

# WORKFLOW MANAGEMENT REGARDING ITERATIONS TO LOAD OR GENERATE FILES
RELOAD_TRIES = 2            # Each step tries to create and load input_files maximum RELOAD_TRIES number of times
DISPLAY_ITER_STEP = 1     # When generating results, how often to display message or progress (This range is usually in terms of thousands)

# Monte-Carlo iterations
MC_ITERATIONS = 10          # External loop that defines Monte-Carlo iterations
MC_RANDOM_SEED = 1234      # Seed to be applied before starting Monte-Carlo randomization
N_JOBS_PARALLEL = -1        # n_jobs passed to sklearn function

# Cross-validation
CV_NUM_FOLDS = 20

# PLOTTING AXES
HEADERS_DATASETS = ['Quaternion', 'Euler', 'Yaw', 'Quat+Euler']

##########################
### DATASETS
##########################

# Input for the notebook
DATASETS_LIST = [Datasets.IMT, Datasets.Tsinghua]
DATASET_MAIN =  DATASETS_LIST[0] #Datasets.IMT #Datasets.Tsinghua #Datasets.IMT # !!!!! All the temp files will have this suffix, in case we use a different dataset

# Classes: Which column from the demographics.csv is used as target class label
CLASS_COLUMN_NAME = "videoId" #"user"  # "videoId": Tries to classify the videos. "user" tries to classify the people.

# Original datasets
DATASET_IMT_TAR = DATASET_FOLDER+"IMT/dataset.tar.gz"
DATASET_TSINGHUA_ZIP = DATASET_FOLDER+"Tsinghua/vr-dataset.zip"

# Preprocessed dataset

DATASET_DEMOGRAPHICS  = DATASET_FOLDER+str(DATASET_MAIN)+"/demographics.csv" # Demographics
DATASET_TIMESTAMPS  = DATASET_FOLDER+str(DATASET_MAIN)+"/timestamps.csv" # Timestamps
DATASET_SUMMARY     = DATASET_FOLDER+str(DATASET_MAIN)+"/summary_timeseries.csv" # CSV file with summary of each time series.
DATASET_LABELS      = DATASET_FOLDER+str(DATASET_MAIN)+"/labels.csv" # Cluster index TRUE_LABEL
DATASET_DATA        = DATASET_FOLDER+str(DATASET_MAIN)+"/dataset.npy" # Resampled data stats


##########################
### CLASSIFIERS
##########################

#### FEATURE-BASED CLASSIFIERS CLASSIFIERS SETUP

# KNN
KNN_N_NEIGH = Classifiers.KNN_11
# DT
DT_MAX_DEPTH = 100
# RF
RF_N_ESTIMATORS = 100
RF_MAX_DEPTH = 10
# GBM
GBM_N_ESTIMATORS = 50
GBM_MAX_DEPTH = 5


#### STATE-OF-THE-ART CLASSIFIERS SETUP

# KNN-TS
KNN_TS_N_NEIGH = Classifiers.KNN_1
KNN_TS_DTW_WARPING_WINDOW = 0.05

# Mr-SEQL (Multivariate)
# No params required

# STSF (Univariate)
STSF_N_ESTIMATORS = 200

# TDE (Multivariate)
TDE_MAX_TIME = 5
TDE_MAX_ENSEMBLE_SIZE = 50
TDE_MAX_SELECTED_PARAMS = 50

# ROCKET (Multivariate)
ROCKET_N_KERNELS = 10000

# MiniRocket (Multivariate)
MINIROCKET_N_KERNELS = 10000
MINIROCKET_MAX_DILATIONS = 32


############################
#### ENTRY POINT
############################

def help():
    m = f"""
        Experiment execution with dataset '{DATASET_MAIN}'
        Parameters:
            
        """
    # print(m)
    return m

def main(argv):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--dataset", type=int, help=f"Index of the dataset> {len(DATASETS_LIST)}")

    args = parser.parse_args()

    main(sys.argv[1:])

    try:
        pass
    except Exception as e:
        help()
        FileNotFoundError(e)
        
