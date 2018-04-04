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
#### libraries
|     name     | version |    license   |
| ------------ | ------- | ------------ |
| keras        | 2.1.5   |     MIT      |
| pandas       | 0.22.0  | BSD 3-Clause |
| jupyter      | 4.4.0   | BSD 3-Clause |
#### data
| dataset      | source  | license      |
| ------------ | ------- | ------------ |
| weather data |         |              |

## Contributors
* James Nachbar
* Stephen Newman
* Jonah Weissman
