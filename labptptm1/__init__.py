import zarr

dataset = zarr.open_group("simplecache::s3://optcommpubdataqrfan/labptptm1_zarr",
                          storage_options={"s3": {'anon': True}})
