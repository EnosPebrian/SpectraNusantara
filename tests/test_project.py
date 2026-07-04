from spectranusantara.project import Project


def test_create_project():
    project = Project()

    assert project.name == "Untitled Project"
    assert len(project.rasters) == 0
    assert len(project.targets) == 0
