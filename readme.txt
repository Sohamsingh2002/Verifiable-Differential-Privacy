# Verifiable Differential Privacy (VerDP) Verifier

This module contains an implementation of a Verifiable Differential Privacy (VerDP) verifier using the Pinocchio Proof Protocol, VFuzz Compiler, and ZKProof. It verifies the correctness and privacy of computations performed on databases while maintaining differential privacy.

The complete code is available in a single Jupyter Notebook named **Verification.ipynb**. To get started, simply execute that notebook.

## Requirements

- Python 3.7 or higher

## Libraries

The following libraries are required:

- `numpy==1.20.3`
- `sqlparse==0.4.2`
- `matplotlib==3.4.2`
- `pandas==1.2.4`
- `scipy==1.6.3`
- `hashlib`
- `libiop` (will be downloaded and built from source, no need for manual installation)
- `os`
- `re`

### Installation

To install the required libraries, use the following command:

```bash
pip install numpy sqlparse matplotlib pandas scipy


##Tech Stack:
Python
Cryptography
Differential Privacy
Zero-Knowledge Proofs
Pinocchio Proof Protocol
VFuzz Compiler


### The project is divided into five main parts:
Data Processing and Sql query Generation
Sql to VFuzz query translation and checking queries as differentially private
VFuzz Query Execution and Proof generation
Proof Verification
Visualization of results(Execution and verification time)

Commands for Running code:
Simply execute Verification.ipynb file.


Usage
Clone the directory to your local machine.
Ensure that you have all the required libraries installed.
Open the Jupyter Notebook (Verification.ipynb) file containing the implementation.
Execute the code cells to perform verification of the computations on databases.
Follow the instructions provided in the notebook to understand the process and results.
In short, simply unzip folder and run  "Verification.ipynb" file. 

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Soham Singh,CSE,IIT Roorkee. ERoll: 21114099

