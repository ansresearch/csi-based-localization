# CSI-based Location Fingerprinting

CSI-based localization applications exploit the Channel State Information (CSI) embedded in Wi-Fi frames to link some states of the wireless channel to specific positions of a human target in a room.
These applications, enabling device-free tracking of any person, are generally evaluated 

This code has been used to determine the accuracy of a generic CSI-based device-free localization system and to evaluate the performance of several obfuscation schemes.

More information about CSI obfuscation and CSI-based localization in general can be found in our paper [*AntiSense: Standard-Compliant CSI Obfuscation against unauthorized Wi-Fi sensing*](https://www.sciencedirect.com/science/article/abs/pii/S0140366421004916).

# Instructions

*The following instructions have been tested with **pip 21.3.1 (Python 3.8.10)***.

To install the required packages, run:
```
pip install -r requirements.txt
```
*We suggest to install the required packages in a virtual environment.*

Then, edit the configuration variables in the file **evaluate.py** with the path to 1) the CSI dataset, 2) the ground truth dataset and 3) the target receiver.

Finally, run the script **evaluate.py** to train a neural network and test the localization performance:
```
python evaluate.py
```
*This command assumes you already have downloaded the dataset from the next section.*

# Dataset

We have published a sample dataset on Zenodo to reproduce the results obtained in our paper. To go to the dataset page, [click here](https://doi.org/10.5281/zenodo.5885635).

# Related Publications

* M. Cominelli, F. Gringoli, R. Lo Cigno, *AntiSense: Standard-compliant CSI obfuscation against unauthorized Wi-Fi sensing*, 2021, Computer Communications [[ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0140366421004916)]
* M. Cominelli, F. Gringoli, R. Lo Cigno, *Non-Intrusive Wi-Fi CSI Obfuscation Against Active Localization Attacks*, 2021, 16th IEEE/IFIP Wireless On-demand Network systems and Services Conference (WONS) [[IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/9415586)] [[IFIP Open Digital Library](https://dl.ifip.org/db/conf/wons/wons2021/1570696889.pdf)]

# Copyright

The code in this repository is licensed under the MIT License. The license does not apply to the publications linked from this repository, for which their own specific license apply (see publishers' website or contact authors for info).