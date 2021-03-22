# LabPtPTm1

LabPtPTm1(Lab dataset series - point to point link transmission data no. 1)

this dataset is collected in Aug. 2019 which is described and partially used in our [paper](https://www.nature.com/articles/s41467-020-17516-7).


## This is a dataset registry

This repo does not host the data itself, instead, it is the [DVC](https://dvc.org/doc/use-cases/data-registries) registry(index) of the dataset which is stored in [AWS S3](https://aws.amazon.com/s3/) bucket.

The files naming is self-explained exampled as below

```
data
├── recv
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
└── sent
    ├── 16QAM65536_mt19937ar.h5.dvc
    └── QPSK65536_mt19937ar.h5.dvc
```

`recv` contains the sampled wavforms which has been intentionally resampled to 2 samples/symbol (80GSa/s -> 56GSa/s) to compressed its size, `sent` is the symbol sequence loaded into AWG which repeatly emits pulse shaped samples through its DACs.
`DP16QAM_RRC0.2_28GBd_1ch_SSNLW` is human readable meta of its corresponding experiments, which can interpreted as parameter terms 'Dual Polarization, 16-QAM, rooted raised cosine with rolloff factor 0.2, baudrate is 28GBd, single channel and single(or same or shared) source narrow linewidth laser'
`LP-20_1.h5.dvc` is the meta file of its recording data file `LP-20_1.h5` which is stored remotely as hdf5 format. h5 file is open and widely supported, for example, see [pyh5](https://www.h5py.org/) and [Matlab](https://www.mathworks.com/help/matlab/import_export/importing-hierarchical-data-format-hdf5-files.html) for helps if you are Python and Matlab users.


## Download actual data

DVC is cross-platformed, you need to [install](https://dvc.org/doc/install) first before you can get the actual data from remote store.

Assume you have dvc(cli version) installed, in your termimal, input
```
mkdir sample_data && cd sample_data
dvc get https://github.com/remifan/LabPtPTm1 data/recv/DP16QAM_RRC0.2_28GBd_1ch/LP-20_1.h5
dvc get https://github.com/remifan/LabPtPTm1 data/sent/16QAM65536_mt19937ar.h5
```

In addition, you can also download a folder with its contents (might be large in size)
```
dvc get https://github.com/remifan/LabPtPTm1 data/recv/DP16QAM_RRC0.2_28GBd_1ch
```

Similarily, download the whole dataset is easy (~5GB)

```
dvc get https://github.com/remifan/LabPtPTm1 data
```

you may see [dvc get](https://dvc.org/doc/command-reference/get) for more details of its commands

## License

to be determined

