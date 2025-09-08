from collections import ChainMap
import os, argparse

defaults = {
    'color' : 'red',
    'user' : 'admin'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
cmd_args = {k: v for k, v in vars(namespace).items() if v}
combined = ChainMap(cmd_args, os.environ, defaults)

print(f'{combined['color'] = }')
print(f'{combined['user'] = }')
