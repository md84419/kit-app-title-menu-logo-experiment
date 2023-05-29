# Omniverse kit-app-title-menu-logo-experiment [robotica.example.app.logo]

A scratch space for exploring and experimenting with an app logo that spans the title and menu bars.

![](./source/extensions/robotica.example.app.logo/data/preview.png)



# Getting Started
## Requirements
- NVIDIA Omniverse Launcher
- An Omniverse App (Create, Code, etc)
- Kit 104.1 or later
- Tested with Code 2022.3.3

```
> .\link_app.bat
> .\runbuild.bat
```

# Background
## User Story
As a marketing exec, I want to brand our company apps so that they are visually distinctive and easily
identifiable, delivering 5 key benefits:
  -  Brand recognition - establish and reinforce brand identify, as a visual representation of our company
  and its values
  -  Professionalism and credibility, emphasising that we pay attention to detail and instilling confidence
  in users, allowing them to trust and engage with the app
  -  Differentiation and memorability, building a connection with our target audience

## The solution
Omniverse currently provides limited ability to control the Chrome for applications.  This experiment provides
a way to work around those limitations to create a more distinctive app design.  This should be considered a
temporary workaround until Omniverse provides a better solution: we're taking advantage of undocumented features
about the way that Omniverse currently works, which results in fragile code which is likely to break in future
Omniverse releases.

This experiment is designed for and only works when running on Microsoft Windows.

This is example code. It is not ready for production use and has not been optimised. It is unlikely to scale well.

# Feature tracking
Two feature requests have been logged related to this ticket.
- [OVC-2561 - Positioning of title in main window](https://nvidia-omniverse.atlassian.net/servicedesk/customer/portal/4/OVC-2561)
- [Forum discussion 254770 - UI Apps - Finer-grained control of main window chrome](https://forums.developer.nvidia.com/t/ui-apps-finer-grained-control-of-main-window-chrome/254770)

# Contributing
The source code for this repository is provided as-is. We only accept outside contributions from individuals who have
signed an Individual Contributor License Agreement.
