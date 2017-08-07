class Importable:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        number_of_rows = wf_module.get_param_number('numberofrows')
        newtab = table.ix[number_of_rows:]
        wf_module.set_ready(notify=False)
        return newtab