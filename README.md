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

## References

1. [Find all files in a directory with extension .txt in Python - Stack Overflow
](https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python)

2. [Rename multiple files in a directory in Python [duplicate] - Stack Overflow
](https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python)

3. [How to set the current working directory? - Stack Overflow
](https://stackoverflow.com/questions/1810743/how-to-set-the-current-working-directory)

4. [Extracting text from a PDF file using Python - Stack Overflow
](https://stackoverflow.com/questions/34837707/extracting-text-from-a-pdf-file-using-python)

5. [wordsegment 1.2.0 · PyPI](https://pypi.org/project/wordsegment/)

6. [Python concat string with list - Stack Overflow
](https://stackoverflow.com/questions/8546245/python-concat-string-with-list)
