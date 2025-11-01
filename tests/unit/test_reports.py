"""
Unit tests for report generation
"""
import pytest
from app.reports import PDFReport, ExcelReport
from datetime import datetime

@pytest.fixture
def sample_data():
    return {
        'items': [
            {'name': 'Item 1', 'quantity': 10, 'category': 1},
            {'name': 'Item 2', 'quantity': 20, 'category': 2}
        ],
        'date': datetime.now(),
        'service': 'Test Service'
    }

def test_pdf_report_generation(sample_data):
    """Test PDF report generation"""
    report = PDFReport('stock_balance')
    pdf_data = report.generate(sample_data)
    assert pdf_data is not None
    assert len(pdf_data) > 0

def test_excel_report_generation(sample_data):
    """Test Excel report generation"""
    report = ExcelReport('stock_movement')
    excel_data = report.generate(sample_data)
    assert excel_data is not None
    assert len(excel_data) > 0

def test_report_validation():
    """Test report parameter validation"""
    with pytest.raises(ValueError):
        PDFReport('invalid_report_type')

def test_report_data_processing(sample_data):
    """Test data processing for reports"""
    report = PDFReport('stock_balance')
    processed_data = report._process_data(sample_data)
    assert len(processed_data['items']) == 2
    assert processed_data['total_items'] == 30  # 10 + 20
