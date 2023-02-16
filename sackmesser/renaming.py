from pathlib import Path
from rich import print
def rename_trimbits(path, name_lookup, dry_run = True):
    """Rename EIGER trimbit files for beb replacement"""
    path = Path(path)
    if dry_run == True:
        print('[yellow]Dry run, no files will be renamed![/yellow]')
    else:
        print('[green]Renaming trimbit files[/green]')
    for child in path.glob('**/*'):
        for key, value in name_lookup.items():
            if child.name == f'noise.sn{key:03}':
                print(child)
                new_name = child.with_suffix(f'.sn{value:03}')
                print('-->', new_name)
                if not dry_run:
                    child.rename(new_name)