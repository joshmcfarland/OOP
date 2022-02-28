class Procedure:
    def __init__(self, proc_name, date, pract_name, charges, id):
        self.__proc_name = proc_name
        self.__date = date
        self.__pract_name = pract_name
        self.__charges = charges
        self.__cid = id

    def get_proc_name(self):
        return self.__proc_name

    def get_date(self):
        return self.__date

    def get_pract_name(self):
        return self.__pract_name

    def get_charges(self):
        return self.__charges

    def get_id(self):
        return self.__cid
