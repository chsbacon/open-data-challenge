# Charlottesville Open Data Challenge

## Catalog
```
.
├── data
│   ├── bus_transit
│   │   └── bus_transit.csv
│   ├── parking_tickets
│   │   └── Parking_Tickets.csv
│   ├── uva_attendance
│   │   └── uva_attendance
│   ├── weather
│   │   └── precip_temp.csv
│   └── wifi
│       ├── 01-01
│       │   ├── Clients per day.csv
│       │   ├── Number of sessions over time.csv
│       │   ├── Top application categories.csv
│       │   ├── Top applications by usage.csv
│       │   ├── Top device models by usage.csv
│       │   ├── Top devices.csv
│       │   ├── Top manufacturers by usage.csv
│       │   ├── Top operating systems by usage.csv
│       │   └── Usage over time.csv
│       ├── 07-01
│       │   ├── Clients per day.csv
│       │   ├── Number of sessions over time.csv
│       │   ├── Top application categories.csv
│       │   ├── Top applications by usage.csv
│       │   ├── Top device models by usage.csv
│       │   ├── Top devices.csv
│       │   ├── Top manufacturers by usage.csv
│       │   ├── Top operating systems by usage.csv
|       └── └── Usage over time.csv
├── LICENSE
├── README.md
└── src
    ├── bus_processing.ipynb
    ├── model.ipynb
    └── ticket_processing.ipynb
```
predictive model
## Usage
```bash
jupyter nbconvert --stdout src/model.ipynb | python3
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
