import configparser
import os
import subprocess
import shutil

config = configparser.ConfigParser()
config.read('config.ini')

accession_id = 170864

'''
# unarchiving
# use this when starting with 7z files
for root, _, files in os.walk(config['to-do']['path']):
    for name in files:

        print 'unarchiving ' + name

        cmd = [
            os.path.join('unarMac', 'unar'),
            '-force-overwrite',
            '-output-directory', config['doing']['path'],
            os.path.join(root, name)
        ]
        # subprocess.check_call(cmd)'''

'''
# use this when not starting with 7z files
for root, dirs, files in os.walk(os.path.join(config['to-do']['path'], str(accession_id)), topdown=True):
    depth = root[len(os.path.join(config['to-do']['path'], str(accession_id))) + len(os.path.sep):].count(os.path.sep)
    if depth == 8:

        print 'unarchiving ' + root

        shutil.move(os.path.join(root), os.path.join(config['doing']['path']))'''

# repackaging
for name in os.listdir(config['doing']['path']):

    print 'repackaging ' + name

    # objects
    os.mkdir(os.path.join(config['doing']['path'], name, 'objects'))
    for item in os.listdir(os.path.join(config['doing']['path'], name, 'data', 'objects')):

        if item in ['metadata', 'submissionDocumentation']:
            continue
        os.rename(
            os.path.join(config['doing']['path'], name, 'data', 'objects', item),
            os.path.join(config['doing']['path'], name, 'objects', item)
        )

    os.chdir(os.path.join(config['doing']['path'], name))
    cmd = [
        os.path.join(config['p7zip_16.02']['path'], 'bin', '7za'), 'a',
        '-bd',
        '-tzip',
        '-y',
        '-mtc=on',
        '-mmt=on',
        os.path.join('objects.zip'),
        os.path.join('objects')
    ]
    subprocess.check_call(cmd)

    os.chdir(os.path.join('..', '..'))
    shutil.rmtree(os.path.join(config['doing']['path'], name, 'objects'))

    # metadata
    os.chdir(config['doing']['path'])
    cmd = [
        os.path.join(config['p7zip_16.02']['path'], 'bin', '7za'), 'a',
        '-bd',
        '-tzip',
        '-y',
        '-mtc=on',
        '-mmt=on',
        '-x!' + os.path.join(name, 'objects.zip'),
        os.path.join(name, 'metadata.zip'),
        name
    ]
    subprocess.check_call(cmd)

    os.chdir(os.path.join('..'))
    for item in os.listdir(os.path.join(config['doing']['path'], name)):
        if item in ['obects.zip', 'metadata.zip']:
            continue

        elif item == 'data':
            shutil.rmtree(os.path.join(config['doing']['path'], name, item))

        elif item in ['bag-info.txt', 'bagit.txt', 'manifest-sha256.txt', 'tagmanifest-md5.txt']:
            os.remove(os.path.join(config['doing']['path'], name, item))

'''
# clean up
for name in os.listdir(config['to-do']['path']):
    shutil.rmtree(os.path.join(config['to-do']['path'], name))

# ready
for name in os.listdir(config['doing']['path']):
    shutil.move(os.path.join(config['doing']['path'], name), os.path.join(config['ready']['path']))'''
