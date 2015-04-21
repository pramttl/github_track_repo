Track your Github project statistics with time
----------------------------------------------

**Warning**: Not ready yet! I'll remove this message when this code is ready to use.

`github_track_repo` is a simple web applicaiton that allows you to follow your favourite github project and see how it is doing over time.

Project
-------

The github project you are tracking. Each project object has the following attribute(s):

```
repo_url = <repo_url>
```

DataPoint
---------
Each datapoint corresponds to a particular project P and a time instant T. It is a collection of the following statistics for a given P and T.

```
P = <reference_to_project>
T = <datetime>
size
stargazers_count
forks_count
open_issues_count
fork
```

The parameter names are self explainatory. Infact since the data is pulled from the Github API itself the terminology and names of these parameters are exactly same as those specified in Github API v3 (Repos)

https://developer.github.com/v3/repos/


Installation
------------

