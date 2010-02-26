import glob 
import nose.tools
import test_basics
import test_None

test_suite = [
    'test_None',
    'test_basics',
    'test_strings'
    ]
# test_suite = glob.glob("test*.py")

for test in test_suite:
    response = nose.run(argv=['','--tests='+test,'--stop'])
    if not response:
        break 
