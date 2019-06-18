import sys
from collections import namedtuple
from database.models import Torrent, current_db, initialize_db

from application_logger import get_logger

main_logger = get_logger('main', term_log=True)

DelugeParameters = namedtuple('DelugeParameters', ['torrent_id', 'torrent_name', 'save_path'])
db = current_db()
if len(sys.argv) < 4:
    main_logger.error('Invalid parameters [%s]', sys.argv)
    sys.exit(1)

parameters = DelugeParameters(torrent_id=sys.argv[1], torrent_name=sys.argv[2], save_path=sys.argv[3])


def start_extract():
    main_logger.info('Starting complex extractor')

    db.connect()
    initialize_db()

    torrent = Torrent()
    torrent.deluge_id = parameters.torrent_id
    torrent.name = parameters.torrent_name
    torrent.save_path = parameters.save_path
    torrent.save()


if __name__ == '__main__':
    start_extract()
