import sys

from src.app.main import list_installed_packages


def test_list_installed_packages_returns_list():
    packages = list_installed_packages()
    assert isinstance(packages, list)


def test_each_package_has_name_and_version():
    packages = list_installed_packages()
    assert len(packages) > 0
    for pkg in packages:
        assert "name" in pkg
        assert "version" in pkg


def test_packages_sorted_alphabetically():
    packages = list_installed_packages()
    names = [p["name"].lower() for p in packages]
    assert names == sorted(names)


def test_python_version():
    assert sys.version_info >= (3, 10)
