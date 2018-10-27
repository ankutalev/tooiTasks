import json

current = 0
maxLength = 0
maxName = ""
counts = {}

with open('RomeoAndJuliet.json') as f:
    data = json.load(f)
for acts in data['acts']:
    for scenes in acts['scenes']:
        for actions in scenes['action']:

            if actions['character'] not in counts:
                counts[actions['character']] = 0
            current = 0
            for phrase in actions['says']:
                current += len(phrase)
            if current > maxLength:
                maxLength = current
                maxName = actions['character']
            counts[actions['character']] += 1

print(counts)
print("maximum replics: ", max(counts, key=counts.get))
print("the longest speech: ", maxName, maxLength)


config = {
    'cpp': {
        'g++': {
            'compile': '$\\MinGW32-gcc-8.1.0\\bin\\g++ % -Wl,--stack=536870912 -o solution.exe -w -static-libgcc -static-libstdc++',
            'run': 'solution.exe',
            'id' : 5
        },
        'cl': {
            'compile': '$\\vcc2015\\bin\\cl /Ox /I$\\vcc2015\\include /I$\\vcc2015\\ucrt\\x86  /EHsc /Fe: solution.exe % /link/LIBPATH:$\\vcc2015\\lib  /STACK:536870912',
            'run': 'solution.exe',
            'id':  0
        }

    },
    'python': {
        'python-2': {
            'compile': None,
            'run': '$\\python2.7\\python.exe %',
             'id' : 1
        },
        'python-3': {
            'compile': None,
            'run': '$\\python3.6\\python.exe %',
            'id' : 2
        },
    },
    'java': {
        'java-1.8-x64': {
            'compile': '$\\jdk1.8.0_121\\bin\\javac.exe Task.java',
            'run': '$\\jdk1.8.0_121\\bin\\java.exe -Xmx512m -Xss32m -Xms8m -Duser.language=en_US Task',
            'id': 3
        },
    },
}


with open('config.json', 'w') as outfile:
    json.dump(config, outfile)


