#!/usr/bin/perl

## Program Name: bglr_encode.pl
## Arguments:   <format type>- possible values: dominant,iupac
## 		<genotype_file>- genotype matrix to encode
## 		<coding_scheme>- codes for alleles (e.g (0,2) translates to minor homozygous, major homozygous respectively)
## 		<output>- standard output
##
## Date: June 22, 2017
## Author: Victor Jun Ulat (v.ulat@cgiar.org)
## Author: Venice Juanillas (v.juanillas@irri.org)


use strict;
use warnings;


## Usage:bglr_encode.pl <format_type> <genotype_file> <coding_scheme> <output>

if(!@ARGV || @ARGV!=4){
	print "Usage: bglr_encode.pl <format_type> <genotype_file> <coding_scheme> <output>\n";
	print "Example: bglr_encode.pl dominant GENOTYPE.csv 0,2 GENOTYPE_ENOCDED.csv\n";
	print "Example: bglr_encode.pl iupac GENOTYPE.csv 0,1,2,3 GENOTYPE_ENOCDED.csv\n";
}


my $dataType = $ARGV[0]; 
my $gFile = $ARGV[1];
my $codingScheme = $ARGV[2];
my $output = $ARGV[3]; 

if($dataType eq "dominant"){
	encodeDominant($gFile,$codingScheme,$output);
}elsif($dataType eq "iupac"){
	encodeIUPAC($gFile,$codingScheme,$output);
	#print "Encoding IUPAC";
}
################## functions ###################
# encode Dominant format
# if dominant, encoding scheme will always be (x,y) where:
# x = 1st allele
# y = 2nd allele
sub encodeDominant{
	my ($geno, $code, $output) =@_;
	my $linecount = 0;
	my @header;
	my @lines;
	my ($a,$b) = split(',',$code);
	open(IN, '<', $geno) or die "Cannot open $geno.\n";
	open(OUT, '>', $output);

	# encode as we read per line
	while(my $line = <IN>){
		chomp $line;
		if($linecount == 0){ ## parse header to get the lines	
			print OUT $line."\n";
		}else{
			@lines = split(',', $line); # split row contents
			for (@lines){s/0/$a/g}	# change all 0 to first number given in the code
			for (@lines){s/1/$b/g} # change all 0 to 2nd number given in the code
			my $row = join(',',@lines); # join everything
			print OUT $row."\n"; # output as encoded
		}
		$linecount++;
	}
	close(IN);
	close(OUT);
}

## encode IUPAC or bi-allelic format
##  Encoding scheme:
## 0- minor homo (w)
## 1- hets (x)
## 2- major homo (y)
## 3- missing (z)
## code = (w,x,y,z)
sub encodeIUPAC{
	my ($geno,$code,$output) = @_;
	my $linecount = 0;
	my @row;
	my ($w,$x,$y,$z) = split(',',$code);	
	my $useThisCode = $z; # default is set to missing
	## open files
	open(IN, '<', $geno) or die "Cannot open file: $geno\n";
	open(OUT, '>', $output);	

	## go through the lines in the genotype
	while(my $line = <IN>){
		chomp $line;	
		if($linecount == 0){ #print header
			print OUT $line."\n";
		}else{ # parse succeeding data rows
			@row = split(',',$line);

			## randomize what to use for minor or major homo
			if(int(rand(2)) == 0){
				$useThisCode = $w
			}else{$useThisCode=$y;}
			for (@row){s/A|C|T|G/$useThisCode/g} # encode every DNA base in the line
			for (@row){s/R|K|M|S|W|Y/$x/g} # encode all hets 
			for (@row){s/N|^-$|^\.$/$z/g} # encode missing values

			my $encoded = join(',',@row); # join everything
			print OUT $encoded."\n"; # output as encoded
		}
		$linecount++;
	}
	close(IN);
	close(OUT);
}

###### end of encode ########





