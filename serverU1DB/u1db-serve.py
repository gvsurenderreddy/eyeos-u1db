__author__ = 'root'

import sys

from u1db import (
    __version__ as _u1db_version,
)
from u1db.commandline import (
    serve,
)


def main(args):
    import argparse
    p = argparse.ArgumentParser(usage='%(prog)s [options]',
                                description='Run the U1DB server')
    p.add_argument('--version', action='version', version=_u1db_version)
    p.add_argument('--verbose', action='store_true', help='be chatty')
    p.add_argument('--host', '-H', default='127.0.0.1', metavar='HOST',
                   help='Bind on this host when serving.')
    p.add_argument('--port', '-p', default=0, metavar='PORT', type=int,
                   help='Bind to this port when serving.')
    p.add_argument('--working-dir', default='.', metavar='WORKING_DIR',
                   help='Directory where the databases live.')

    args = p.parse_args(args)
    server = serve.make_server(args.host, args.port, args.working_dir)
    sys.stdout.write('listening on: %s:%s\n' % server.server_address)
    sys.stdout.flush()
    server.serve_forever()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
