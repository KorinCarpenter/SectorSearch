#!/usr/bin/perl

use strict;
use warnings;
use Text::Balanced qw/extract_multiple extract_bracketed/;

my $file;
open my $fileHandle, '<', $ARGV[0];

{ 
  local $/ = undef; # or use File::Slurp
  $file = <$fileHandle>;
}

close $fileHandle;

my @array = extract_multiple(
                               $file,
                               [ sub{extract_bracketed($_[0], '{}')},],
                               undef,
                               1
                            );

print $_,"\n" foreach @array;
