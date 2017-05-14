"""
This is a cron file.
"""
import datetime
import dropbox
from app.models import Observatory, DataEntry, ImageDataEntry, Em, Instrument, Type


def split_str(str):
    arr = str.split('_')
    if arr[-1].endswith('.png') or arr[-1].endswith('.jpg') or arr[-1].endswith('.PNG') or arr[-1].endswith('.JPG'):
        arr[-1] = arr[-1][:-4]
    elif arr[-1].endswith('.jpeg'):
        arr[-1] = arr[-1][:-5]
    return arr


def make_url(url):
    if url.endswith('?dl=0'):
        url = url[:-5]
    return url.replace('www.dropbox', 'dl.dropboxusercontent')


def get_observatory(observatory):
    try:
        obs = Observatory.objects.get(key=observatory)
    except:
        obs = None
    return obs


def get_em(em):
    try:
        obs = Em.objects.get(key=em)
    except:
        obs = None
    return obs


def get_instrument(em):
    try:
        obs = Instrument.objects.get(key=em)
    except:
        obs = None
    return obs


def get_type(em):
    try:
        obs = Type.objects.get(key=em)
    except:
        obs = None
    return obs


def save_data_entry(title, movie, instrument, observatory, em, type, created_at):
    try:
        data_entry = DataEntry.objects.get(title=title, observatory=observatory)
    except:
        data_entry = DataEntry(title=title, movie=movie, instrument=instrument, observatory=observatory, em=em,
                               type=type, created_at=created_at)
        data_entry.save()
    return data_entry


def convert_date(strin):
    st_pattern = "%Y%m%d%H%M%S"
    return datetime.datetime.strptime(strin, st_pattern)


def save_image_entry(entry, url, arr):
    try:
        img = ImageDataEntry.objects.get(url=make_url(url), filename=entry.name)
    except ImageDataEntry.DoesNotExist:
        title = entry.name
        movie = url
        obs = get_observatory(arr[0])
        instrument = get_instrument(arr[1])
        em = get_em(arr[2])
        type = get_type(arr[3])
        created_at = convert_date(arr[4])
        data_entry = save_data_entry(title, movie, instrument, obs, em, type, created_at)
        img = ImageDataEntry(filename=entry.name, url=make_url(url), model=data_entry)
        img.save()
    return img


def schedule_job():
    dbx = dropbox.Dropbox('ngrUwh1dfAAAAAAAAAAAC8zBJhbb6ycu2hPNexGtMqHsmtSCK4GPlnwzLiVVEoJZ')
    for entry in dbx.files_list_folder('').entries:
        url = dbx.sharing_create_shared_link(entry.path_display).url
        arr = split_str(entry.name)
        img = save_image_entry(entry, url, arr)
