import pytest
from librarian import Librarian

class TestLibrary:

    @pytest.mark.skip(reason="Not implemented yet")
    def test_add_librarian(self):
        pass

    def test_librarian_record_count(self):
        lib = Librarian()
        lib.cursor.execute('SELECT * FROM librarians')
        num = lib.cursor.fetchall()
        assert len(num) == 5

    """@pytest.mark.xfail(reason="Feature not ready")
    def test_remove_librarian(self):
       """

