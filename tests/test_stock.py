"""Test cases for the __main__ module."""
import pytest
from vs_data.stock import batch_upload
from vs_data import log


@pytest.mark.fmdb
@pytest.mark.wcapi
def test_get_batches_awaiting_upload_join_acq(vsdb_connection):
    batches = batch_upload.get_batches_awaiting_upload_join_acq(vsdb_connection)
    log.debug(batches)
    assert batches

def test_get_products_by_id(wcapi):