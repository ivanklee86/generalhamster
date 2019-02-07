
def compare_categories(v1_category: dict, v2_category: list) -> dict:
    attachmend_dict = {
        'title': f"V1/V2 Diff Report for {v1_category['name']} ({v1_category['id']})",
        'color': 'danger',
        'fields': []
    }

    v1_classes = v1_category['children']
    v1_length = len(v1_classes)
    v2_length = len(v2_category)

    diff_length = abs(v1_length - v2_length)
    diff_percentage = ((max(v1_length, v2_length) - min(v1_length, v2_length)) / max(v1_length, v2_length)) * 100

    v1_workout_ids = [x['cls']['id'] for x in v1_category['children']]
    v2_workout_ids = [x['id'] for x in v2_category]

    v1_but_not_v2 = set(v1_workout_ids) - set(v2_workout_ids)
    v2_but_not_v1 = set(v2_workout_ids) - set(v1_workout_ids)

    if diff_length:
        attachmend_dict['fields'].append({
            'title': '# of different classes',
            'value': diff_length,
            'short': True
        })

        attachmend_dict['fields'].append({
            'title': '# of different classes',
            'value': f'{diff_percentage*100:.2f}%',
            'short': True
        })

    if v1_but_not_v2:
        attachmend_dict['fields'].append({
            'title': 'Classes in v1 but not v2',
            'value': "\n".join(v1_but_not_v2),
            'short': False
        })

    if v2_but_not_v1:
        attachmend_dict['fields'].append({
            'title': 'Classes in v2 but not v1',
            'value': "\n".join(v2_but_not_v1),
            'short': False
        })

    if attachmend_dict['fields']:
        return attachmend_dict
    else:
        return {}


