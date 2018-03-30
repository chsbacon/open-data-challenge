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
| package name | version | url |
| ------------ | ------- | --- |
| keras        |         |     |
| pandas       |         |     |
| jupyter      |         |     |

## Contributors
* James Nachbar
* Stephen Newman
* Jonah Weissman
