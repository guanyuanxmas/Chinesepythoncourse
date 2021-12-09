#组
import re
a = 'PythonPythonPythonPythonPython'

r = re.findall('(Python){3}(JS)', a)
print(r)