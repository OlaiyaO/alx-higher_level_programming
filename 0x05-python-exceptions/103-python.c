#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about Python lists
 * @p: Pointer to a Python object (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	size = ((PyVarObject *)p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		
		printf("Element %ld: %s\n", i, PyUnicode_AsUTF8(PyObject_Str(obj_type)));
		Py_XDECREF(obj_type);
		
		if (PyBytes_Check(obj)) 
			print_python_bytes(obj);
		else if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Pointer to a Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", (unsigned char)str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Print information about Python float objects
 * @p: Pointer to a Python object (float)
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
