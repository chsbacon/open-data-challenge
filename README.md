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
│   ├── prediction_generator.ipynb
# BEGIN PREDICTIVE MODEL SUBMISSION
│   ├── Number of sessions over time.csv
│   ├── Clients per day.csv
│   └── Usage over time.csv
# END PREDICTIVE MODEL SUBMISSION
├── README.md
└── src
    └── model_trainer.ipynb
```
## Usage
1. Run `jupyter notebook`
2. Navigate to `src/model_runner.ipynb`
3. Edit the date in the fourth cell
4. Run the whole notebook by clicking `Kernel > Restart & Run all`

## Dependencies
#### libraries
|     name     | version |    license   |
| ------------ | ------- | ------------ |
| keras        | 2.1.5   |     MIT      |
| pandas       | 0.22.0  | BSD 3-Clause |
| jupyter      | 4.4.0   | BSD 3-Clause |
| numpy        | 1.14.2  | BSD 3-Clause |
| scipy        | 1.0.0   | BSD 3-Clause |
| livelossplot | https://github.com/stared/livelossplot.git@fd72c53bd82d0c0052478c735edd356892f6f7f6 | MIT |
#### data
| dataset      |          source           | license       |
| ------------ | ------------------------- | ------------- |
| weather data | https://www.ncdc.noaa.gov | Public Domain |

## Contributors
* James Nachbar
* Stephen Newman
* Jonah Weissman
