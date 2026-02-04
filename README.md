# LabPtPTm1

[![CC BY 4.0][cc-by-shield]][cc-by]

Lab dataset series - point to point 815km-SSMF transmission data no. 1.

Experimental transmission of DP-16QAM signal over ~815km SSMF (10 spans) at 28 GBd.
This dataset was collected in Aug 2019.

## Installation

```bash
pip install https://github.com/remifan/LabPtPTm1/archive/main.zip
```

## Usage

```python
from labptptm1 import dataset

# browse the dataset structure
dataset.tree()
```

```
/
├── 815km_SSMF
│   └── DP16QAM_RRC0.2_28GBd_1ch
│       ├── LP-20_1
│       │   ├── recv (3500000, 2) complex64
│       │   └── sent (1750000, 2) complex64
│       ├── LP-20_2
│       ...
└── source
    └── 16QAM65536
        └── src (65536, 2) complex64
```

```python
# access a specific transmission data group
ds = dataset['815km_SSMF/DP16QAM_RRC0.2_28GBd_1ch/LP-20_1']

# view metadata
dict(ds.attrs)  # {'lpdbm': -2.0, 'lpw': 0.000630957344480193}

# load received waveforms (2 samples/symbol, 2 polarizations)
recv = ds['recv'][:]  # shape: (3500000, 2), dtype: complex64

# load synchronized sent symbols
sent = ds['sent'][:]  # shape: (1750000, 2), dtype: complex64

# load source symbols
src = dataset['source/16QAM65536/src'][:]  # shape: (65536, 2), dtype: complex64
```

Data is stored remotely on AWS S3 and downloaded on-demand with local caching.

For a practical example of using this dataset for adaptive equalization, see the
[commplax equalizers tutorial](https://commplax.readthedocs.io/en/latest/tutorial/equalizers.html).

## See also

[LabPtPTm2](https://github.com/remifan/LabPtPTm2) - 1125km 7-channel DP-16QAM WDM transmission using quantum random bit source (Jan 2021)

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

