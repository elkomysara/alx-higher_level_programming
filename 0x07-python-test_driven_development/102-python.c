#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python string objects
 * @p: PyObject pointer
 */
void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    
    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  type: compact ascii\n");
    } else {
        printf("  type: compact unicode object\n");
    }

    
    Py_ssize_t length = PyUnicode_GetLength(p);
    printf("  length: %ld\n", length);

    const char *value = PyUnicode_AsUTF8(p);
    printf("  value: %s\n", value);
}
