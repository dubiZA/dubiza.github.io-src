Tags: python, pelican, github, reference
Status: published

Over the last few days I have been trying to figure out how I want to go about chronicling my... accomplishments? I figured, if I'm going to spend time learning something, I should also invest some time documenting what I have learned for three reasons (in no particular order):

- So that I don't have to find all the sources out there on the web that lead to success all over again
- With the hopes that it proves useful to someone out there in comming days
- The stuff I've worked on stays in my head as a result of "writing it down" so to speak

Setting up this site with GitHub Pages using Pelican (the Python based static site generator) was enough of a challenge that it seems like a fantastic place to start writing. So, let's get started!

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

I suppose the second repo name doesn't matter too much, but it is suggested to name it `username.github.io-src`. This repo will contain the source files used to generate the HTML, CSS, etc. I set mine up with a `.gitignore` for Python to make sure I'm not commiting unnecessary Python specific config to the repo.

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
Having completed the `pelican-quickstart`, you'll have a pretty good initial baseline to build up from. Most of the initial "building up" is done in the pelican configuration files `pelicanconf.py` and `publishconf.py`. Some additional configuration will be done through updating the default directory structure as well.

### <a id="config-files"></a>Config Files
- `pelicanconf.py` is the configuration file Pelican uses when building/publishing and running things locally. The settings defined here are also imported in to the `publishconf.py` file, so it's a good place to configure as many settings as possible that aren't dependant on the final published "product".
- `publishconf.py`, as mentioned above, imports the `pelicanconf.py` configurations and allows you to overide anything that needs to be changed for the live version of the site. And example would be the `SITEURL` setting, which you'll defenitely want different between to two files - don't worry, the quickstart will have taken care of that one for you!

Open `publishconf.py` and add the following line:

    :::python
    DELETE_OUTPUT_DIRECTORY = False

This is very important - when the publish command is issued, Pelican will try clean up after itself by default. But with the way we have things set up, that would eliminate our submodule and make life difficult every time we publish.

At this point, you probably don't need to mess around with `pelicanconf.py` too much. Most of the defaults will work for the purposes of this writeup. The Pelican docs have tons of information about [available settings](https://docs.getpelican.com/en/latest/settings.html "Pelican Settings").

There are a few addtions that we'll make here though. Add the following lines to `pelicanconf.py`:

    :::python
    STATIC_PATHS = ['images/', 'extra/CNAME']
    EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

The above lines will set things up to help Pelican find the images directory and get things ready to use a custom domain name. **NOTE:** If you are not planning to use a custom domain, I believe the CNAME entries are unnecessary.

The next setting I use to avoid publishing an incomplete article prematurely is:

    :::python
    DEFAULT_METADATA = { 'status': 'draft', }

This will place generated pages for an article in `SITEURL/drafts/article_name.html`. Once a post is complete, the `Status: published` page "front matter" or page meta will tell Pelican it's ready to go live. 

### Test Post
At this point, it seems like it's time for a first post test. Create a new file in the `content` directory called `first-post.md`. Yes, Pelican uses Markdown (or reStructured Text) for page authoring. For a reference, see [markdownguide.org](https://www.markdownguide.org/basic-syntax "Markdown Reference")

    :::markdown
    Title: First Post
    Date: 2021-01-01 15:00
    Category: Other
    Tags: tag1, tag2, tag3
    Slug: first-post
    Author: Your Name
    Summary: Summary of your blog post.

    Start your first blog post here.
    Lorem Ipsum
    etc...

There are ways to avoid using some (or even any of) the meta data. Take a look at Pelican docs for details.

With the page written up, it can be test published by using the commands:

    :::zsh
    make html && make devserver

If you system is not set up for `make`, you can also run:

    :::python
    pelican content -o output -s pelicanconf.py
    pelican -r -l --ignore-cache

Either way you choose to generate the local instance, it will start up a local webserver listening at `localhost:8000`. Navigate there with your favorite browser. If I have guided you correctly up to this point, you should have a functioning dev instance of you new site. If things are broken, well... I'm sorry. But you favorite search engine is your friend :D.

## <a id="publishing"></a>Publishing to GitHub
Once you are satisfied with you post, we'll need to move from draft to publish, then publish and push all those changes to GitHub. Make sure to add the meta `Status: published` to the post.

    :::markdown
    Title: First Post
    Date: 2021-01-01 15:00
    Category: Other
    Tags: tag1, tag2, tag3
    Slug: first-post
    Author: Your Name
    Summary: Summary of your blog post.
    Status: published

    Start your first blog post here.
    Lorem Ipsum
    etc...

Next, publish the page using `make` or the `pelican` command:

    :::zsh
    make publish

Or

    :::zsh
    pelican content -o output -s publishconf.py

Then go through the `git` workflow. This is all assuming you are in the root of the `ghpages/` directory, as with all the other commands in this article. You will need to follow the git flow twice, first in the `output/` directory or submodule, then in the `ghpages` root directory.

Before running the git workflow, add `*.pyc` to your `.gitignore` file

    :::zsh
    cd output
    git add .
    git commit -m 'commit message'
    git push

    cd ..
    git add .
    git commit -m 'commit message'
    git push

Within a few moments, you should be able to visit https://username.github.io with your site live. Now for setting up the custom domain.

# Setting Up a Custom Domain
I'm not going to go over setting up DNS with your domain registrar. That really depends on who your registrar is and there are far too many of those. The [GitHub Pages docs][6] have some guidance here. The GHP docs cover the GitHub config, but I'll mention it here briefly too.
[6]: <https://docs.github.com/en/github/working-with-github-pages/configuring-a-custom-domain-for-your-github-pages-site> "GitHub Pages Custom Domains"

Go to the `username.github.io` repo > settings > GitHub Pages section. Add your registered domain name in the field and hit save. GHP supports several types of domain: 

- www.domain.com
- custom subdomain (like blog.domain.com)
- apex domain like domain.com

What you provide to GHP will be dependant on how you have set up your DNS records. Whatever it is you choose, it will need to match what we apply to a new file that needs to be created in `extra/`. In an [earlier configuration](#config-files) step for Pelican, we applied a the `STATIC_PATHS` AND `EXTRA_PATH_METADATA` settings, referencing a file called `CNAME`. Create this file now, with no file extention in the `extra/` directory. Edit the new file by adding the same domain configuration you applied to the GHP setting for your repo. There should be no `http(s)://` or trailing slash on what you put here. So in my case, with using the apex domain, it was simply

    :::
    dariushall.com

Once this is complete, [republish you site](#publishing). Within a few moments, the site should be alive and well. At this point, you should also be able to check the `Enforce HTTPS` setting within the GHP settings on the repo. This will have GitHub force a redirect from http requests to https.

# Setting up Cloudflare
To improve the user experience and protect you website from some level of abuse, I would encourage you to take advantage of Cloudflare's really generous [free/personal website tier](https://www.cloudflare.com/plans/ "Cloudflare Pricing Page"). In order to do so, sign up for a free account, add your website and follow the instructions. I think they were quite clear and easy to use. Cloudflare basically does all the work for you by importing DNS settings from your registrar and walking you through how to change the default nameservers to Cloudflare's nameservers.

Cloudflare will then start acting as a Content Deliver Network for your website. A CDN will cache static assets from your website (HTML, JS, CSS, Images, etc.) by requesting them from your website (or origin as they like to call it). Once the CDN has those files, it distributes them to hundreds of CDN servers around the world. Next time a visitor to your site requests an asset cached by the CDN, they will be able to receive that asset from their closest CDN server, dramatically increasing the response time for them, even if they are on the oposite side of the word to your origin server. Check out [Cloudflare's explanation](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/ "What is a CDN") if you want more details.

# Wrapping Up
So, that's it. If all goes well, and I haven't provided a completely garbage set of instructions here, you should have a shiny new website/blog up and running that performs extremely well, and that can withstand up to 59Tbps DDoS attacks, for the cost of just your domain name registration (and maybe a few grey hairs trying to troubleshoot issues). Feel free to take a look at my [source repo](https://github.com/dubiZA/dubiza.github.io-src "Pelican Source Repo")