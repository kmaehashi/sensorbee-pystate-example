# sensorbee-pystate-example

```
$ build_sensorbee
$ ./sensorbee run &
$ ./sensorbee topology create test
$ ./sensorbee shell -t test
```

```
CREATE STATE py_evaluator TYPE pystate WITH
    module_path = "./py",
    module_name = "evaluator",
    class_name = "PyEvaluator";

EVAL pystate_func(
    "py_evaluator",
    "eval",
    "lambda arg1, arg2: filter(lambda v: v % 2 == 0, arg1 + arg2)",
    [1,2,3],
    [4,5,6]);
```
