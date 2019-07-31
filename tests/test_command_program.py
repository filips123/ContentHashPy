from unittest.mock import patch
import sys
import io

from content_hash.__main__ import main


CODEC = 'zeronet'
DECODED = '1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D'
ENCODED = 'e6013148654c4c6f34757a6a614c65744678364e4833504d774650337162526254663344'


def test_command_program_get_codec():
    argv = ['content-hash', 'get-codec', ENCODED]
    stdout = io.StringIO()

    with patch.object(sys, 'argv', argv), patch('sys.stdout', stdout):
        main()

    assert stdout.getvalue().split('\n')[0] == CODEC


def test_command_program_decode():
    argv = ['content-hash', 'decode', ENCODED]
    stdout = io.StringIO()

    with patch.object(sys, 'argv', argv), patch('sys.stdout', stdout):
        main()

    assert stdout.getvalue().split('\n')[0] == DECODED


def test_command_program_encode():
    argv = ['content-hash', 'encode', CODEC, DECODED]
    stdout = io.StringIO()

    with patch.object(sys, 'argv', argv), patch('sys.stdout', stdout):
        main()

    assert stdout.getvalue().split('\n')[0] == ENCODED
