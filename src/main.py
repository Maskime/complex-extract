import sys
from collections import namedtuple

from src.application_logger import get_logger

main_logger = get_logger('main', term_log=True)

DelugeParameters = namedtuple('DelugeParameters', ['torrent_id', 'torrent_name', 'save_path'])

if len(sys.argv) < 4:
    main_logger.error('Invalid parameters [%s]', sys.argv)
    sys.exit(1)

parameters = DelugeParameters(torrent_id=sys.argv[1], torrent_name=sys.argv[2], save_path=sys.argv[3])

def start_extract():
    main_logger.info('Starting complex extractor')


if __name__ == '__main__':
    start_extract()
