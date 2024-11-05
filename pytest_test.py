def test_package_import():
    try:
        from my_package import nonstandardcode
    except ImportError as e:
        assert False, f"Import failed: {e}"
    assert True, "Package installed and import successful"