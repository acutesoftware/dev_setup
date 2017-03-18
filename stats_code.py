# stats_code.py

import collections
import os
import ast
import time


code_folders = ['AIKIF\\aikif', 
                'rawdata\\rawdata', 
                'virtual-AI-simulator\\vais', 
                'worldbuild\\worldbuild', 
                'web_aikif.com']
                
#code_folders = ['web_aikif.com']

def main():
    base_fldr = 'T:\\user\\dev\\src\\python\\'
    opfile = 'code_stats.md'
    start_time = time.time()
    res = []
    res.append('## Code stats')
    res.append('###### updated ' + today_as_string() + '\n')
    res.append('Project | Stat Name | Value')
    res.append('--- | --- | ---')
    
    for fldr in code_folders:
        stats = analyze(base_fldr + fldr)
        for k,v in stats.items():
            res.append(fldr + '|' + str(k) + '|' + str(v))
    
    end_time = time.time()
    res.append('\n\nTime to run : ' +  str(end_time - start_time) + ' seconds\n')
    
    with open(opfile, 'w') as f:
        f.write('\n'.join(line for line in res))

def today_as_string():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def analyze(packagedir):
    stats = collections.defaultdict(int)
    for (dirpath, dirnames, filenames) in os.walk(packagedir):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue

            filename = os.path.join(dirpath, filename)

            syntax_tree = ast.parse(open(filename, encoding="utf8").read(), filename)
            for node in ast.walk(syntax_tree):
                stats[type(node)] += 1


    return stats

#print(analyze('.')[ast.FunctionDef])  # prints num
#print(analyze('.'))

#print(analyze('T:\\user\\dev\\src\\python\\AIKIF\\aikif')[ast.FunctionDef])
#print(analyze('T:\\user\\dev\\src\\python\\AIKIF\\aikif'))


main()