from spyre import server

import pandas as pd
import csv
import datetime
import shutil

class CsvUpdateApp(server.App):
    title = "CSV update"

    inputs = [{
        "type": 'text',
        "label": 'file name (under ./data/ directory)',
        "value": 'test_data.csv',
        "key": 'file',
        "action_id": "get_data"
    },{
        "type": 'text',
        "label": 'data1',
        "value": '',
        "key": 'data1',
        "action_id": "add_data"
    },{
        "type": 'text',
        "label": 'data2',
        "value": '',
        "key": 'data2',
        "action_id": "add_data"
    },{
        "type": 'text',
        "label": 'data3',
        "value": '',
        "key": 'data3',
        "action_id": "add_data"
    },{
        "type": 'text',
        "label": 'data4',
        "value": '',
        "key": 'data4',
        "action_id": "add_data"
    },{
        "type": 'text',
        "label": 'data5',
        "value": '',
        "key": 'data5',
        "action_id": "add_data"
    }]

    controls = [{
        "type": "button",
        "label": "get data from file path",
        "id": "get_data"
    },{
        "type": "button",
        "label": "add data",
        "id": "add_data"
    }]

    tabs = ["GetTable", "RecentlyAddedTable"]

    outputs = [{
        "type": "table",
        "id": "table_id1",
        "control_id": "get_data",
        "tab": "GetTable",
        "on_page_load": True
    },{
        "type": "html",
        "id": "html_id2",
        "control_id": "add_data",
        "tab": "AddTable",
        "on_page_load": True
    }]


    def getData(self, params):
        filepath = params['file']
        df = pd.read_csv('data/' + filepath)
        return df

    def getHTML(self, params):
        filepath = params['file']
        filepath = 'data/' + filepath

        data1 = params['data1']
        data2 = params['data2']
        data3 = params['data3']
        data4 = params['data4']
        data5 = params['data5']
        new_data = [data1, data2, data3, data4, data5]

        if data1 != "" and data2 != "" and data3 != "" and data4 != "" and data5 != "":

            # backup
            now = datetime.datetime.now()
            now = datetime.datetime.strftime(now, '%Y%m%d%H%M%S')
            shutil.copy(filepath, filepath + '_' + now)

            # update data
            with open (filepath, 'a') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(new_data)
            return "added line [%s,%s,%s,%s,%s]" % (data1,data2,data3,data4,data5)


if __name__ == '__main__':
    app = CsvUpdateApp()
    app.launch(port=9093)
