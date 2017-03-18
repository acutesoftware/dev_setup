# stats_code.py

import collections
import os
import ast
import time

base_fldr = 'T:\\user\\dev\\src\\python\\'
opfile = 'code_stats.md'

code_folders = ['AIKIF\\aikif', 
                'rawdata\\rawdata', 
                'virtual-AI-simulator\\vais', 
                'worldbuild\\worldbuild', 
                'web_aikif.com']
                
#code_folders = ['web_aikif.com']

def main():
    
    start_time = time.time()
    sum = []
    sum.append('## Code stats')
    sum.append('###### updated ' + today_as_string() + '\n')
    sum.append('Project | Files | Lines | Comments | Size')
    sum.append('--- | --- | --- | --- | ---')
    res = []
    res.append('Project | Stat Name | Value')
    res.append('--- | --- | ---')
    
    for fldr in code_folders:
        stats, fs = analyze(base_fldr + fldr)
        sum.append(format_sum(fs))
        print(fs)
 
        for k,v in stats.items():
            res.append(fldr + '|' + str(k) + '|' + str(v))
    
    end_time = time.time()
    res.append('\n\nTime to run : ' +  str(end_time - start_time) + ' seconds\n')
    
    with open(opfile, 'w') as f:
        f.write('\n'.join(line for line in sum))
        f.write('\n\n### AST Stats\n')
        f.write('\n'.join(line for line in res))

def format_sum(fs):
    txt = ''
    txt += fs['name'][len(base_fldr):] + '|'
    txt += str(fs['num_files']) + '|'
    txt += str(fs['num_lines']) + '|'
    txt += str(fs['comment_lines']) + '|'
    txt += str(fs['sze'])
    return txt    
        
def file_stats(fname):
    sze = 0
    comment_lines = 0
    num_lines = 0
    with open(fname) as f:
        for num_lines, line in enumerate(f):
            sze += len(line)
            if line.strip(' ')[0:1] == '#':
                comment_lines += 1
    return num_lines + 1 , comment_lines, sze       
        
def today_as_string():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def analyze(packagedir):
    stats = collections.defaultdict(int)
    file_sum = collections.defaultdict(int)
    file_sum['name'] = packagedir
    for (dirpath, dirnames, filenames) in os.walk(packagedir):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue

            filename = os.path.join(dirpath, filename)
            num_lines, comment_lines, sze = file_stats(filename)
            
            file_sum['num_files'] += 1
            file_sum['num_lines'] += num_lines
            file_sum['comment_lines'] += comment_lines
            file_sum['sze'] += sze
            
            syntax_tree = ast.parse(open(filename, encoding="utf8").read(), filename)
            for node in ast.walk(syntax_tree):
                stats[type(node)] += 1


    return stats, file_sum

#print(analyze('.')[ast.FunctionDef])  # prints num
#print(analyze('.'))

#print(analyze('T:\\user\\dev\\src\\python\\AIKIF\\aikif')[ast.FunctionDef])
#print(analyze('T:\\user\\dev\\src\\python\\AIKIF\\aikif'))


main()