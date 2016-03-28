#!/usr/bin/env python3

import os
import sys
import glob
import subprocess
import tempfile
import shutil


def main():

    path = sys.argv[1]

    test_files = []
    for infile in glob.glob(os.path.join(path, '*.in')):
        inname = os.path.splitext(os.path.basename(infile))[0]
        outfile = os.path.join(os.path.dirname(infile), inname + '.out')
        test_files.append((infile, outfile))

    program_sources = []
    program_types = ('*.py', '*.c', '*.cpp')
    for program_type in program_types:
        program_sources.extend(glob.glob(os.path.join(path, program_type)))
    program_source = program_sources[0]
    program_type = os.path.splitext(program_source)[1]
    command = []
    if program_type == '.py':
        command = ['python3', program_source]
    elif program_type == '.c':
        ofile = os.path.join(path, 'program')
        symfile = os.path.join(path, 'program.dSYM')
        cc_command = ['gcc', '-g', '-o', ofile, program_source]
        result = subprocess.run(cc_command)
        if result.returncode != 0:
            print(result.stdout)
            exit(1)
        command = [ofile]
    elif program_type == '.cpp':
        ofile = os.path.join(path, 'program')
        symfile = os.path.join(path, 'program.dSYM')
        cc_command = ['g++', '-g', '-o', ofile, program_source]
        result = subprocess.run(cc_command)
        if result.returncode != 0:
            print(result.stdout)
            exit(1)
        command = [ofile]

    for infile, outfile in test_files:
        print(os.path.basename(infile))
        result = subprocess.run(command, stdin=open(infile), stdout=subprocess.PIPE)
        if result.returncode != 0:
            print('CRASHED')
            print(result.stdout)
        else:
            expected_output = open(outfile, 'rb').read()
            if expected_output == result.stdout:
                print('SUCCESS')
            else:
                print('WRONG ANSWER')
                print('Got:')
                print(result.stdout)
                print('Expected:')
                print(expected_output)

    if program_type == '.py':
        pass
    elif program_type == '.c':
        ofile = os.path.join(path, 'program')
        symfile = os.path.join(path, 'program.dSYM')
        os.remove(ofile)
        shutil.rmtree(symfile)
    elif program_type == '.cpp':
        ofile = os.path.join(path, 'program')
        symfile = os.path.join(path, 'program.dSYM')
        os.remove(ofile)
        shutil.rmtree(symfile)


if __name__ == "__main__":
    main()
