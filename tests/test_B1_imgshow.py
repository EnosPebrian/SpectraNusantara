from spectranusantara.raster.reader import RasterReader
from pathlib import Path

path = Path(
    r"D:/Work/Sumatera/Aceh/PT LLI/ASTER/ASTER L1T Calang 2006/ASTER 2006 Stack.tif"
)


def test_B1_imgshow():
    dataset = RasterReader.open(path)
