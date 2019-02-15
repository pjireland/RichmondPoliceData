# Richmond Police Activity repository

This repository contains scripts and reports of Richmond Police Department and Wayne
County Sheriff's Department activity, as reported by these agencies in their
media reports (see https://sheriff.co.wayne.in.us/media-reports.html]
and [http://www.co.wayne.in.us/rpdmedia.html, respectively).
The data are taken from 2018 reports by default, but 
a different date range can be selected if the user would like to customize
these reports (see **Level 3: Generate New Reports** below).

There are three different levels to which a user can interact with these data,
and the prerequisites and approach for each is given below.

## Level 1: View the existing activity maps

### Prerequisities

None

### Approach

The exisiting data can be analyzed online here:
https://nbviewer.jupyter.org/github/pjireland/RichmondPoliceData/blob/master/activity_map.ipynb.

## Level 2: Generate new maps from the existing dataset

### Prerequisites

1. Install Jupyter using Anaconda and conda following the instructions
[here](https://jupyter.readthedocs.io/en/latest/install.html#id3).

2. Clone this repository:

```
git clone https://github.com/pjireland/RichmondPoliceData.git
```

### Approach

1. Run Jupyter Notebooks from within the cloned `RichmondPoliceData` repository:

```
jupyter notebook
```

and select the `activity_map.ipynb` file.

2. Add additional police maps to the bottom of the notebook.  Some tips for adding these maps:

  * The command `create_map()` is called to generate the maps.
  * The following optional arguments can be passed to the `create_map()` function:
    * `dots`: `True` or `False`. `True` by default. Includes dots showing each recorded police activity.
        More information can be obtained by clicking each dot.
    * `static_heat_map`: `True` or `False`. `True` by default.  Includes a static heat map of the police 
        activity.
    * `time_lapse_heat_map`: `True` or `False`. `False` by default.  Generates a month-by-month series
        of heat maps.
    * `include`: Empty by default.  A list of words to limit the police activity to. If this argument is 
        not provided, all activity will be shown.
    * `exclude`: Empty by default. Ignore police reports that contain any of the words in this list.

## Level 3: Generate new reports

### Prerequisites

1. A shell with a `bash`.
   * For Unix, Linux, and Mac systems, this should be included by default.
   * For Windows machines, [git bash](https://gitforwindows.org/) can be installed to obtain a bash prompt.

2. [Anaconda](https://www.anaconda.com/distribution/#download-section) and 
   [Jupyter Notebooks](https://jupyter.readthedocs.io/en/latest/install.html#id3)

3. Python client library for Google Maps API Web Services.  This can be installed via the command

```
pip install googlemaps
```

   It is used to geocode (obtain the latitude and longitude) of police incidents.

4. Sign up for a [Google Maps API key](https://developers.google.com/maps/documentation/javascript/get-api-key)

   * Note that that while Google Maps API is a paid service, the monthly free allowances are typically sufficient
     for geocoding the police data, but be careful to not exceed your free allowance.

### Approach
