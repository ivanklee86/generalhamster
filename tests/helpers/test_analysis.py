import app.helpers.analysis as analysis
from tests.utilities.fixtures import categories_data   # noqa: F401


def test_analysis_match(categories_data):  # noqa: F811
    analysis_output = analysis.compare_categories(*categories_data)

    assert not analysis_output


def test_analysis_mismatch(categories_data):  # noqa: F811
    (v1, v2) = categories_data
    v2.pop()

    analysis_output = analysis.compare_categories(v1, v2)

    assert len(analysis_output['fields']) == 3
