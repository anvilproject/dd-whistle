#!/usr/bin/env python

"""Extract the data-dictionary from the composite document, CMG 16July2020 to FHIR

This just identifies which table (instrument) variables go into and generates 
appropriate DD csv files for consumption by NCPI Whistler. 
"""

import csv
from pathlib import Path

ignored_values = set([
    "N/A",
    "Values collected thus far:",
    "UBERON concepts such as:"
])

class Variable:
    def __init__(self, table_name, row):
        self.table_name = table_name

        self.varname = row['Field']
        self.description = row['Data element description']
        self.field_type = row['Field type']
        
        self._enums = {}
        enums = row['Enumerations']

        # For this one, we don't have any underlying codes to worry about, 
        # so the enumerations are just individual entries separated by a 
        # semi-colon
        if enums not in ignored_values:
            for value in enums.split("\n"):
                if value not in ignored_values:
                    if " - " in value:
                        desc,code = [x.strip() for x in value.split(" - ")]
                        assert("=" not in code)
                        assert("=" not in desc)
                        self._enums[code] = code
                    else:
                        self._enums[value] = value

    def write_header(self, writer):
        """Write header for the CSV DD"""
        writer.writerow([
            'variable_name',
            'description',
            'variable_type',
            'enumerated_values'
        ])

    def write(self, writer):
        """Write local variable to the dd file"""
        writer.writerow([
            self.varname,
            self.description,
            self.field_type,
            self.enum
        ])

    @property
    def enum(self):
        "Transform the dictionary into the semi-colon separated values"
        return ";".join(self._enums.values())

def clean_fieldname(value):
    "Just in case there are any spaces in 'Instrument' name" 
    return value.replace(" ", "_").lower()

class Instrument:
    """Basically a table that has a name and some number of variables. 
    
    Variables are ordered according to the order they are encountered. 
    """
    def __init__(self, name):
        self.instrument_name = clean_fieldname(name)
        self.variables = []

    def add_row(self, row):
        """Add a variable from the CSV row at hand"""
        variable = Variable(self.instrument_name, row)
        self.variables.append(variable)

    def to_file(self, destination):
        "Write the 'table' to a file named after the table name"
        filename = destination / f"{self.instrument_name}.csv"
        print(filename)
        with open(filename, 'wt') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"')
            self.variables[0].write_header(writer)
            for var in self.variables:
                var.write(writer)

def parse_file(filename="data/cmg/original/cmg_07162020.csv", outdir="data/cmg/dd/"):
    tables = {}

    destination = Path(outdir)
    destination.mkdir(parents=True, exist_ok=True)

    with open(filename, 'rt') as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')

        # Walk over each row and append the variables to each "instrument" 
        # listed in the instrument column. 
        for line in reader:
            instruments = [x.strip() for x in line['Instrument'].split(",")]

            for instrument in instruments:
                if instrument not in tables:
                    tables[instrument] = Instrument(instrument)
    
                tables[instrument].add_row(line)
    
    # Write the data to the appropriate files
    for table in list(tables.values()):
        table.to_file(destination)

if __name__ == '__main__':
    parse_file()
    
