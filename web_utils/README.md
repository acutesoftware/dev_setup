## Dev_setup - web utils
Currently a web site generator for flask apps

### Setup

Create a YAML file using existing example as template (with a different op folder)

create a build script

run the build script

go to the OUTPUT_FOLDER_yourfolder and run GO.BAT


#### Sample YAML File

~~~~
---

filenames:
    proj_name: lifepim
    css: lifepim.css
    htm: lifepim.html
    
    
colour_themes:
    - nme: Plain
      fg: Black
      bg: White

screen:
    max_width: 1920
    max_height: 1080
    colour_theme: Plain

widgets:
    - nme: Header
      x: 0
      y: 0
      w: 100%
      h: 160px
    - nme: Top Menu
      x: 0
      y: 100
      w: 100%
      h: 80px
    - nme: Side Menu
      x: 0
      y: 120
      w: 180px
      h: 100%
    - nme: Main
      x: 180
      y: 240
      w: 100%
      h: 100%
    - nme: Footer      
      x: 180
      y: 1000
      w: 100%
      h: 200px
      
    
top_menu:
    - Home
    - Diary
    - Tasks
    - Contacts
    - Notes
    - Photos
    - About
    
    
side_menu:
    - Lists
    - Setup
    
~~~~