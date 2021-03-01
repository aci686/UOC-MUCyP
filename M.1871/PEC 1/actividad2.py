#! /usr/bin/env python3

'''
Accepts a Youtube watch-history json file and plots an histogram with the number of videos/hour watched
Considers the whole file
'''

__author__ = 'Aaron Castro'
__author_email__ = 'aaron.castro.sanchez@outlook.com'
__copyright__ = 'Aaron Castro'
__license__ = 'MIT'

import json, argparse
import matplotlib.pyplot as plt
from datetime import datetime

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to json history file', required=True)
    args = parser.parse_args()

    return(args)

def extract_hours(json_file): # Devuelve una lista con todos los registros de hora del historial
    hour_list = []

    file = open(json_file)
    data = json.load(file)
    for _ in data:
        hour_list.append(datetime.strptime(_['time'][:19], '%Y-%m-%dT%H:%M:%S').hour)

    return(hour_list)

def main():
    args = get_arguments()

    if args.input:
        plt.hist(extract_hours(args.input), 24)
        plt.xlabel('Hora')
        plt.ylabel('# Vídeos')
        plt.title('Distribución')
        plt.show()

if __name__ == '__main__':
    main()
