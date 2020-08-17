# Disabling the Task Manager
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/159ce710186b46b1a41a9804b6f6b959)](https://www.codacy.com/manual/ThomasThelen/Disable-Task-Manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ThomasThelen/Disable-Task-Manager&amp;utm_campaign=Badge_Grade)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

Example of modifying Windows registry values. This example disables the Windows Task Manager.
## Background

For whatever reason, some people have reason to restrict access to the task manager. Maybe you're a researcher running a long computation and don't want anyone killing your process. Maybe you're a sysadmin trying to lock a computer down. Maybe you're an asshole and don't want people killing your fake av process. An incredible obtrusive way to disable it is by modifying the value of the `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskMgr` key.
Note that [Malwarebytes](https://blog.malwarebytes.com/detections/pum-optional-disabletaskmgr/) flags this.

The key in question resides at 

Key Location: `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`

with

Key Name: `DisableTaskMgr`

Setting this to `1` (true) should be a first order approximation to preventing access to the control panel

## Code

The code is fairly simple. It doesn't take into account that the Key Location doesn't exist. It uses the `winreg` module to first open, then write, and close the registry.
