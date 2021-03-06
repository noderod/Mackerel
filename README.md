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
  If no title is provided, the title defaults to the topic.  
  If the user wishes to provide a subtitle, separate it using a "/+/" without spaces.  
  Since this program is primarily based on wikipedia, all names are not influenced at all
  by capital letters or their absence.

  i.e. :  
    python jurel.py Augustus 6 Augustus/+/Emperor of Rome

  The program does not support any spaces in the topic, so they must be changed into "-".


  Currently, only the first slide (the title), will have an accompanying image, which may
  be covering the text.


### Updates and versions

**0.1** - Current - Minimum Viable Product  
_0.1.3_ : Changed the way sentences are ordered, to maintain chronological order.
