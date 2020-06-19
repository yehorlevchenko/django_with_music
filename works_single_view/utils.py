from works_single_view.models import Work, Contributor


def parse_works(in_data):
    if not isinstance(in_data, str):
        raise TypeError(f"Received unexpected data of type {type(in_data)}")

    works_list = list()
    rows = in_data.strip().split('\n')[1:]
    for row in rows:
        fields = row.split(',')
        work = {'title': fields[0],
                'contributors': fields[1],
                'iswc': fields[2]}
        works_list.append(work)
    return works_list

def parse_contributors(in_data):
    if not isinstance(in_data, str):
        raise TypeError(f"Received unexpected data of type {type(in_data)}")

    contributors_names = list()
    rows = in_data.strip().split('\n')[1:]
    for row in rows:
        fields = row.split(',')
        names_list = fields[1].split('|')
        contributors_names.extend(names_list)
    contributors_names = list(set(contributors_names))

    return [{'name': name} for name in contributors_names]

def save_works_from_csv(works):
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

