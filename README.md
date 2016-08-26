# End-user App Deployment
This project highlights the unique capabilities of [`conda-build`](http://conda.pydata.org/docs/building/recipe.html) and [`constructor`](https://www.continuum.io/blog/developer-blog/introducing-constructor) to build Python (or other source-code) packages and create a self-contained installer that includes all of the packages your app requires to run. This procedure is cross-platform and will work on Mac, Linux and Windows.

## The PyQT App
The `my_versions` App I wish to deploy to my end-users requires that following Python packages be installed. It is a simple PyQt app this displays the version numbers of these packages.

* gdal
* numpy
* pandas
* matplotlib

### Setuptools
For this demonstration I have written a minimal [`setup.py` script](./setup.py) that just defines a `gui_script` entry point. See [Python Apps, The Right Way](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/) for more information about Setuptools and entry points.

## Conda recipe
The [`conda.recipe`directory](./conda.recipe) is used to build a [`conda package`](http://conda.pydata.org/docs/index.html) which specifies the required packages to build and run the `my_versions` app.

Further, there is a [`menu-windows.json`](./conda.recipe/menu-windows.json) file that will install a Start Menu entry when the package is installed on Windows. This uses the [Menuinst](https://github.com/ContinuumIO/menuinst) project.

### Building the package
The conda package must be built separately on a Mac, Windows and Linux machine by cloning this repository and running

```
conda build conda.recipe
```

See the [`conda-build` documentation](http://conda.pydata.org/docs/building/recipe.html) for more information.

Note: at this time only Python 3.4 is supported on Windows for this package because `gdal` has been compiled for Ptyhon 3.4 and not Python 3.5.

### Anaconda Cloud
The final step in generating the conda package is to upload the package files to your [Anaconda Cloud](anaconda.org) channel with the following command.

```
anaconda upload /path/to/<filename>.bz2
```

See the [Anaconda Cloud documentation](https://docs.continuum.io/anaconda-cloud/using) for more information.

## Constructor
Now that the conda package for the `my_versions` app has been built and uploaded to [my channel](anaconda.org/defusco/my_versions) on [Anaconda Cloud](anaconda.org) we can build the self-contained installer for Mac, Linux and Windows using [`constructor`](https://www.continuum.io/blog/developer-blog/introducing-constructor), which is the tool used to make the [Anaconda Installers](https://www.continuum.io/downloads).

`constructor` requires a [`construct.yaml` file](./constuct.yaml) file which specifies the desired conda packages to be downloaded and packaged into the installer.

Since the `my_versions` conda package already defines all of its required packages I only need specify the correct version of Python for each architecture.

```yaml
name: MyVersions
version: 1.0

channels:
  - http://repo.continuum.io/pkgs/free/
  - http://conda.anaconda.org/defusco

specs:
  - python 3.4* [win]
  - python 3.5* [not win]
  - menuinst    [win]
  - my_versions
```

Note: the `menuinst` package has been included to ensure that the Windows Start Menu item is installed for `my_versions`.

To build the installer, first install `constructor` in your root conda env.

```
conda install constructor
```

Now just run `constuctor`.

```
constructor .
```

Constructor will create a file called `MyVersions-1.0-MacOSX-x86_64.sh` on Mac and one called MyVersions-1.0-Windows-x86_64.exe` on Windows.

These installer files will be over 200 MB each since *every* required Python package need to be included.

### Installing MyVersions
The installer files can be shipped to other users for them to install.

Note: **Other users do not need to have Anaconda Installed or know how to work with conda**
