# Summary

> **Paper:** *Effective Classification of Head Motion Trajectories in Virtual Reality using Time-Series Methods*
> 
> **Venue:** *The 4th IEEE International Conference on Artificial Intelligence and Virtual Reality (IEEE AIVR 2021)*

In this paper, we present a method to classify head motion trajectories using recent time-series methods. The analysis of motion data with machine learning is a common technique to solve problems in Virtual Reality (VR), such as adaptive rendering or user behavioral modeling. Motion data are initially collected as time series, but they are usually transformed into tabular features compatible with traditional feature-based classifiers. Data mining research has proposed several time-series classifiers that can directly exploit the temporal relationship of the data without requiring manual feature extraction. Nevertheless, the effectiveness of these time-series methods still requires validation on real-life problem domains. Therefore, this paper demonstrates how a pipeline that combines a recent time-series classifier with two rotation space representations (quaternion and Euler) can successfully analyze head motion in VR applications. We test the proposed method on two public datasets containing head rotations, resulting in higher prediction accuracy than other feature-based and time-series classifiers. We also discuss some limitations, guidelines for future work, and concluding remarks.

## Datasets

This project uses publicly available datasets with head rotations, each  details about datasets can be found in [dataset/README.md](/dataset/README.md).

1. IMT: Refers to *The 360-Degree Videos Head Movements Dataset* available [here](https://dl.acm.org/doi/10.1145/3083187.3083215).
2. Tsinghua: Refers to *A Dataset for Exploring User Behaviors in VR Spherical Video Streaming* available [here](https://dl.acm.org/do/10.1145/3192423/abs/)

---

# Setup

```console
>> git clone https://github.com/luiseduve/head-motion-classification-AIVR21.git

Create and activate python venv
>> python -m venv env
    >> [Win] ./env/Scripts/activate.bat
    $$ [Linux/MacOS] source env/bin/activate

Install required libraries
>> pip install -r ./requirements.txt

Initialize git submodules
>> git submodule update --init

Note: If the previous command does not pull the repository:
>> git submodule add https://github.com/luiseduve/kinemats.git
```

# Replicate results

1. Change the variable `experiment_config.DATASET_MAIN` to the value `DATASETS_LIST[0]` to process `Datasets.IMT`.
2. Execute the jupyter notebooks in order.
    - `01_....ipynb`: Preprocess the datasets
    - `02_....ipynb`: Executes feature-based classifiers
    - `03_....ipynb`: Runs state-of-the-art time-series classifiers
3. Change the variable `experiment_config.DATASET_MAIN` to the value `DATASETS_LIST[1]` to process `Datasets.Tsinghua`.
4. Run again all jupyter notebooks from **step 2**.
5. Execute `99_results_compilation.ipynb`to generate a single table and corresponding plots.