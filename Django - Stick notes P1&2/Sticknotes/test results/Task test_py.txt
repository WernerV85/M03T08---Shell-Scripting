'''Test unit to test the tasks of the sticky_notes app.
Testing to see the following:
- Creation of a task
- Retrieval of all tasks
- Updating a task
- Marking task as completed
- Deletion of a task'''

from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskModelTestCase(TestCase):

    def setUp(self):
        # Create a sample task for testing
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            author="Test Author",
            completed=False,
            priority="medium",
            category="work"
        )

    def test_create_task(self):
        """Test creating a new task"""
        task = Task.objects.create(
            title="New Task",
            description="New Description",
            author="Author"
        )
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "New Task")
        self.assertFalse(task.completed)

    def test_task_str(self):
        """Test the string representation of a task"""
        self.assertEqual(str(self.task), "Test Task")

    def test_get_all_tasks(self):
        """Test retrieving all tasks"""
        tasks = Task.objects.all()
        self.assertIn(self.task, tasks)
        self.assertEqual(tasks.count(), 1)

    def test_update_task(self):
        """Test updating a task"""
        self.task.title = "Updated Title"
        self.task.description = "Updated Description"
        self.task.save()
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.description, "Updated Description")

    def test_mark_task_as_completed(self):
        """Test marking a task as completed"""
        self.task.completed = True
        self.task.save()
        completed_task = Task.objects.get(id=self.task.id)
        self.assertTrue(completed_task.completed)

    def test_delete_task(self):
        """Test deleting a task"""
        task_id = self.task.id
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)
