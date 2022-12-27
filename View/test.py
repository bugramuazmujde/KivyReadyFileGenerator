from pathlib import Path
import getpass

def get_lst_writable_linux_disks():
    this_user = getpass.getuser()

    lst_available_linux_disks = [str(Path.home())]
    with open('/proc/mounts', 'r') as f:
        data = f.readlines()

    for line in data:
        item = line.split(' ')
        mount_point = item[1]
        fs_type = item[2]
        options = item[3]
        if mount_point.startswith('/mnt') or (mount_point.startswith(f'/media/{this_user}') and fs_type != 'vfat' and 'rw' in options):
            lst_available_linux_disks.append(mount_point)

    return lst_available_linux_disks

print(get_lst_writable_linux_disks())

