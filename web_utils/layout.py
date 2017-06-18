#!/usr/bin/python3
# -*- coding: utf-8 -*-
# layout.py
# This is initially a way to define the CSS layout of 
# multiple widgets on the screen and generate the CSS
# files and DIV layouts.
# Later, maybe it could be used in a dynamic way to 
# adjust widget sides via frames, but there is likely 
# to be an existing JS solution to do this.

import yaml

def define_screen(config_file):
    """
    reads in config file to get widgets and layout screen
    """
    cfg = read_yaml(config_file)
    
    #colour_theme = ColourThemes('plain')
    colour_theme = ColourThemes(cfg['screen']['colour_theme'])
    
    
    
    s = Screen(colour_theme, cfg)
    #s.add_widget(ScreenWidget('Top Menu', x='0', y='100', w='100%', h='100px'))
    for w in cfg['widgets']:
        s.add_widget(ScreenWidget(nme=w['nme'], x=w['x'], y=w['y'], w=w['w'], h=w['h']))
    print(s)
    s.write_css('test.css')

    
def read_yaml(yaml_file):
    """ 
    return a dictionary of the yaml file
    """
    with open(yaml_file, 'r') as stream:
        return yaml.load(stream)

    
class Screen(object):
    """
    Manage the layout of the overall screen
    """
    def __init__(self, colour_theme, cfg):
        self.widgets = []
        self.cfg = cfg
        self.colour_theme = colour_theme
        self.max_width = self.cfg['screen']['max_width']
        self.max_height = self.cfg['screen']['max_height']
        self.cur_x = 0
        self.cur_y = 0
    
    def __str__(self):
        res = 'Screen Layout\n'
        res += 'max_width = ' + str(self.max_width)  + ', max_height = ' + str(self.max_height) + '\n'
        for w in self.widgets:
            res += str(w)
            
        return res
    
    def add_widget(self, widget):
        """
        add a widget to the screen which should auto
        size to the appropriate space
        """
        self.widgets.append(widget)
        if widget.w == '100%':
            self.cur_y += int(widget.h.strip('px').strip('%'))
        self.cur_x += int(widget.w.strip('px').strip('%'))
        
    
    def write_css(self, css_file):
        with open(css_file, 'w') as f:
        
        
        
            f.write(str(self.colour_theme))
        
    
class ScreenWidget(object):
    """
    A widget is a section (DIV) in the overall page
    """
    def __init__(self, nme, x, y, w, h):
        self.nme = nme.ljust(15)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        
    def __str__(self):
        res = 'Widget: ' + self.nme + ' is '
        res += 'x=' + str(self.x) + ','
        res += 'y=' + str(self.y) + ','
        res += 'w=' + str(self.w) + ','
        res += 'h=' + str(self.h) + '\n'
        
        return res
        

    
class ColourThemes(object):
    """
    sort of hard coded for now, but sets up default colour styles
    """
    def __init__(self, theme_name):
        if theme_name == 'plain':
            self.fg_colour = 'Black'
            self.bg_colour = 'White'
        elif theme_name == 'green_screen':
            self.fg_colour = 'Green'
            self.bg_colour = 'Black'
            
    def __str__(self):
        """
        outputs the colour theme as CSS content
        """
        
        res = '/* CSS Colour Theme */\n'
        res += 'body { \n'  	 
        res += '  background-color: ' + self.bg_colour + ';\n'
        res += '  font-color: ' + self.fg_colour + '; \n'
        res += '  color: ' + self.fg_colour + '; \n'
        res += '}\n'
        return res
                
        
if __name__ == '__main__':    
    define_screen('aikif_web1.yaml')
