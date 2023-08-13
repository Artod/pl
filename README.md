# Monte Carlo π Estimation CI/CD with MLOps flavour

This repository demonstrates the use of Monte Carlo simulations to estimate the value of π and integrates CI (Continuous Integration) practices using GitHub Actions for automated testing. Beyond the core simulation, the project incorporates principles of MLOps, using DVC for data and model versioning.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [MLOps Integration with DVC](#mlops-integration-with-dvc)
- [Running the Tests](#running-the-tests)
- [Continuous Integration](#continuous-integration)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a simple Monte Carlo simulation to estimate the value of π. Beyond the core simulation, the project incorporates principles of MLOps, using DVC for data and model versioning.

## Getting Started

### Prerequisites

- Python (>=3.6)
- dvc (>=2.5.4)

### Installation

1. Clone this repository:
```git clone https://github.com/Artod/pl.git```

2. Navigate to the directory:
```cd [Your Repository Directory]```

3. Install the required packages:
```pip install -r requirements.txt```

## MLOps Integration with DVC:

**DVC (Data Version Control)** offers a bridge between traditional software development and data science by providing a means to version large datasets and ML models, akin to how Git versions code. DVC's principles are rooted in MLOps, aiming to make ML projects more reproducible, collaborative, and continuous.

For this demonstration using the Monte Carlo simulation:

**Validation**: The CI pipeline ensures that the simulation runs correctly and produces an output.

**Reproducibility**: Given the inherent randomness of Monte Carlo simulations, results will vary slightly with each run. However, with DVC, we ensure that every result, every change in the code or data can be tracked, and previous states of the project can be restored.

### Steps:

**Set up DVC**: Initialize DVC in your local environment using dvc init.

**Versioning Data & Model Outputs**: After running the simulation, the estimated value can be versioned using:

```dvc add pi_estimate.txt```

Subsequent runs and changes can be reproduced using `dvc repro``, which re-executes the pipeline stages, ensuring consistency and reproducibility.

In broader applications, DVC's integration with remote storage would allow data scientists to share datasets, intermediate data, and models, facilitating collaboration and ensuring that everyone is working from a consistent base.

For this demo, we keep everything local, but in a more extensive project setup, one would use dvc push to store datasets and models in remote storage, such as Amazon S3 or Google Drive, ensuring that large datasets and models are decoupled from code but remain versioned and accessible.

## Running the Tests

From the root directory, run:
```python -m unittest test_monte_carlo_simulation.py```

## Continuous Integration

This repository uses GitHub Actions for Continuous Integration, automatically running tests on every push and pull request. Check the `.github/workflows/ci.yml` file for workflow details.

## Future Enhancements

Discuss potential improvements or extensions, such as:

- Enhanced π estimation methods.
- Integration with other CI/CD tools.
- Real-world applications using this simulation.

## Contributing

While this is primarily an educational project, contributions are welcome! Please open an issue to discuss changes or propose a Pull Request.

## License

This project is open source, under the [MIT License](LICENSE).

---

Made with ❤️ by Artod
