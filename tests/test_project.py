from spectranusantara.models.sample import Sample


def test_create_sample():

    sample = Sample()

    assert sample.name == "Untitled Sample"

    assert sample.easting is None
