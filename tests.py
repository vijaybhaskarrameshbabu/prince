#!/usr/bin/python
# -*- coding: utf-8 -*-

from prince import Prince
import os


def test(ptxt, key, exp):
    cipher = Prince()
    ctxt = cipher.encrypt(ptxt, key)
    if ctxt != exp:
        print "FAILED encryption of {} with key {}. Expected: {}, got: {}".format(ptxt.encode('hex'), key.encode('hex'), exp.encode('hex'), ctxt.encode('hex'))
    else:
        print "PASSED encryption of {} with key {}. Yields:   {}".format(ptxt.encode('hex'), key.encode('hex'), ctxt.encode('hex'))
    dec = cipher.decrypt(ctxt, key)
    if dec != ptxt:
        print "FAILED decryption of {} with key {}. Expected: {}, got: {}".format(ctxt.encode('hex'), key.encode('hex'), ptxt.encode('hex'), dec.encode('hex'))
    else:
        print "PASSED decryption of {} with key {}. Yields:   {}".format(ctxt.encode('hex'), key.encode('hex'), dec.encode('hex'))


if __name__ == "__main__":
    cipher = Prince()
    print "Running test1"
    test("\x00" * 8, "\x00" * 16, "818665aa0d02dfda".decode('hex'))
    
    print "\nRunning test2"
    test("\xff" * 8, "\x00" * 16, "604ae6ca03c20ada".decode('hex'))
    
    print "\nRunning test3"
    test("\x00" * 8, "\xff" * 8 + "\x00" * 8, "9fb51935fc3df524".decode('hex'))
    
    print "\nRunning test4"
    test("\0" * 8, "\x00" * 8 + "\xff" * 8, "78a54cbe737bb7ef".decode('hex'))

    print "\nRunning test5"
    test("0123456789abcdef".decode('hex'), "\x00" * 8 + "fedcba9876543210".decode('hex'), "ae25ad3ca8fa9ccf".decode('hex'))
