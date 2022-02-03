import src.Admin as Admin
import src.DataManager as DataManager
import src.Instructor as Instructor
import src.Student as Student
import unittest


class TestAdmin(unittest.TestCase):

    def setUp(self):
        '''
        This method automatically gets called before every test.
        '''
        DataManager.reset()

    def test_nocourse(self):
        '''
        EXAMPLE TEST
        This method checks that a random course doesn't exist before cretion
        '''
        self.assertIsNone(DataManager.findCourse("ecs999", 2022))

    def test_class_does_not_exist(self):
        '''
        EXAMPLE TEST
        This method checks that a random course doesn't exist before cretion
        '''
        self.assertTrue(Admin.classExists("ecs161", 2022) == False)

    def test_class_exists(self):
        """
        EXAMPLE TEST
        This test creates a course, and checks that we
        can find the course.
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        self.assertTrue(Admin.classExists("ecs161", 2022))

    def test_newcourse(self):
        """
        EXAMPLE TEST
        This test creates a course with a name, for a year, and checks that
        a) The course with this name, and year is created correctly, and exists. 
        b) The course instructor is set correctly.
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        course = DataManager.findCourse("ecs161", 2022)
        self.assertIsNotNone(course)
        self.assertEqual(
            DataManager.courseInstructors[course],  "Prem Devanbu")

    def test_newEnrollee(self):
        """YOU MUST WRITE THIS TEST
        This test creates a course, and an enrolls a student,
        and then checks that the student is indeed in the class. Use
        functions in Admin.py and Student.py
        """
        pass

    def test_change_capacity(self):
        """YOU MUST WRITE THIS TEST
        This test creates a course, changes the capacity
        and then ensures that the capacity has indeed changed
        to the new value 
        """
        pass


class TestHomework(unittest.TestCase):

    def setUp(self) -> None:
        """This gets run before every test. 
        """
        DataManager.reset()

    def test_new_homework(self):
        """This test creates a course, and a homework for that course, and ensures that it exists. 
        YOU MUST WRITE. Use functions in DataManager Some of them will be
        top level functions, others will be methods in specific classes (e.g., Course)
        """
        pass

    def test_newhomework_grade(self):
        """This test creates a course, registers a student in a course,
        adds a homework to the course, assigns a grade for the student,
        and checks that the grade the student actually has for that homework, for that course,
        is the grade that was assigned. 
        YOU MUST WRITE. 
        Use functions in DataManager, Student, Instructor, Admin, etc, as needed
        """
        pass


class TestInstructor(unittest.TestCase):

    def setUp(self) -> None:
        DataManager.reset()

    def test_add_homework(self):
        """EXAMPLE TEST
        Create a course, make sure it exists;
        then add a homework, and check that the homework exists
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        course = DataManager.findCourse("ecs161", 2022)
        self.assertIsNotNone(course)
        Instructor.addHomework("Prem Devanbu", "ecs161", 2022, "HW1")
        self.assertTrue(Instructor.homeworkExists("ecs161", 2022, "HW1"))

    def test_get_grade_with_no_course(self):
        """YOU MUST WRITE THIS TEST
        If you try to get the grade for a student, for a course that does not exist,
        you will get 'None'
        """
        pass

    def test_get_grade_with_no_grading(self):
        """YOU MUST WRITE THIS TEST
        FOr this test, you will create a class, create a homework in that class,
        add a student to that class, but NOT assign a grade for that student (see Instructor.py, for
        the relevant function, but don't call it) and then ensure that the grade for that student is NOne.
        """
        pass

    def test_get_the_grade(self):
        """YOU MUST WRITE THIS TEST
        FOr this test, you will create a class, create a homework in that class,
        add a student to that class, then assign a grade for that student (see Instructor.py, for
        the relevant function) and then ensure that the grade for that student is correct (any
        integer value can be a grade)
        """

        pass

    def test_assign_grade(self):
        """Lab 5
            # 1. create a class        
            # 2. Getting the course information
            # 3. Add a student
            # 4. Add homework
            # 5. Grade the student's homework for that course
            # 6. Retreive the grade
            # 7. Assert that the given grade matches the retreived grade            
        """
        pass


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        DataManager.reset()

    def test_register_for_class_for_no_course(self):
        """YOU MUST WRITE THIS TEST
        If you add a student for a course that does not exist, 
        then the student is not registered for the course. 
        """
        pass

    def test_drop_class(self):
        """YOU MUST WRITE THIS TEST
        This test will a) Create a class, b) register a student for the class, 
        c) drop teh student, and, then after this d) ensure that the student is NOT REGISTERED
        for the class.
        """
        pass

    def test_submit_homework(self):
        """YOU MUST WRITE THIS TEST
        For this test, a) Create a class, b) add a homework, c) add a student
        d) student submits the homework e) now check that teh student has indeed
        submitted the homework. 
        """
        pass

    def test_register_for_class(self):
        """lab5
        Mo's demo
        """
        pass


if __name__ == "__main__":
    unittest.main()
