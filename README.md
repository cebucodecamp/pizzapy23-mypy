PizzaPY 23: MyPY

Murat presents static type checking for Python, using [MyPy](http://mypy-lang.org/) at [PizzaPY 23](https://www.meetup.com/PizzaPy-PH/events/235261664/).

Have a look at [presentation.org](./presentation.org) for the presentation notes.

To play around with the examples in this repository, follow these steps:

1. Clone the repo

    git clone https://github.com/cebucodecamp/pizzapy23-mypy.git

2. Run a demo file:

    pizzapy23-mypy$ ./mymypy demo1.py
    demo1.py:3: error: Incompatible types in assignment (expression has type "str", variable has type "int")
