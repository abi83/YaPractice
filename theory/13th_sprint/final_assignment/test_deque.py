import unittest

try:
    from deque import Deque
except ModuleNotFoundError:
    assert False, 'File to test not found'


class TestDequeClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            {'name': 'test2',
             'stack_size': 10,
             'commands': [
                 ("push_front", -855), ("push_front", 720), ("pop_back", None),
                 ("pop_back", None), ("push_back", 844), ("pop_back", None),
                 ("push_back", 823),
             ],
             'output': '-855 720 844',
             },
            {'name': 'test4',
             'stack_size': 4,
             'commands': [
                 ("push_front", 861), ("push_front", -819), ("pop_back", None),
                 ("pop_back", None)
             ],
             'output': '861 -819',
             },
            {'name': 'test7',
             'stack_size': 7,
             'commands': [
                 ("pop_front", None), ("pop_front", None), ("push_front", 741),
                 ("push_front", 648), ("pop_front", None), ("pop_back", None),
                 ("pop_front", None),
             ],
             'output': 'error error 648 741 error',
             },
        ] 
    
    def test_deque(self):
        for case in TestDequeClass.test_cases:
            with self.subTest(case=case['name']):
                deque = Deque(case['stack_size'])
                output = ''
                for command, parameter in case['commands']:
                    try:
                        if parameter is not None:
                            getattr(deque, command)(parameter)
                        else:
                            answer = str(getattr(deque, command)())
                            output += answer if not output else ' ' + answer
                    except KeyError:
                        output += 'error' if not output else ' error'
                self.assertEqual(output, case['output'])
