import warnings
import zarr

# Suppress async warning from zarr since simplecache doesn't support async mode
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', message='.*asynchronous.*', category=UserWarning)
    dataset = zarr.open_group("simplecache::s3://optcommpubdataqrfan/labptptm1_zarr",
                              mode='r',
                              storage_options={"s3": {'anon': True}},
                              use_consolidated=True,
                              zarr_format=2)
