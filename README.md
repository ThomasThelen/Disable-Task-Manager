# Disable-Control-Panel
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

Example of disabling the Windows Task Manager via registry manipulation.
## Background

Access to the Task Manager is dictated by a flag in the registry. An incredible obtrusive way to disable it is by modifying the value of the key.
Note that [Malwarebytes](https://blog.malwarebytes.com/detections/pum-optional-disabletaskmgr/) flags this.

The key in question resides at 

Key Location: `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`

with

Key Name: `DisableTaskMgr`

Setting this to `1` should prevent access to the control panel

## Code

The code is fairly simple. It doesn't take into account that the Key Location doesn't exist. It uses the `winreg` module to first open, then write, and close the registry.