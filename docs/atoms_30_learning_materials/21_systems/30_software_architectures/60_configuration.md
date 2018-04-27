# Configuration management {#configuration-management status=draft}

Assigned: Andrea

<div class='requirements' markdown="1">

Results: How to deal with configuration effectively.

</div>

## Motivation


### Aside: Python

We use Python examples but the general concepts are applicable
to any programming languages. Some of the idioms here are good for
dynamic object-oriented languages.

## Stages of configuration management: from clueless to pro

We will look at the typical story of how one deals with parameters.

TODO: summary


## The primordial stage (clueless developer)

At the beginning you have:

    def f(x):
        return x * 10 + 1

Then it becomes:

    def f(x):
        # return x * 10 + 1
        return x * 11 + 1

##  Recognition that parameters are important

The next step is making sure that the parameters are extracted from the code

After this step, the code looks much better:

    def f(x):
        a = 10
        b = 1
        y = x * a + b
        return y

Why is it better?

* It separates the "business logic" from the parameters.
* It gives meaningful name to the parameters

### Aside: legibility of code

Note that it is not true that having fewer lines of code means
the code is better! Legibility first.

> Code is for humans to read, and only tangentially for machines to interpret. -???


See: Python manifesto

## Parameters in interfaces

The next step is recognizing the parameters in the interface of the function.

In this case, we might write something like this:

    def f(x, a=10, b=1):
        y = x * a + b
        return y

The next step is encapsulation of the object.


TODO: parameters and defaults


## Encapsulation of functionality objects

For example, consider an image resizing function:

    def resize(y, w, h):
        y = cv2.imresize(x, (w, h))
        return y

Probably the better way is the following.
We create an `ImageResizer` class that is parametrized.

    class ImageResizer():

        def __init__(self, w, h):
            self.w, self.h = w, h

        def __call__(self, x):
            y = cv2.imresize(x, (self.w, self.h))
            return y

Now we can call this object as follows:

    image_filter = ImageResizer(w=200,h=320)

    x = ...
    y = image_filter(x)

Notice that now we have abstracted the interface from the implementation:
after the object is created, we can call it an "image filter", with the
implication that it is "something that given an image into another".

TODO: For example, we can now write a generic `apply_filter` function:

### In Duckietown

TODO: In Duckietown...

## Convenient interfaces

Now, we still have the problem of how the user specified these parameters. We
need some sort of glue that goes from the user interface, which might be the
command line interface, a graphical interface, or configuration files.

It makes sense that this functionality is implemented consistently across the
system.

## Abstracting the configuration

The next step is understanding that a user never wants to deal with single
parameters, but rather we need to give names to entire configurations.

For example, we wight want to say something like:

    image_resizer_large:
        w: 640
        h: 480

    image_resizer_small:
        w: 320
        h: 320

From the point of view of the user, it is easy to experiment.

From the point of view of the developer, it promotes
an approach in which one writes more generic code.

If there

    apply_filters:
        filter_names:
        - image_resizer_large
        - increase_contrast
        - crop_bottom

For example, suppose that there is a magic function

    def instance(name):
        """ Returns an instantiation of the named object """
        ...

Then, one could implement a filter combinations like in the following code. The
initialization parameter is the names of the filters, which are then
instantiated and stored. The `__call__()` function calls all the filters in the
that where defined

    class ApplyFilters():
        def __init__(self, filter_names):
            self.filters = map(instance, filter_names)

        def __call__(self, image):
            for f in self.filters:
                image = f(image)
            return image

## Duckietown solution

We now look at the Duckietown solution for the previous problems.

The code is in [`EasyAlgo`](#easy_algo).




## Beyong: Customization, History tracking
