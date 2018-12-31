# Occupancy Detection

**Downloaded from the UCI Machine Learning Repository on October 13, 2016.**

- Multivariate, Time-Series Data Set
- Real Attributes
- 20,560 Instances
- 7 attributes
- Well suited for _classification_ tasks
- [https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+](https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+)

## Abstract

Experimental data used for binary classification (room occupancy) from Temperature, Humidity, Light and CO2. Ground-truth occupancy was obtained from time stamped pictures that were taken every minute.

## Description

Three data sets are submitted, for training and testing. Ground-truth occupancy was obtained from time stamped pictures that were taken every minute. For the journal publication, the processing R scripts can be found on GitHub: [https://github.com/LuisM78/Occupancy-detection-data](https://github.com/LuisM78/Occupancy-detection-data)

## Attributes

- datetime `year-month-day hour:minute:second`
- temperature (celsius)
- relative humidity (%)
- light (lux)
- carbon dioxide (ppm)
- humidity ratio (kgwater-vapor/kg-air)
- occupancy (1 for occupied, 0 for not occupied)

## Citation

Candanedo, Luis M., and Véronique Feldheim. "Accurate occupancy detection of an office room from light, temperature, humidity and CO 2 measurements using statistical learning models." Energy and Buildings 112 (2016): 28-39.