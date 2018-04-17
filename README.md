# Rename you pdf file

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>

Change the name of the pdf file automatically mostly.

When you download papers from SCI or ScienceDiract. Sometimes the name of the file is not actually the name of the essay. When you have massive amount of paper downloaded, it is convinient that the name of the pdf file match the name of the essay. I write this python script to do this automatically.

Right noe, there are 2 methods packaged. The first one is to use `pdfrw` to read the Info of the file. The scond method is to use `PyPDF2` to read the actual title of the paper.

In order to use this script run

```python
pip install -r requirements.txt
```

first. Then go into the directory which contants the python script and run 

```
python file_try1.py
```

Then input the directory whitch contains the pdf file directly.
