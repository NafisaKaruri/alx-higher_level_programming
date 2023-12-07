#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list -
 * @p:
 */
void print_python_list(PyObject *p)
{
	unsigned int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];
		
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes -
 * @p:
 */
void print_python_bytes(PyObject *p)
{
	unsigned int i, b;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		b = 10;
	else
		b = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", b);
	for (i = 0; i < b; i++)
	{
		printf("%02hhx", PyBytes_AsString(p)[i]);
		if (i == (b - 1))
			printf("\n");
		else
			printf(" ");
	}
}
