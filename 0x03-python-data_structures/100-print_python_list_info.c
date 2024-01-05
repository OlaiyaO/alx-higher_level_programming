#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	PyObject *item;

	size = Py_SIZE(list);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GET_ITEM(list, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
