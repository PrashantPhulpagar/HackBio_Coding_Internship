This folder contains four Python functions performing various biological and computational tasks:

**1. DNA to Protein Translation**

**2. Logistic Population Growth Curve Simulation**

**3. Time to Reach 80% of Maximum Growth Rate**

**4. Hamming Distance Calculation**

Each function is explained below in detail.

**1. DNA to Protein Translation**

This function translates a given DNA sequence into a protein sequence based on the standard genetic codon table.

The function dna_to_protein(dna) takes a DNA string as input.

A dictionary (codon_table) maps each three-letter DNA codon to its corresponding amino acid.

The function iterates over the DNA sequence in steps of three (codons).

Each codon is translated into an amino acid and appended to the protein string.

If an unknown codon appears, it is replaced with ?.

**2. Logistic Population Growth Curve Simulation**

This function simulates population growth using the logistic growth model.

The function simulate_logistic_growth(P0, r, K, time_steps) models a population's growth.

P0 = Initial population.

r = Growth rate.

K = Carrying capacity (maximum sustainable population).

The function iterates through the specified number of time_steps.

The function returns a list of population values over time.

**3. Time to Reach 80% of Maximum Growth Rate**

This function determines the time when a growing population reaches 80% of its peak growth rate.

The function time_to_80_percent_max_growth(P0, r, K, time) models logistic growth.

The maximum growth rate occurs at K/2 (half the carrying capacity).

It finds the first time point where the growth rate reaches 80% of the maximum.

**4. Hamming Distance Calculation**

This function calculates the Hamming distance between two strings, which is the number of positions where they differ.

The function hamming_distance(str1, str2) takes two strings as input.

If they are of different lengths, the shorter one is padded with underscores (_).

The function iterates through the characters of both strings and counts mismatches.
