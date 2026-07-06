# class GenericDriver(RasterDriver):
#     def can_open(self, src):
#         return True

#     def open(self, path):

#         with rasterio.open(path) as src:
#             cube = src.read()

#             sensor = SensorDetector.detect(src)

#             return RasterDataset(...)
