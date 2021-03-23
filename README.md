# LabPtPTm1

[![CC BY 4.0][cc-by-shield]][cc-by]

LabPtPTm1(Lab dataset series - point to point 815km-SSMF transmission data no. 1)

this dataset is collected in Aug. 2019 which is described and partially used in this [paper](https://www.nature.com/articles/s41467-020-17516-7).


## This is a dataset registry

This repo does not host the data itself, instead, it serves as the [Registry](https://dvc.org/doc/use-cases/data-registries) of this dataset which is stored remotely in [AWS S3](https://aws.amazon.com/s3/) bucket.


DVC registry in this repo is built (`dvc add -R`) to mirror the tracked file structure and replace actual file with its records, namly `.dvc` file. The file/folder namings are self-explained which is previewed as

```
data
├── 815km_SSMF
│   ├── DP16QAM_RRC0.2_28GBd_1ch
│   ├── ├── LP-20_1.h5.dvc
│   ├── ├── ...
│   ├── DP16QAM_RRC0.2_28GBd_1ch_SSNLW
│   ├── DP16QAM_RRC0.2_28GBd_5ch_SSNLW
│   ├── DP16QAM_RRC0.2_34GBd_5ch_SSNLW
│   ├── SP16QAM_RRC0.01_28GBd_1ch_SSNLW
│   ├── SP16QAM_RRC0.1_28GBd_1ch_SSNLW
│   ├── SP16QAM_RRC0.2_28GBd_1ch
│   ├── SP16QAM_RRC0.2_28GBd_1ch_SSNLW
│   └── SPQPSK_RRC0.2_28GBd_1ch_SSNLW
└── source
    ├── 16QAM65536_mt19937ar.h5.dvc
    └── QPSK65536_mt19937ar.h5.dvc
```

`815km_SSMF` contains the transmission signal which has been intentionally resampled to 2 samples/symbol to compress its size. `source` contains the symbol sequences loaded into AWG after proper pulse-shaping.

`DP16QAM_RRC0.2_28GBd_1ch_SSNLW` is human readable label of its corresponding experiments, which can be interpreted as terms 'Dual Polarization, 16-QAM, rooted raised cosine with rolloff factor 0.2, baudrate is 28GBd, single channel transmission and single(or same or shared) source narrow linewidth laser'

`LP-20_1.h5.dvc` is the mentioned record file linking to actual data `LP-20_1.h5`, whose name means 'the #1 sequence with launched power of -2 dBm'. On the other hand, `.h5` format is prefered since it is open and widely supported. For example, see [pyh5](https://www.h5py.org/) and [Matlab](https://www.mathworks.com/help/matlab/import_export/importing-hierarchical-data-format-hdf5-files.html) for data import helps if you are Python and Matlab users.


## Use dvc to download data

DVC is cross-platformed, you need to [install](https://dvc.org/doc/install) it first before you can get the actual data from remote store.

assume you have dvc(cli version) installed, to get files, in your termimal, input
```
mkdir sample_data && cd sample_data
dvc get https://github.com/remifan/LabPtPTm1 data/recv/DP16QAM_RRC0.2_28GBd_1ch/LP-20_1.h5
dvc get https://github.com/remifan/LabPtPTm1 data/sent/16QAM65536_mt19937ar.h5
```

you can also download a folder with its contents (>x00 MB)
```
dvc get https://github.com/remifan/LabPtPTm1 data/recv/DP16QAM_RRC0.2_28GBd_1ch
```

Similarily, download the whole dataset is easy (~5GB)

```
dvc get https://github.com/remifan/LabPtPTm1 data
```

you may see [dvc get](https://dvc.org/doc/command-reference/get) for more details of this command

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

