#!/usr/bin/perl -w
use strict;
use Data::Dumper;
die "usage: perl $0 <blast results|outfmt 0> <identy|float> <extend length> <out>\n" unless @ARGV == 4;
=pod
blastn -task blastn -query $query -db $db -outfmt 0 -num_threads 4 -max_hsps 1 -num_descriptions 1 -num_alignments 1 -out $out
=cut
open (IN, "$ARGV[0]") or die "blast results missing!\n";
open (OUT, ">$ARGV[3]") or die "permission denied!\n";
my ($query, $target_name, $identy, $coverage, $strand);
my $alignindex = -1;
my $flag = 0;
my $focus_index = 0;
while (<IN>){
	chomp;
	if (/^Database:/) {print STDERR "$_\n";}
	if (/^Query= (\S+)/) { #block start
		$query = $1; #($chr, $start, $end) = split/:|-/, $1; #fasta cut using bedtools ( ]
		$flag = 0;
		$alignindex = -1;
		$focus_index = 0;
	}
	if (/^>/) {$target_name = (split/>/, $_)[1];}
	if (/Identities = (\d+)\/(\d+)/) {
		$identy = $2 > 0 ? $1/$2 : 0;
	}
	if (/Strand/) {
		if ($_ =~ /Plus\/Minus/){
			$strand = "-";
		}
		elsif ($_ =~ /Plus\/Plus/){
			$strand = "+";
		}
		else{
			die "$_ not possible, please check!\n"; 
		}
	}
	if ($_ =~ /^Query/ and $_ !~ /^Query=/ and $identy >= $ARGV[1]){#identy
		my @query_alignment = split/\s+/, $_;
		my @query = split//, $query_alignment[2];
		next if ($query_alignment[1] > $ARGV[2]+1 or $query_alignment[3] < $ARGV[2]+1); ###block containing the site
        $flag = 1; #record the interested segment
		my $focus_sites = 0;
		foreach my $base (@query){
			$alignindex++;
			$focus_sites = $query_alignment[1]++ unless ($base =~ /-/); #blast results are 1 based
			if ($focus_sites == $ARGV[2]+1){
					print OUT $query,"\t",$focus_sites,"\t",$base,"\t";
					$focus_index = $alignindex; #0 based
			}
            last if ($focus_sites == $ARGV[2]+1);
		}
	}
	if ($_ =~ /^Sbjct/ and $flag == 1){
		my @target_alignment = split/\s+/, $_;
		my $target_start = $target_alignment[1];
		my $target_allele = substr ($target_alignment[2], $focus_index, 1);
		my @target = split//, $target_alignment[2];
		my $tmp_index = -1;
        my $target_shift = -1;
		foreach my $base (@target){
			$tmp_index++;
            $target_shift++ unless ($base =~ /-/); # first assign the value to the variable
			if ($strand eq "+"){
                print OUT $target_name,"\t",$target_start+$target_shift,"\t",$target_allele,"\t",$strand,"\n" if $tmp_index == $focus_index;
			}
			elsif ($strand eq "-"){
                print OUT $target_name,"\t",$target_start-$target_shift,"\t",$target_allele,"\t",$strand,"\n" if $tmp_index == $focus_index;
			}
		}
		$flag = 0;
	}
}
close IN;
