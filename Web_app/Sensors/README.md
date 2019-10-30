### From sensors branch
This folder contains all necessary files for retrieving data from connected sensors.
* For DHT11 default pin is 4

The process collecting data from *DHT11* sensor and *BH1750* with defined timeout (sleep time)
which might be changed durigng data collecting.

The output is a .csv file with 
* Temperature
* Light
* Humidity

Process writing to a file an average from 2 last measurements.

### sensors_data.py is an entry point

## Plotting data
Small script that using padas, matplotlib modules
to draw .jpeg pictures

Before drawing, please pass to a scipt valid name (name from csv columns)
Script using tails (the oldest ones) values. It's possible to specify an amount
of last values:
`create_plot(column_name, tail_size=10)`
