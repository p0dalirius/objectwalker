![](./.github/banner.png)

<p align="center">
    A python module to explore the object tree to extract paths to interesting objects in memory.
    <br>
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/objectwalker">
    <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
    <a href="https://www.youtube.com/c/Podalirius_?sub_confirmation=1" title="Subscribe"><img alt="YouTube Channel Subscribers" src="https://img.shields.io/youtube/channel/subscribers/UCF_x5O7CSfr82AfNVTKOv_A?style=social"></a>
    <br>
</p>

## Features

 - [x] Python module to use in pdb after a `breakpoint()`.
 - [x] Standalone tool to explore paths in python modules.
 - [x] Multiple built-in filters.
 - [x] Possibility to implement custom filters and pass them to ObjectWalker().

## Demonstration

https://user-images.githubusercontent.com/79218792/234614877-19b5e5b8-a52b-4f4d-a4aa-4cda0b7ddf96.mp4

## Installation

You can now install it from pypi (latest version is <img alt="PyPI" src="https://img.shields.io/pypi/v/objectwalker">) with this command:

```
sudo python3 -m pip install objectwalker
```

## Example commands

 + We want to find all the paths to the `os` module in the module `jinja2`:
    ```
    objectwalker -m jinja2 --filter-object-is-module os --max-depth 15
    ```
    We get the following output:
    ![](./.github/find_module_os_in_jinja2.png)

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.
