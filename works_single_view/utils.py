from works_single_view.models import Work, Contributor


def parse_works(in_data):
    """
    Will parse received work data into a list of model-like dicts
    :param in_data: string representing all uploaded data
    :return:
    """
    if not isinstance(in_data, str):
        raise TypeError(f"Received unexpected data of type {type(in_data)}")

    rows = in_data.strip().split('\n')[1:]
    works_list = list(map(map_works, rows))
    return works_list


def map_works(raw_data):
    """
    Will map parsed work data to a dictionary
    :param raw_data: single string representing Work
    :return:
    """
    fields = raw_data.split(',')
    work = {'title': fields[0],
            'contributors': fields[1],
            'iswc': fields[2]}
    return work


def save_works(works):
    """
    Will handle Work and Contributor saving process.
    This method creates both models, also updates
    Work with missing data.
    :param works: list of Work-like dicts
    :return:
    """
    for work_data in works:
        new_work = Work.create(iswc=work_data['iswc'],
                               title=work_data['title'])
        if not new_work.id:
            new_work.save()
        else:
            if new_work.iswc == '':
                new_work.iswc = work_data['iswc']

        contrib_names = work_data['contributors'].split('|')
        for name in contrib_names:
            c_obj, _ = Contributor.objects.get_or_create(name=name)
            new_work.contributors.add(c_obj)

        new_work.save()

