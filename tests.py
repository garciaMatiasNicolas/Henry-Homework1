import unittest
from unittest.mock import patch
from users import Users

class TestUsers(unittest.TestCase):

    @patch('utils.utils.read_json_file')
    @patch('utils.utils.write_json_file')
    def test_user_registration(self, mock_write, mock_read):
        mock_read.return_value = []
        Users.user_registration("Ana", "García", "ana@mail.com", "1234")
        mock_write.assert_called_once()

    @patch('utils.utils.read_json_file')
    def test_list_users(self, mock_read):
        mock_read.return_value = [{"id": 1, "email": "ana@mail.com"}]
        usuarios = Users.list_users()
        self.assertEqual(len(usuarios), 1)

    @patch('utils.utils.read_json_file')
    @patch('utils.utils.write_json_file')
    def test_delete_user(self, mock_write, mock_read):
        mock_read.return_value = [{"id": 1, "email": "ana@mail.com"}]
        Users.delete_user(1)
        mock_write.assert_called_once()


if __name__ == '__main__':
    unittest.main()

