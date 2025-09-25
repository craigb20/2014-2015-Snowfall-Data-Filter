from snowfall_data_class import SnowfallDataEntry


def create_snowfall_label():
    """ creates the labels for the snowfall table """
    month_label = 'MONTH'
    day_label = 'DAY'
    amount_label = 'AMOUNT (in.)'
    print(f' ')
    print(f'{" ":<5}{month_label:<10}{day_label:<10}{amount_label:<10}')
    print(f'===========================================')


def create_snowfall_table(target_file):
    """ reads and prints the snowfall data from the text file """
    count = 1
    snowfall_data_list = []

    for line in target_file:
        """ skip empty lines and header line """
        if line.strip() == "" or line.lower().startswith("month"):
            continue

        snowfall_list = line.split()

        snowfall_obj = SnowfallDataEntry(*snowfall_list)

        if snowfall_obj.amount != '' and float(snowfall_obj.amount) > 5.0:
            print(f'{count:<5}{snowfall_obj.month:<10}{snowfall_obj.day:<10}{snowfall_obj.amount:<10}')
            snowfall_data_list.append(snowfall_obj)
            count += 1


def main():
    """ executes functions """
    try:
        target_file = open("snowfall_data.txt")
    except IOError:
        print("Error opening snowfall_data.txt")
        return
    create_snowfall_label()
    create_snowfall_table(target_file)
    target_file.close()


if __name__ == '__main__':
    main()
