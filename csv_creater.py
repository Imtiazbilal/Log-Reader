import pandas as pd
import xlsxwriter


class CSV:

    def __init__(self, output_text, output_csv):
        self.output_csv = output_csv
        self.output_text = output_text

    def conversion_MGO(self):
        df = pd.read_csv(filepath_or_buffer=self.output_text, header=None)
        df.style.set_properties(
            {'background-color': 'green', 'color': 'black', 'border-color': 'black', 'border-width': 'Ipx',
             'boarder-style': 'solid'})
        df.columns = ['Month', 'Date', 'Time', 'loglevel', 'Location', 'Description']
        # df.to_csv(path_or_buf=self.output_csv)
        with pd.ExcelWriter(path=self.output_csv) as writer:
            df.to_excel(writer, sheet_name="oMGW")

    def conversion_cloud(self):
        df = pd.read_csv(filepath_or_buffer=self.output_text, header=None)
        df.style.set_properties(
            {'background-color': 'green', 'color': 'black', 'border-color': 'black', 'border-width': 'Ipx',
             'boarder-style': 'solid'})
        df.columns = ['Date', 'Time', 'loglevel', 'Location', 'Request Id', 'Description']
        # df.to_csv(path_or_buf=self.output_csv)
        with pd.ExcelWriter(path=self.output_csv) as writer:
            df.to_excel(writer, sheet_name="cloud")

    def conversion_OBSFAILA(self):
        df = pd.read_csv(filepath_or_buffer=self.output_text, header=None)
        # df.style.set_properties(
        #     {'background-color': 'green', 'color': 'black', 'border-color': 'black', 'border-width': 'Ipx',
        #      'boarder-style': 'solid'})
        df.columns = ['Report Number', 'Call Id', 'Call Start', 'Clear Code', 'Clear Info', 'Clear Part', 'Signaling',
                      'Calling Number', 'Called Number', 'IMSI-A', 'IMSI-B', 'CGR/BSC/PCM-TSL-A', 'CGR/BSC/PCM-TSL-B',
                      'LAC/CI/CELL BAND-A', 'LAC/CI/CELL BAND-B']
        # df.to_csv(path_or_buf=self.output_csv)
        with pd.ExcelWriter(path=self.output_csv) as writer:
            df.to_excel(writer, sheet_name="OBSFAILA", startrow=0, startcol=0, index=True, header=True,
                        index_label="No.")
