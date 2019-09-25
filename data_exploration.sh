
fname=$1
wc -l $fname
grep 'LOC' $fname | wc -l
grep 'MISC' $fname | wc -l
grep 'ORG' $fname | wc -l
grep 'PER' $fname | wc -l
