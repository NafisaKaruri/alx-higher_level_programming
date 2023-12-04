#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: a python object (list)
 */
void print_python_list_info(PyObject *p)
{
	unsigned int i;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		if (item != NULL)
		{
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
		}
		else
		{
			printf("Element %d: NULL\n", i);
		}
	}
}
