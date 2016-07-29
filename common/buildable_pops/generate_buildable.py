#!/usr/bin/env python

import sys
import yaml

print sys.argv
if len(sys.argv) != 3:
    print "Expected 2 argument, got: " + str(len(sys.argv)-1)
    raise Exception()

cfg_path = sys.argv[1]
template_path = sys.argv[2]

species_spec = {}
with open(cfg_path, 'r') as stream:
    try:
        species_spec = yaml.load(stream)
    except yaml.YAMLError as exc:
        raise exc

template = ""
with open(template_path, 'r') as stream:
    template = stream.read()

for species, portraits in species_spec.iteritems():
    print species, portraits
    with open(species + "_robot_pops.txt", 'w') as out:
        species_template = template.replace('$name', species)
        for portrait_name, portrait_spec in portraits.iteritems():
            suffix = portrait_spec.get('suffix', '')
            if 'min' in portrait_spec or 'max' in portrait_spec:
                min_n = portrait_spec.get('min', 1)
                max_n = portrait_spec.get('max', 1)
                for i in range(min_n, max_n+1):
                    out.write(species_template.replace('$portrait', portrait_name + str(i) + suffix))
