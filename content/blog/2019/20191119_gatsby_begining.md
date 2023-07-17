---
Title: Gatsby Beginings
Date: 2019-11-19 21:12
Status: published
Category: Code
Tags: Open Source
Keywords: Open Source
Slug: gatsby-beginings
original_url: blog/gatsby-beginings.html
Author: Justin Cooksey
Image: gatsby-logo.jpg
Summary: Hacktoberfest is a brilliant idea to get people involved in Open Source, with a friendly competition that's really only about being involved.
---

<img src="{attach}gatsby-logo.jpg"  width="33%" height="33%">

This is the beginings of this site utilising [GatsbyJS](https://www.gatsbyjs.org/).

While I am learning parts of [GatsbyJS](https://www.gatsbyjs.org/) as well as expanding knowledge on [ReactJS](https://reactjs.org/), I am not following through somone tutorial and simply pasting things in from that. I want to work on this to understand how these frameworks operate. As such it has been, and will be, a little jumpy as I don't follow a set path through setting up this site as I would if I followed through someones tutorial.

At present I have a fairly basic blog/thoughts/articles system operational, as well as a landing page. All of the pages have very little styling at this point, which certainly needs to be worked on. I also need to get some content up, expecially in the about page. I've also got options to discover on things such as styling where I'm exploring:

- [styled-components](https://www.styled-components.com/) _Using this currently_
- [Emotion](https://emotion.sh/docs/introduction)
- CSS & SASS
- I'm sure others as well

I've currently used the following plugins:

- `gatsby-plugin-react-helmet` for correct SEO elements on the pages
- `gatsby-plugin-react-helmet-canonical-urls` to make pages cannonical for this site. The source site.
- `gatsby-plugin-styled-components` for styling
- `gatsby-plugin-mdx` to manage the Markdown files to be used as post content
- `gatsby-remark-vscode` to have any Markdown code blocks styled to look like vscode screenshots
- `gatsby-plugin-feed` to create RSS feed data to allow sharing via feeds
- `gatsby-plugin-sitemap` to screate sitemap files
- `gatsby-plugin-robots-txt` to create robots.txt files
- `gatsby-plugin-offline` & `gatsby-plugin-manifest` to make the site a Progressive Web App
- `gatsby-plugin-netlify-cms` suppoprt for Netlify CMS system to allow online creation of blog entries

Still a long way to go.
