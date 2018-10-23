# PM Forcasting using LSTM

This Project uses LSTM Recurrent Neural Network as a framework for forecasting the future, based on the time series PM2.5 data and meteorological information in Beijing.

The dataset was collected form UCI Machine Learning Repository. The dataset contains data from 2010-2014.
### Dataset Demo  
<pre>
| Date                   | PM     | dew | temp |  press  | wnd_dir | wnd_spd | snow  | rain |<br/>
| 2010-01-02 00:00:00    |  129.0 | -16 | -4.0 | |1020.0 |  SE     |  1.79   |   0   |  0  |
| 2010-01-02 01:00:00    |  148.0 | -15 | -4.0 | 1020.0  |  SE     |  2.68   |   0   |  0  |
| 2010-01-02 02:00:00    |  159.0 | -11 | -5.0 | 1021.0  |  SE     |  3.57   |   0   |  0  | 
| 2010-01-02 03:00:00    |  181.0 |  -7 | -5.0 | 1022.0  |  SE     |  5.36   |   1   |  0  | 
| 2010-01-02 04:00:00    |  138.0 |  -7 | -5.0 | 1022.0  |  SE     |  6.25   |   2   |  0  | 
</pre>
![DEMO](https://raw.githubusercontent.com/sagunkayastha/PM-Forcasting-using-RNN/master/extra/Figure_1.png)


The codes on the project are based on tutorial: <br>
Multivariate Time Series Forecasting with LSTMs in Keras, by Jason Brownlee <br>
https://machinelearningmastery.com
