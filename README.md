# Homodyne Tomography

Given representations of a density operator (matrix) it is possible to reconstruct this density operator without knowing it precisely. This process has previously been carried out using Radon transformations, however, this project examines a new approach; maximum likelyhood (or MaxLik).

The formulae used are all found in the paper 'Iterative maximum-likelyhood reconstruction in quantum homodyne tomography' by A. I. Lvovsky et. al.

## Files

The file relevant for this project is 'prob_theta.ipynb' and contains all the relevant code, including functions (I have not used classes for this project). At the end of the project, by help of Jonas, I changed the iterative calculations from matrix multiplication (using matrices created by nested loops) to using einsum which both sped up the calculations and made it much shorter (simpler).

## prob_theta.ipynb

Note that the file name is bad, but I dare not change it (overlaps in github etc.). I just keep this name

This file contains the code for creating some density operator (matrix, Wigner) and derive representations from different angles. From these representations samples are gathered using rejection sampling.

The purpose is to create pseudo-samples for the Likelyhood-function described in A.I. Lvovsky et. al.

The likelyhood function (eq. 1, Lvovsky), including overlap functions (eq. 8, Lvovsky) is formulated with code. Our pseudo-samples are applied to the function with our density matrix (which we know by fact is correct).

Another file should be created for using the function on different (unknown) density matrices to derive the maximum likelyhood (MaxLik) (once and if I get it to work).

At the end of the file I use an iterative for-loop for the MaxLik-function as this reflects the mathematical formula and is easy to read (for me), but changing this to matrix multiplication will increase the computational speed