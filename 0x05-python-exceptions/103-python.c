#include <Python.h>

/**
 * print_python_bytes - prints bytes info
 * @p: the python object in question
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	ssize_t size, i, limit;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);
	for (i = 0; i < limit; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	}
	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - prints float info
 * @p: the python object in question
 */
void print_python_float(PyObject *p)
{
	double v;
	char *f_name;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	v = ((PyFloatObject *)p)->ob_fval;
	f_name = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", f_name);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - prints list info
 * @p: the python object in question
 */
void print_python_list(PyObject *p)
{
	ssize_t size, i;
	PyObject *o;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		o = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((o)->ob_type)->tp_name);
		if (PyBytes_Check(o))
			print_python_bytes(o);
		if (PyFloat_Check(o))
			print_python_float(o);
	}
	setbuf(stdout, NULL);
}
