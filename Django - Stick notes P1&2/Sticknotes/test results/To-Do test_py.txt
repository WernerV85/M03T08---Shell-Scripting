''' Test unit to test the todo list of the sticky_notes app.
Testing to see the following:
- Creation of a todo list
- Retrieval of all todo lists
- Updating a todo list
- Marking todo list as completed
- Deletion of a todo list
'''

from django.test import TestCase
from .models import TodoList
from datetime import date


class TodoListModelTestCase(TestCase):

    def setUp(self):
        # Create a sample todo list for testing
        self.todo_list = TodoList.objects.create(
            title="Test Todo",
            entry="Test Entry",
            author="Test Author",
            is_completed=False,
            estimated_due_date=date(2026, 1, 15)
        )

    def test_create_todo_list(self):
        # Test creating a new todo list
        todo_list = TodoList.objects.create(
            title="New Todo",
            entry="New Entry",
            author="Author",
            estimated_due_date=date(2026, 1, 20)
        )
        self.assertIsInstance(todo_list, TodoList)
        self.assertEqual(todo_list.title, "New Todo")
        self.assertFalse(todo_list.is_completed)

    def test_todo_list_str(self):
        # Test the string representation of a todo list
        self.assertEqual(str(self.todo_list), "Test Todo")

    def test_get_all_todo_lists(self):
        # Test retrieving all todo lists
        todo_lists = TodoList.objects.all()
        self.assertIn(self.todo_list, todo_lists)
        self.assertEqual(todo_lists.count(), 1)

    def test_update_todo_list(self):
        # Test updating a todo list
        self.todo_list.title = "Updated Title"
        self.todo_list.entry = "Updated Entry"
        self.todo_list.save()
        updated_todo_list = TodoList.objects.get(id=self.todo_list.id)
        self.assertEqual(updated_todo_list.title, "Updated Title")
        self.assertEqual(updated_todo_list.entry, "Updated Entry")

    def test_mark_todo_list_as_completed(self):
        # Test marking a todo list as completed
        self.todo_list.is_completed = True
        self.todo_list.save()
        completed_todo_list = TodoList.objects.get(id=self.todo_list.id)
        self.assertTrue(completed_todo_list.is_completed)

    def test_delete_todo_list(self):
        # Test deleting a todo list
        todo_list_id = self.todo_list.id
        self.todo_list.delete()
        with self.assertRaises(TodoList.DoesNotExist):
            TodoList.objects.get(id=todo_list_id)
