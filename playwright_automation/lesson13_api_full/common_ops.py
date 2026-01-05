import csv



class CommonOps:
    @staticmethod
    def generate_csv_from_list(headers:list,data:list,filename:str)->None:
        with open(filename,"w",newline="") as csv_file:
            csv_writer=csv.writer(csv_file)
            csv_writer.writerow(headers)
            csv_writer.writerows(data)


