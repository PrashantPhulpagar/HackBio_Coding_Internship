# HackBio Biocoding Internship - Python Data Analysis & Visualization (Stage - 2)

This repository contains my solutions to various bioinformatics and data science tasks as part of the HackBio Biocoding Internship. These tasks involve analyzing and visualizing datasets from different biological and healthcare domains using Python.

## Table of Contents

* Task Code 2.1: Botany and Plant Science

* Task Code 2.2: Biochemistry & Oncology

* Task Code 2.3: Transcriptomics

* Task Code 2.4: Public Health


## Task Code 2.1: Botany and Plant Science

### Objective:

Analyze the metabolic response of engineered mutant crops and wild-type plants under different treatments to assess pesticide resistance.

### Steps:

- Calculate the difference in metabolic response (ΔM) between the DMSO treatment and the 24-hour treatment.

- Generate a scatter plot showing ΔM for wild-type (WT) and mutant plants.

- Fit a line with y-intercept = 0 and slope = 1.

- Calculate residuals and apply a threshold to color points based on deviation from the fitted line.

- Identify outlier metabolites and generate line plots for selected metabolites across 0h, 8h, and 24h.

## Task Code 2.2: Biochemistry & Oncology

### Objective:

Analyze the impact of non-synonymous nonsense mutations on protein structure and function using SIFT and FoldX datasets.

### Steps:

- Merge SIFT and FoldX datasets based on concatenated Protein and Amino Acid information.

- Identify mutations with a SIFT score < 0.05 and FoldX score > 2.

- Analyze amino acid substitutions and generate frequency tables.

- Visualize amino acid frequencies using bar plots and pie charts.

- Identify and describe the amino acid with the highest structural and functional impact.

## Task Code 2.3: Transcriptomics

### Objective:

Analyze RNA-seq data to study differential gene expression between a diseased cell line and a compound-treated diseased cell line.

### Steps:

- Generate a volcano plot for differential gene expression.

- Identify upregulated genes (Log2FC > 1, p-value < 0.01).

- Identify downregulated genes (Log2FC < -1, p-value < 0.01).

- Retrieve functional information for the top 5 upregulated and top 5 downregulated genes using GeneCards.

## Task Code 2.4: Public Health

### Objective:

Analyze NHANES data to assess the health and nutritional status of participants.

### Steps:

- Process missing values.

- Visualize BMI, weight, weight in pounds, and age distributions using histograms.

- Compute the mean 60-second pulse rate, diastolic blood pressure range, income variance, and standard deviation.

- Visualize weight-height relationships, coloring points by gender, diabetes status, and smoking status.

- Perform t-tests between age & gender, BMI & diabetes, alcohol consumption & relationship status.
