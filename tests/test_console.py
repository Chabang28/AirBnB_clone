import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.console.postloop()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, command, mock_stdout=None):
        if not mock_stdout:
            mock_stdout = self.mock_stdout
        with patch('sys.stdout', mock_stdout):
            self.console.onecmd(command)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_command(self):
        with patch('models.storage') as mock_storage:
            mock_storage.all.return_value = {}
            self.assert_stdout("f1r57-1n574nc3\n", "create BaseModel")

    def test_show_command(self):
        obj = BaseModel()
        self.assert_stdout(str(obj) + '\n', "show BaseModel {}".format(obj.id))

    def test_destroy_command(self):
        obj = BaseModel()
        self.assert_stdout("", "destroy BaseModel {}".format(obj.id))
        self.assertNotIn(obj, storage.all().values())

    def test_all_command(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assert_stdout("[{}, {}]\n".format(str(obj1), str(obj2)), "all BaseModel")

    def test_update_command(self):
        obj = BaseModel()
        self.assert_stdout("", 'update BaseModel {} name "New Name"'.format(obj.id))
        updated_obj = storage.all()['BaseModel.' + obj.id]
        self.assertEqual(updated_obj.name, "New Name")

    def test_invalid_commands(self):
        invalid_commands = [
            "create InvalidClass",
            "show InvalidClass",
            "destroy InvalidClass",
            "all InvalidClass",
            "update InvalidClass"
        ]
        expected_output = "** class doesn't exist **\n"
        for command in invalid_commands:
            self.assert_stdout(expected_output, command)

    def test_empty_line_command(self):
        self.assert_stdout("", "")
        
    def test_quit_command(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_help_quit_command(self):
        self.assert_stdout("Quit command to exit the program\n", "help quit")


if __name__ == '__main__':
    unittest.main()

