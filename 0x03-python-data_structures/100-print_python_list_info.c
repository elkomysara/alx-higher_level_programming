#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type_name);
    }
}
