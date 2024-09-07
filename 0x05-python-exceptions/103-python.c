#include <Python.h>
#include <stdio.h>
#include <floatobject.h>
#include <object.h>

/**
* print_python_list - prints basic info about Python lists
* @p: PyObject representing a Python list
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;

fflush(stdout);
if (!PyList_Check(p)) {
printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

for (i = 0; i < size; i++) {
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);

if (PyBytes_Check(item)) {
print_python_bytes(item);
} else if (PyFloat_Check(item)) {
print_python_float(item);
}
}
}

/**
* print_python_bytes - prints basic info about Python bytes objects
* @p: PyObject representing a Python bytes object
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *string;

fflush(stdout);
printf("[.] bytes object info\n");

if (!PyBytes_Check(p)) {
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", string);
printf("  first %zd bytes: ", size < 10 ? size + 1 : 10);

for (i = 0; i < size && i < 10; i++) {
printf("%02x ", (unsigned char)string[i]);
}
printf("\n");
}

/**
* print_python_float - prints basic info about Python float objects
* @p: PyObject representing a Python float object
*/
void print_python_float(PyObject *p)
{
double value;

fflush(stdout);
printf("[.] float object info\n");

if (!PyFloat_Check(p)) {
printf("  [ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AsDouble(p);
printf("  value: %g\n", value);
}
