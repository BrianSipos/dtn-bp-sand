#!/usr/bin/env python3
''' Split artwork from an RFC XML file and feed them to a command.
'''
import os
import sys
import logging
import argparse
import subprocess
import lxml.etree as etree

LOGGER = logging.getLogger()


def main():
    ''' Main entry for the tool. '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', default='info',
                        help='The minimum logging severity displayed.')
    parser.add_argument('--lines', default=False, action='store_true',
                        help='Replace all newlines with whitespace and send to one command process as separate lines.')
    parser.add_argument('infile', help='The file to read from.')
    parser.add_argument('xpath', help='The XPath expression to match.')
    parser.add_argument('command', nargs=argparse.REMAINDER,
                        help='The command and its arguments to run and pass to stdin.')

    args = parser.parse_args()
    logging.basicConfig(
        level=args.log_level.upper(),
        stream=sys.stderr
    )
    logging.root.debug('command args: %s', args)

    with open(args.infile, 'rb') as infile:
        xml_parser = etree.XMLParser()
        doc = etree.parse(infile, xml_parser)

    parts = []
    if args.lines:
        parts.append('')
    for elem in doc.xpath(args.xpath):
        text = elem.text.strip()
        if args.lines:
            text = text.replace('\r', ' ')
            text = text.replace('\n', ' ')
            parts[0] += text + '\n'
        else:
            parts.append(text)

    exitcodes = []
    for part in parts:
        LOGGER.debug('Processing part text:\n%s', text)
        proc = subprocess.Popen(args.command, stdin=subprocess.PIPE)
        proc.communicate(part.encode('utf8'))
        proc.stdin.close()
        exitcodes.append(proc.wait())

    return max(exitcodes) if exitcodes else 0


if __name__ == '__main__':
    sys.exit(main())
