# PizzaPY 23: MyPY

Murat presents static type checking for Python, using [MyPy](http://mypy-lang.org/) at [PizzaPY 23](https://www.meetup.com/PizzaPy-PH/events/235261664/).

## What's here?

* Have a look at [presentation.org](./presentation.org) for the presentation notes.
* There's a bunch of demo files that show particular features of MyPy. See notes below how to try them out quickly.
* The docker image is available at [Docker Hub](https://hub.docker.com/r/cebucodecamp/pizzapy23-mypy/)

## Get started with the demo files

To play around with the examples in this repository, follow these steps:

1. Clone this repo.

On the commandline type:

    git clone https://github.com/cebucodecamp/pizzapy23-mypy.git

2. Run a demo file.

Switch to the directory.

    $ cd pizzapy23-mypy

Then check one of the demo files. You should immediately get the error:

    $ ./mymypy demo1.py
    demo1.py:3: error: Incompatible types in assignment (expression has type "str", variable has type "int")

Then look at the demo files, modify them and run the check again to see the difference.

Happy coding! :)
