# Homodyne Tomography

Given representations of a density operator (matrix) it is possible to reconstruct this density operator without knowing it precisely. This process has previously been carried out using Radon transformations, however, this project examines a new approach; maximum likelyhood (or MaxLik).

The formulae used are all found in the paper 'Iterative maximum-likelyhood reconstruction in quantum homodyne tomography' by A. I. Lvovsky et. al.

## Libraries needed

numpy
scipy
qutip
cmath
math
matplotlib.pyplot
funcs.py (my own file)

## Files

'prob_theta.ipynb' : This is the file relevant for this project is and contains all the relevant code. At the end of the project, by help of Jonas, I changed the iterative calculations from matrix multiplication (using matrices created by nested loops) to using einsum which both sped up the calculations and made it much shorter (simpler).

'funcs.py' : This file contains all the functions necessary to run main file 'prob_theta.ipynb'

The remaining files are used by myself to test out different lines of codes (either my own or others' code)

## prob_theta.ipynb

Note that the file name is bad, but I dare not change it (overlaps in github etc.). I just keep this name

This file contains the code for creating some density operator (matrix, Wigner) and derive representations from different angles. From these representations samples are gathered using rejection sampling.

The purpose is to create pseudo-samples for the Likelyhood-function described in A.I. Lvovsky et. al.

The likelyhood function (eq. 1, Lvovsky), including overlap functions (eq. 8, Lvovsky) is formulated with code. Our pseudo-samples are applied to the function with our density matrix (which we know by fact is correct).

At the end of the file I use an iterative for-loop for the MaxLik-function as this reflects the mathematical formula and is easy to read (for me), but changing this to matrix multiplication will increase the computational speed

## How to use

The first part of the program shows the different representations of the coherent state.

In the next part of the program the user chooses the index of theta in list [0,30,60,90,120,150] that is to be used to generate random samples for the likelyhood function (by default we use index 0).

As different samples are generated for theta != 0 we see that the likelyhood decreases (less likely) using the unrotated density operator. This indicates that the likelyhood function expresses higher values for better correlated density operator <-> sample pairs