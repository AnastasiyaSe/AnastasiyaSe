from app import  get_doc_owner_name
import pytest

class TestSomething:

    def setup(self):
        print("method setup")

    @pytest.mark.parametrize('number', 'name',[('2207 876234', 'Василий Гупкин'),("11-2", "Геннадий Покемонов"),("10006", "Аристарх Павлов")])
    def doc_owner_name(self, number, name):
        assert get_doc_owner_name(number) == name


    def teardown(self):
        print("method teardown")