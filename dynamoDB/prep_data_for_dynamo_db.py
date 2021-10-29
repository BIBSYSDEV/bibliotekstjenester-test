import json
import csv

table_name = "contents"
csv_file_path = "contents.csv"
output_file_name = "prepped.json"
delete_items_file_name = "delete_items.json"
primary_key_name = "isbn"
MAX_AWS_WRITE_BATCH_ITEMS = 25
REPLACEMENT_ISBN_FOR_FILES = "1235467890123"


def read_csv(csv_file, tb_name, p_key):
    put_request_data = {tb_name: []}
    p_key_list = []
    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        processed = []
        for row in csv_reader:
            for key, value in row.items():
                row[key] = {"S": value}
                if key == p_key:
                    p_key_list.append(value)
            processed.append({'PutRequest': {'Item': row}})
        put_request_data[tb_name] = processed
    return put_request_data, p_key_list


def write_json(json_data, tb_name, op_file_name):
    json_array = json_data[tb_name]
    json_array = json_array[:MAX_AWS_WRITE_BATCH_ITEMS]  # write batch can only handle up to 25 writes per batch job
    json_data[tb_name] = json_array
    json_file_output = open(op_file_name, 'w')
    json_file_output.write(json.dumps(json_data))
    json_file_output.close()


def create_delete_items_json(list_of_primary_keys, t_name, p_name):
    delete_requests = []
    for value in list_of_primary_keys:
        delete_requests.append({"DeleteRequest": {"Key": {p_name: {"S": value}}}})
    return {t_name: delete_requests}


# replaces some file paths with a give mock path
def replace_files_path_to_mock_pack(put_request_data, mock_isbn, t_name):
    put_requests = put_request_data[t_name]
    for put_request in put_requests:
        item = put_request['PutRequest']['Item']
        if item.get('audio_file') and len(item['audio_file']['S']) > 0:
            item['audio_file']['S'] = "files/audio/mp3/" + mock_isbn + ".mp3"
        if len(item['image_small']['S']) > 0:
            item['image_small']['S'] = "files/images/small/" + mock_isbn + ".jpg"
        if len(item['image_original']['S']) > 0:
            item['image_original']['S'] = "files/images/original/" + mock_isbn + ".jpg"
        if len(item['image_large']['S']) > 0:
            item['image_large']['S'] = "files/images/large/" + mock_isbn + ".jpg"
    return {t_name: put_requests}


json_put_request_data, list_of_items_to_be_deleted = read_csv(csv_file_path, table_name, primary_key_name)
json_delete_request_data = create_delete_items_json(list_of_items_to_be_deleted, table_name, primary_key_name)
json_put_request_data = replace_files_path_to_mock_pack(json_put_request_data, REPLACEMENT_ISBN_FOR_FILES, table_name)
write_json(json_delete_request_data, table_name, delete_items_file_name)
write_json(json_put_request_data, table_name, output_file_name)
