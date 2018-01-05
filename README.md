## An Automated Writing Tool

Mackerel provides an automated, easy to use alternative for company or school
writing tasks. Simply provide the topic and/or files and we will do the rest.


### How it works
Mackerel is, at its core, a text summarizer based on [sumy](https://github.com/miso-belica/sumy).
It simply reorganizes the result into an usable product.  
Current development is geared towards powerpoint presentations.


### Necessary Dependencies
[**Sumy**](https://github.com/miso-belica/sumy): Text summarizer  
[**Wikipedia**](https://pypi.python.org/pypi/wikipedia/): Access to the wikipedia API  
[**python-pptx**](http://python-pptx.readthedocs.io/en/latest/user/install.html): Creates powerpoints using python.  


Sumy requires the download of certain libraries before this project is used for
the first time. Fortunately, the error message is enough as a guide.


### Usage
**Jurel**: A command line tool to create a presentation provided a topic. The correct order of arguments would be:  
python jurel.py {TOPIC} {SLIDE_NUMBER} {COMPLETE_TITLE}

  i.e. :  
    python jurel.py Augustus 6 Emperor of Rome

  If no slide number is provided, the program defaults to 8 (one of which is the title).
  If no title is provided, the title defaults to the topic
  If the user wishes to provide a subtitle, separate it using a "/+/" without spaces.

  i.e. :  
    python jurel.py Augustus 6 Augustus/+/Emperor of Rome


### Updates and versions
**0.0** - Current - Incomplete.
