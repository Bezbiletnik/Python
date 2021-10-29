import json
def func():
    list_1 = []
    with open('input.txt', 'r') as input_file:
        data = sorted(json.load(input_file), 
            key=lambda x: x['event_id'], reverse=True)
    for event in data:
        if event['status'] == 'OK' and event['event_id'] == len(data):
            result = event['count'] - event['return_count']
            print(result)
        else: print(list_1)

    # with open('output.txt', 'w') as output_file:
    #     json.dumps()
    
func()  