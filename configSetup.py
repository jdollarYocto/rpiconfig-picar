#!/usr/bin/env python3

import os
import sys
import glob
import yaml

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

print("Starting file generation")

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
config_file_path = dir_path / 'config.yml'

if not config_file_path.is_file():
    print("You must specify a config.yml with the appropriate values")
    sys.exit()

config_data = yaml.load(open(str(config_file_path.resolve())))

template_dir = dir_path / 'templates'
template_glob = sorted(template_dir.glob('**/*.j2'))
all_templates = list(map(lambda temp: str(temp.resolve().parent), template_glob))
env = Environment(loader = FileSystemLoader(all_templates))

for template_path in template_glob:
    # Determine the directory the finished file will go to and create it
    build_dir = Path('build/' + str(template_path.resolve().parent).split(str(template_dir.resolve()), 1)[1])
    if not build_dir.exists():
        build_dir.mkdir(parents=True)

    build_file = build_dir / template_path.stem
    template_file = env.get_template(template_path.name)
    build_file.open('w').write(template_file.render(config_data))

print("Finished generating files. See the build folder")
