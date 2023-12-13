import pandas as pd

class ExcelTest:
    def test11(self):
        input_file = r"C:\Users\ST AND AUTOLAB\excel\Students.xls"
        output_file = r"C:\Users\ST AND AUTOLAB\excel\Result.xls"

        df = pd.read_excel(input_file)
        df['Result'] = df.apply(lambda row: 'pass' if row[2] > 35 else 'fail', axis=1)
        df.to_excel(output_file, index=False)
        print("Records successfully updated")

if __name__ == "__main__":
    ExcelTest().test11()
