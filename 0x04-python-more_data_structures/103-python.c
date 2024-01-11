#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject pointer to the bytes object
 */


void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p) || !PyBytes_CheckExact(p))
	{
		printf("[.] bytes object info\n");
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ", PyBytes_Size(p));
	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i)
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer to the list
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		PyObject *element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
