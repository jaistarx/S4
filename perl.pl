#! /usr/bin/env perl
# perl1.pl

#JaisonJ

#question:Create a text file and answer the following queries :
#a) Search for the pattern ‘apple’ in the file and display the number of occurences.
#b) Count the number of words that ends with ‘e’
#c) Count the number of words that starts with ‘ap’
#d) Search for words containing ‘a’ or ‘s’
#e) Search for words containing zero or more occurrence of ‘e’
#f) Search for words containing one or more occurrence of ‘e’
#g) Search for words containing the letters ‘l’ and ‘m’, with any number of characters in between


use strict;
#use warnings;

open my $fh, '<', 'report.txt' or die "Cannot open file: $!\n";
my $i = 0;
my $e = 0;
my $ap = 0;
my $as = 0;
while(<$fh>) {
    my $line = $_;
	my @arr = split /\s+/, $line;  
	for my $word (@arr) {
	$i += () = $word =~ m\apple\gi; #no of apples
	$e += () = $word =~ m\e$\gi; #no of e
	$ap += () = $word =~ m\^ap\gi; #no of ap
	$as += () = $word =~ m\.*[as].*\gi; #no of a or s
	
	}
}
$as--;
print "\nNumber of occurences of apple : $i\n";
print "\nNumber of occurences of words ending with e : $e\n";
print "\nNumber of occurences of words starting with ap : $ap\n";

#occurences of words containing a or s
print "\noccurences of words containing a or s :\n";
open my $fh, '<', 'report.txt' or die "Cannot open file: $!\n";
while(<$fh>) {
    my $line = $_;
        my @arr = split /\s+/, $line;
        for my $word (@arr) {
	if ($word =~ m\.*[as].*\)
        {print "$&\n";}
        }

}

#ccurences of words containing zero or more e
open my $fh, '<', 'report.txt' or die "Cannot open file: $!\n";
print "\noccurences of words containing zero or more e :\n";
while(<$fh>) {
    my $line = $_;
        my @arr = split /\s+/, $line;
        for my $word (@arr) {
        if ($word =~ m\.*e?\)
        {print "$&\n";}
        }

}

#ccurences of words containing one or more e 
open my $fh, '<', 'report.txt' or die "Cannot open file: $!\n";
print "\noccurences of words containing one or more e :\n";
while(<$fh>) {
    my $line = $_;
        my @arr = split /\s+/, $line;
        for my $word (@arr) {
        if ($word =~ m\.*e\)
        {print "$&\n";}
        }

}

#occurences of words containing letters l and m, with any number of characters in between
open my $fh, '<', 'report.txt' or die "Cannot open file: $!\n";
print "\noccurences of words containing letters l and m, with any number of characters in between :\n";
while(<$fh>) {
    my $line = $_;
        my @arr = split /\s+/, $line;
        for my $word (@arr) {
        if ($word =~ m\.*l.*m.*\)
        {print "$&\n";}
        }

}

close(); #close the file
