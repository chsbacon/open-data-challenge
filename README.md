# Charlottesville Open Data Challenge

## Catalog
Entry for Best Predictive Model prize.

```
├── LICENSE
├── models
│   ├── model.h5
│   └── model_runner.ipynb
├── README.md
└── src
    ├── bus_processing.ipynb
    ├── model_trainer.ipynb
    └── ticket_processing.ipynb
```
## Usage
```bash
jupyter nbconvert --execute --to markdown --stdout models/model_runner.ipynb
```

## Dependencies
| package name | version |                                       url                                              |
| ------------ | ------- | -------------------------------------------------------------------------------------- |
| keras        | 2.1.5   | https://repo.continuum.io/pkgs/main/linux-64/keras-2.1.5-py36_0.tar.bz2                |
| pandas       | 0.22.0  | https://repo.continuum.io/pkgs/main/linux-64/pandas-0.22.0-py36hf484d3e_0.tar.bz2      |
| jupyter      | 4.4.0   | https://repo.continuum.io/pkgs/main/linux-64/jupyter_core-4.4.0-py36h7c827e3_0.tar.bz2 |

## Contributors
* James Nachbar
* Stephen Newman
* Jonah Weissman
