def render(table, params):
    number_of_rows = params['numberofrows']
    newtab = table.ix[number_of_rows:]
    return newtab
