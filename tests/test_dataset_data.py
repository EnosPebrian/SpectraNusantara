from spectranusantara.raster.reader import RasterReader
from pathlib import Path

path = Path(r"D:/Programming/SpectraNusantara/tests/AST Dummy.tif")


def test_reading_data_raster():
    dataset = RasterReader.open(path)
    assert dataset.name
    assert dataset.band_count == 3
    assert dataset.data.shape[0] == 3
    assert dataset.data.shape[1] == 811
    assert dataset.data.shape[2] == 921
