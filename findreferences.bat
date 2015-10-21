python findreferences.py -i %1 > names.txt
python findreferences.py -i %1 -n names.txt > output.dot
dot -Tpdf -O -v -Gsize="10,15!" -Gratio=0.6 -Nfontname=Arial -Nfontsize=12 -Nshape=box -Ktwopi -Goverlap=prism100 output.dot
start output.dot.pdf
