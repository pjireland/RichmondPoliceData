# Richmond Police Activity repository

This repository contains scripts and reports of Richmond Police Department and Wayne
County Sheriff's Department activity, as reported by these agencies in their
media reports (see https://sheriff.co.wayne.in.us/media-reports.html]
and [http://www.co.wayne.in.us/rpdmedia.html, respectively).
The data are taken from 2018 reports by default, but 
a different date range can be selected if the user would like to customize
these reports (see *Level 3: Generate New Reports* below).

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

  A. The command `create_map()` is called to generate the maps.
  B. The following optional arguments can be passed:
     i. `add_dots`: `True` or `False`. `True` by default. Includes dots showing each recorded police activity.
        More information can be obtained about the activity by clicking a dot.
     ii. `static_heat_map`: `True` or `False`. `True` by default.  Includes a static heat map of the police 
        activity.
     iii. `time_lapse_heat_map`: `True` or `False`. `False` by default.  Generates a month-by-month series
        of heat maps.
     iv. `include`: Empty by default.  A list of words to limit the police activity to. If this argument is 
        not provided, all activity will be shown.
     v. `exclude`: Empty by default. Ignore police reports that contain any of the words in this list.

