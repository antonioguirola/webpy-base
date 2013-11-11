```
Base project Web.py Copyright (C) 2013 Antonio Ángel Guirola Vicente This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.
```

webpy-base
==========

Base project Web.py-mako-MongoDB-Bootstrap-JQuery

## Installation

### Web.py + Mako

```sh
sudo apt-get install python python-pip
sudo pip install web.py
sudo pip install mako
```

### MongoDB

- Download last version from http://www.mongodb.org/downloads
- Useful tutorial in http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/


## Structure

webpy-base
  |
  |- sessions
  |- sql
  |    |-mongo.conf
  |    |-mongo.log
  |
  |- static
  |    |-bootstrap
  |    |     |- All Bootstrap files
  |    |-jquery
  |    |     |- JQuery min files
  |    |-images
  |    |-styles
  |          |-style-base.css
  |
  |- view
  |    |-templates
  |    |     |-base.html
  |    |-footer.html
  |    |-header.html
  |    |-index.html
  |
  |- code.py
  |- config.py
  |- db.py
  |- forms.py
  |- view.py
 

## Versions

- Web.py v0.37
- Mako v0.9.0
- Bootstrap v3.0.0
- JQuery 1.10.2


