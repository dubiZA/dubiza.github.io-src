
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
The [Fedora Magazine](#resources) write up I followed suggests creating one GitHub repo named the way GHP requires, which is in the form `username.github.io` (follow the [official GHP docs][5] if you are unsure how to do this). This is where the output files from Pelican will go. The name of the repo **must exactly match** `username.github.io` -- if it does not, GHP will not work. Make sure to initialize the repo with a readme. I left mine as a public repo.
[5]: <https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site> "GitHub Pages Docs"

I suppose the second repo name doesn't matter too much, but it is suggested to name it `username.github.io-src`. This repo will contain the source files used to generate the HTML, CSS, etc. I set mine up with a `.gitignore` for Python and, though it's probably not necessary, have it as a private repo.

## Cloning the Repos


# Setting Up Python and Pelican


## Creating the Python Virtual Environment


## Installing Pelican


## Initializing Pelican


## Configuring Pelican


# Setting Up a Custom Domain


# Fonting GitHub Pages with Cloudflare CDN