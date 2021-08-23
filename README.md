# Summary

**Title:** *Effects of data representations of 3D rotation for time-series classification of 360 videos with virtual reality headsets*

This project includes the algorithms to conduct time-series analysis of head movements based on publicly-available repositories.

The analysis comprises:
- Converting Quaternion(4D) representations into Euler(3D), Spherical(2D) and Yaw(1D)
- Apply KNN classifiers with multiple distance metrics: Euclidean, Specific Euclidean, Dynamic Time Warping (DTW)
- Apply state-of-the-art time-series classifiers: STSF and ROCKET.

## Datasets

This project uses publicly available datasets with head rotations, each  details about datasets can be found in [dataset/README.md](/dataset/README.md).

1. IMT: Refers to *The 360-Degree Videos Head Movements Dataset* available [here](https://dl.acm.org/doi/10.1145/3083187.3083215).
2. Tsinghua: Refers to *A Dataset for Exploring User Behaviors in VR Spherical Video Streaming* available [here](https://dl.acm.org/do/10.1145/3192423/abs/)

---

# Setup

```console
>> git clone https://github.com/luiseduve/user_identif_hmd_rotation.git

Create and activate python venv
>> python -m venv env
    >> [Win] ./env/Scripts/activate.bat
    $$ [Linux/MacOS] source env/bin/activate

Install required libraries
>> pip install -r ./requirements.txt

Initialize git submodules
>> git submodule update --init

If the previous does not pull the repository:
>> git submodule add https://github.com/luiseduve/kinemats.git]
```

## Compatibility

- TSC like MrSEQL and TDE are implemented with `sktime==0.6.1`, which uses `pandas==1.2.4` and in turn requires `Python>=3.7.1`.
- 


# Replicate results

1. Change the variable `experiment_config.DATASET_MAIN` to one of these options depending on the dataset to process:
    - `Datasets.IMT`
    - `Datasets.Tsinghua`
2. Execute the jupyter notebooks in order.
    - `01_....ipynb`: Preprocess the datasets
    - `02_....ipynb`: Executes feature-based classifiers
    - `03_....ipynb`: Runs state-of-the-art time-series classifiers
    - `99_results_compilation.ipynb`: Compiles all previous results in a single table and generates plots