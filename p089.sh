cp p089.input p089_roman_minimal.txt
sed -i 's/VIIII/IX/g' p089_roman_minimal.txt
sed -i 's/IIII/IV/g' p089_roman_minimal.txt
sed -i 's/LXXXX/XC/g' p089_roman_minimal.txt
sed -i 's/XXXX/XL/g' p089_roman_minimal.txt
sed -i 's/DCCCC/CX/g' p089_roman_minimal.txt
sed -i 's/CCCC/CD/g' p089_roman_minimal.txt
FILESIZEORIG=$(stat -c%s p089.input)
FILESIZEMINIMAL=$(stat -c%s p089_roman_minimal.txt)
FILESIZEDIFF="$((FILESIZEORIG-FILESIZEMINIMAL))"
echo "$FILESIZEDIFF"
rm p089_roman_minimal.txt
