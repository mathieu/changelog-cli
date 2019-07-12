import os
import argparse
import subprocess
import datetime

unreleased_path='changelogs/unreleased'
changelog_filepath='CHANGELOG.md'

parser = argparse.ArgumentParser(prog='changelog', description='Changelog administration tool.')
parser.add_argument('-c', '--create',
                    metavar='message',
                    type=str,
                    help='creates an entry with this actual message to be added to the changelog')

parser.add_argument('-r', '--release',
                    metavar='version',
                    type=str,
                    help='releases the changelog by gathering all entries')

parser.add_argument('-f', '--filename',
                    type=str,
                    help='the filename to put the message in if you don\'t want to use the branch name')

parser.add_argument('-t', '--commit',
                    action='store_true',
                    help='the filename to put the message in if you don\'t want to use the branch name')


args = parser.parse_args()

if args.create == args.release:
    print('Need one of --create or --release option')
    parser.print_help()
    exit(1)

filename = args.filename
if filename == None:
    head = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    filename = head.split('/').pop().rstrip()

filename += '.md'

if args.create:
    if not os.path.isdir('changelogs/unreleased'):
        os.makedirs('changelogs/unreleased')
    
    changelog_entry_filepath = 'changelogs/unreleased/%s' % filename

    f = open(changelog_entry_filepath,'w')
    f.write(args.create)
    f.close()

    subprocess.check_output(['git', 'add', changelog_entry_filepath])

    if args.commit:
        subprocess.check_output(['git', 'commit', '-m', 'Created changelog entry', changelog_entry_filepath])

    print('Changelog entry added to \'%s\'' % changelog_entry_filepath)

if args.release:
    if not os.path.isdir('changelogs/unreleased'):
        os.makedirs('changelogs/unreleased')

    changelog = '## %s _%s_\n' % (args.release, datetime.datetime.today().strftime('%Y/%m/%d'))

    for root, dirs, files in os.walk('changelogs/unreleased'):
        for filename in files:
            f = open('changelogs/unreleased/%s' % filename,'r')
            changelog += '* %s\n' % f.read()
            f.close()

    changelog += '\n\n'

    f = open(changelog_filepath, 'r')
    changelog += f.read()
    f.close()
    f = open(changelog_filepath, 'w')
    f.write(changelog)
    f.close()
    subprocess.check_output(['git', 'add', changelog_filepath])

    for root, dirs, files in os.walk('changelogs/unreleased'):
        for filename in files:
            subprocess.check_output(['git', 'rm', '-f', 'changelogs/unreleased/%s' % filename])

    if args.commit:
        subprocess.check_output(['git', 'commit', '-m', 'Created release entry for %s' % args.release, changelog_filepath])
        
    print('Changelog entry for release \'%s\' added to changelog file \'%s\'' % (args.release, changelog_filepath))


