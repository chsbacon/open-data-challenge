# Charlottesville Open Data Challenge

## Catalog
Entry for Best Predictive Model prize.

```.
├── data
│   ├── weather
│   │   └── precip_temp.csv
│   └── wifi # given data
├── LICENSE
├── models
│   ├── model.h5
│   └── model_runner.ipynb
├── predictions
│   ├── Clients per day.csv
# BEGIN PREDICTIVE MODEL SUBMISSION
│   ├── Number of sessions over time.csv
│   ├── prediction_generator.ipynb
│   └── Usage over time.csv
# END PREDICTIVE MODEL SUBMISSION
├── README.md
└── src
    └── model_trainer.ipynb
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
| weather data | https://www.ncdc.noaa.gov | Public Domain |

## Contributors
* James Nachbar
* Stephen Newman
* Jonah Weissman
