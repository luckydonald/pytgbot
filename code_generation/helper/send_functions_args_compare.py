from code_generator_online import load_api_definitions
from code_generator_classes import Function
from itertools import permutations

folder, html_document, results = load_api_definitions()

sendable = [f for f in results if isinstance(f, Function) and f.api_name.startswith('send')]

funcs = {s.name: set([v.name for v in s.variables]) for s in sendable}

print(funcs)

table = []

for colum_name in funcs.keys():
    table.append([colum_name, len(colum_name)])
# end for

TITLE_DATA=0
LENGTH_DATA=1

for i, func_args in enumerate(funcs.values()):
    for arg in func_args:
        table[i].append(arg)
        table[i][LENGTH_DATA] = max(table[i][LENGTH_DATA], len(arg))
    # end if
# end for

# order table, least arguments first

print(table)

table.sort(key=len)

print(table)

rows = []
title_row_string = ""
space_row_string = ""
for cols in table:
    title = cols[TITLE_DATA]
    length = cols[LENGTH_DATA]
    title_row_string += " {t:^{l}} |".format(t=title, l=length)
    space_row_string += " "+ ("-"*length) + " |"
# end for
rows.append(title_row_string)
rows.append(space_row_string)

max_rows = max(max(len(c) for c in table), 0)  # lenth of data (first 2 rows are title and border)

print("{i} rows".format(i=max_rows))

for i in range(2, max_rows + 2):  # (first 2 rows are title and border)
    row_string = ""
    for col in table:
        length = col[LENGTH_DATA]
        if len(col) > i:
            value = col[i]
            row_string += " {t:^{l}} |".format(t=value, l=length)
        else:  # we are out of content
            # produce empty row, to keep structure
            row_string += (" " * (length + 2)) + "|"
        # end if
    # end for
    rows.append(row_string)
# end for

table_string = "\n".join(rows)

print("TABLE:\n")
print(table_string)


from luckydonaldUtils.interactions import confirm
from luckydonaldUtils.encoding import to_binary as b

if confirm('save as file & open in browser?'):
    import tempfile
    import webbrowser
    from html import escape
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f:
        f.write(b("<pre>"))
        f.write(b(escape(table_string)))
        f.write(b("</pre>"))
        f.flush()
        print(f.name)
        webbrowser.open('file://'+f.name)
    # end with
# end if


possibilities = permutations(funcs.keys(), len(funcs))
#for order in possibilities:



"""   
 a | b | c | d
 - | - | - | -
 1 | 1 | 1 | 1
 2 | 2 |   | 2
 3 |   | 3 | 3
"""

"""   
 s | a | b | c | d |  s |
 - | - | - | - | - | -- |
   | 1 | 1 | 1 | 1 |    |
   | 2 | 2 |   | 2 |    |
   | 3 |   | 3 | 3 |    |
 - | - | - | - | - | -- |
 0 | 3 | 2 | 2 | 3 | 10 |
"""
"""   
 s | a | b | c | d |  s |
 - | - | - | - | - | -- |
 1 | x | x | x | x |    |
   | 2 | 2 |   | 2 |    |
   | 3 |   | 3 | 3 |    |
 - | - | - | - | - | -- |
 1 | 2 | 1 | 1 | 2 |  7 |
"""

"""   
 s | b | c | a | d |  s |
 - | - | - | - | - | -- |
 1 | x | x | x | x |    |
   | 2 |   | 2 | x |    |
   |   | 3 | 3 | x |    |
 - | - | - | - | - | -- |
 1 | 1 | 1 | 2 | 0 |  5 |
"""

"""   
 s | a | b | c | d |  s |
 - | - | - | - | - | -- |
   | 1 | 1 | 1 | 1 |    |
   | 2 | 2 |   | 2 |    |
   | 3 |   | 3 | 3 |    |
 - | - | - | - | - | -- |
 0 | 3 | 2 | 2 | 3 | 10 |
"""

