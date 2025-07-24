import os
import subprocess
import sys

import pytest

# Add the src directory to sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)


def test_package_installation():
    """Test if the package can be imported and its modules are accessible."""
    try:
        import house_pricing_predictor
    except ImportError as e:
        pytest.fail(f"Package import failed: {str(e)}")

    try:
        from house_pricing_predictor import main
    except ImportError as e:
        pytest.fail(f"Failed to import main module: {str(e)}")

    try:
        from house_pricing_predictor import data_ingestion
    except ImportError as e:
        pytest.fail(f"Failed to import DataIngestion module: {str(e)}")

    try:
        from house_pricing_predictor import model_training
    except ImportError as e:
        pytest.fail(f"Failed to import ModelTraining module: {str(e)}")

    try:
        from house_pricing_predictor import model_scoring
    except ImportError as e:
        pytest.fail(f"Failed to import ModelScoring module: {str(e)}")

    try:
        from house_pricing_predictor.data_ingestion import load_housing_data

        assert callable(load_housing_data)
    except ImportError as e:
        pytest.fail(
            f"Failed to import load_housing_data function from DataIngestion module: {str(e)}"
        )

    try:
        from house_pricing_predictor.model_training import model_training

        assert callable(model_training)
    except ImportError as e:
        pytest.fail(
            f"Failed to import model_training function from ModelTraining module: {str(e)}"
        )

    try:
        from house_pricing_predictor.model_scoring import model_scoring

        assert callable(model_scoring)
    except ImportError as e:
        pytest.fail(
            f"Failed to import model_scoring function from ModelScoring module: {str(e)}"
        )
