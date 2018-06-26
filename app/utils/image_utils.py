import datetime


def get_new_image_name(old_name):
    suffix_name='.'+old_name.split('.')[-1]
    new_name='IMG_{}'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    return new_name+suffix_name

