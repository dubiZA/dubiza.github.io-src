
Over the last few days I have been trying to figure out how I want to go about chronicling my... accomplishments? I figured, if I'm going to spend time learning something, I should also invest some time documenting what I have learned for three reasons (in no particular order):

- So that I don't have to find all the sources out there on the web that lead to success all over again
- With the hopes that it proves useful to someone out there in comming days
- The stuff I've worked on stays in my head as a result of "writing it down" so to speak

Setting up this site with GitHub Pages using Pelican (the Python based static site generator) and fronting it with Cloudflare's free tier CDN was enough of a challenge that it seems like a fantastic place to start writing. So, let's get started!

![pelican]({static}/images/birger-strahl-3FDMW9XoNXU-unsplash.jpg)
Photo by [Birger Strahl][1] on [Unsplash][2]  

[1]: <https://unsplash.com/@bist31?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText> "Birger Strahl"
[2]: <https://unsplash.com/s/photos/pelican?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText> "Unsplash"

---

# <a id="resources"></a>Resources I Used
I followed two guides to get this to work:

- [Fedora Magazine][3] has a pretty solid write up that helped the most in figuring things out
[3]: <https://fedoramagazine.org/make-github-pages-blog-with-pelican/>
- [Tom Ordonez's][4] blog is where I found the Fedora Magazine reference and the idea to configure the GitHub Pages site with Cloudflare as CDN
[4]: <https://www.tomordonez.com/make-static-website-python-github-pages/>

# Setting Up GitHub
If you're not familiar with GitHub Pages, you can [read more about it here](https://pages.github.com/ "GitHub Pages"). In a nutshell, GitHub very generously offers to host "static" web content for you and/or your projects. No infrastructure to worry about. Extremely minimal configuration. The power of git workflow. A common use case for this is publishing personal/project blogs, for which, GitHub integrates with the Ruby based static site generator [Jekyl](https://jekyllrb.com/ "Jekyll Static Site Generator").

While I'm sure Jekyll is great, I'm a Python guy and decided to make the GitHub Pages (GHP) thing a tiny bit more complicated by using a Python based static site generator called [Pelican](https://blog.getpelican.com/ "Pelican Python Static Site Generator"). While GHP is capabile of automatically building the static files (HTML, etc.) when using Jekyll, choosing to use Pelican appears to mean doing things more manually (I say appears because I haven't actually looked further in to automating builds with anything else). To accomodate this manual process, two GitHub repos are suggested.

## Creating the Repos
The [Fedora Magazine](#resources) write up I followed suggests creating one GitHub repo named the way GHP requires, which is in the form `username.github.io` (follow the [official GHP docs][5] if you are unsure how to do this). This is where the output files from Pelican will go. The name of the repo **must exactly match** `username.github.io` -- if it does not, GHP will not work. Make sure to initialize the repo with a readme. I left mine as a public repo. This repo will be configured as a submodle within the second repo at a later stage.
[5]: <https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site> "GitHub Pages Docs"

I suppose the second repo name doesn't matter too much, but it is suggested to name it `username.github.io-src`. This repo will contain the source files used to generate the HTML, CSS, etc. I set mine up with a `.gitignore` for Python and, though it's probably not necessary, have it as a private repo.

## Cloning the Repos
Once you have the repos created, they can be cloned to your local machine, but **STOP**: if you are familiar with `git clone`. Don't clone them both just yet. The `username.github.io` repo will be set up as a submodule within `username.github.io-src`. So, follow this sequence to make sure it's done right:

This assumes you are set up in GitHub to [clone via SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh "Using GitHub with SSH"). Make sure to replace `<your_username>` and to execute this command where you want the cloned repo to exist locally. It will create a new directory called `ghpages` in your current working directory.

    :::zsh
    git clone git@github.com:<your_username>/<your_username>.github.io-src ghpages

Next, change to the `ghpages` directory

    :::zsh
    cd ghpages

Now you can set up the submodule. I'll be honest here, I'm not sure if this is the best way to do this or not, I was just following directions. But the ghp-import method the [Pelican docs](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github "Pelican Docs") talked about confused me and the Fedora Mag post seemed to confirm it didn't work as expected, so, I went with the "ask no questions" approach and blindly followed Fedora Mag. If you're interested, [read more about submodules here](https://git-scm.com/book/en/v2/Git-Tools-Submodules "Git Submodules").

    :::zsh
    git submodule add git@github.com:username/username.github.io.git output

Your folder structure will look something like this at this point

    :::zsh
    ghpages/
    |-- output/

# Setting Up Python and Pelican
As mentioned previously, Pelican is a Python static site generator. As such, it is probably wise to use a virtual environment when installing and configuring Pelican so as not to interfere with your "global" Python environment. Personally, I am a huge fan of [pyenv](https://github.com/pyenv/pyenv "GitHub Pyenv Page") for managing multiple versions of Python. When using the [pyenv-installer](https://github.com/pyenv/pyenv-installer "GitHub pyenv-installer Page") script, you will also have access to [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv "GitHub pyenv-virtualenv Page"). The combination of these tools is what I use to configure my Python development environments.

Having said all that, I'll assume you're just using your system Python for these purposes.

## Creating the Python Virtual Environment
Creating a Python virtual environment is pretty simple. Making sure to be in the `ghpages` directory, run the following command (I'm putting python3 here. While Python 2 is EOL, many OSes have not completely migrated to Python 3 yet. In many cases, running `python --version` in your terminal will show some version of Python 2 as the system python. I think it's safe to assume that running `python3` will ensure you're using Python 3 even if your system's default Python version is 3.x):

    :::zsh
    python3 -m venv .venv

With the virtual environment created, it's time  to activate it:

    :::zsh
    source ./.venv/bin/activate

The venv can be exited using:

    :::zsh
    deactivate

## Installing Pelican
Now that you have the virtual environment configured and active, you can install Pelican and it's dependancies without it affecting your system Python environment.

Installing Pelican is as easy as:

    :::zsh
    pip3 install pelican
    pip3 install Markdown
    pip3 install typogrify

## Initializing Pelican
With Pelican installed, getting the base configuration up and running is pretty easy. Again, making sure to be in `ghpages`, run:

    :::zsh
    pelican-quickstart

Pelican will present a series of questions to help in setting up the base configuration. Most of the options have defaults which are acceptable for this. Defaults will be expressed either in square regulare braces/parentheses `[ ]` or `( )`. Answer them as follows:

    :::zsh
    Welcome to pelican-quickstart v4.5.4.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.

    Where do you want to create your new web site? [.]
    What will be the title of this web site? <provide your desired title>
    Who will be the author of this web site? <your name>
    What will be the default language of this web site? [en]
    Do you want to specify a URL prefix? e.g., https://example.com   (Y/n)
    What is your URL prefix? (see above example; no trailing slash) https://username.github.io <or customer domain, in my case https://dariushall.com>
    Do you want to enable article pagination? (Y/n)
    What is your time zone? [Europe/Paris] <use a tz database compatible name>
    Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n)
    Do you want to upload your website using FTP? (y/N)
    Do you want to upload your website using SSH? (y/N)
    Do you want to upload your website using Dropbox? (y/N)
    Do you want to upload your website using S3? (y/N)
    Do you want to upload your website using Rackspace Cloud Files? (y/N)
    Do you want to upload your website using GitHub Pages? (y/N) Y <set this to Y>
    Is this your personal page (username.github.io)? (y/N) Y <set this to Y>

The options you'll need to change from default are the `Do you want to upload your website using GitHub Pages?` and `Is this your personal page (username.github.io)?` Make sure to change those to `Y`.

## Configuring Pelican


# Setting Up a Custom Domain


# Fonting GitHub Pages with Cloudflare CDN