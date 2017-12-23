#include <Python.h>

static PyObject hello_world(PyObject *self, PyObject *args)
{
	PyObject *ret = PyString_FromString("Hello World! 42");
	
	return ret;
}

static PyMethodDef ModuleMethods[] = {
	{ "hello_world", "hello_world", METH_VARARGS, "Says 'Hello'" }
};

DL_EXPORT(void) initmodule(void)
{
	Py_InitModule("hello", ModuleMethods);
}

