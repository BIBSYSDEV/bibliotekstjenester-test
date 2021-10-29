#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import csv


table_name = "contents"
csv_file_path = "contents.csv"
output_file_name = "prepped.json"
MAX_AWS_WRITE_BATCH_ITEMS = 25


def make_json(csv_file, tb_name):
    data = {tb_name: []}
    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        processed = []
        for row in csv_reader:
            for key, value in row.items():
                row[key] = {"S": value}
            processed.append({'PutRequest': {'Item': row}})
        data[tb_name] = processed
    return data


def prep_json(json_data_from_csv, tb_name, op_file_name):
    json_array = json_data_from_csv[tb_name]
    json_array = json_array[:MAX_AWS_WRITE_BATCH_ITEMS]  # write batch can only handle up to 25 writes per batch job
    json_data_from_csv[tb_name] = json_array
    json_file_output = open(op_file_name, 'w')
    json_file_output.write(json.dumps(json_data_from_csv))
    json_file_output.close()


json_data = make_json(csv_file_path, table_name)
prep_json(json_data, table_name, output_file_name)
