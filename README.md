# Multipass

[![CircleCI build status](https://circleci.com/gh/canonical-web-and-design/multipass.run.svg?style=shield)](https://circleci.com/gh/canonical-web-and-design/multipass.run)
[![Code coverage](https://codecov.io/gh/canonical-web-and-design/multipass.run/branch/main/graph/badge.svg)](https://codecov.io/gh/canonical-web-and-design/multipass.run)

Codebase for https://multipass.run - the marketing website for Canonical's multipass product.

## Local development

The simplest way to run the site locally is with the dotrun snap:

```bash
dotrun
```

Once the containers are setup, you can visit <http://127.0.0.1:8026> in your browser.

### Building CSS

For working on [Sass files](static/sass), you may want to dynamically watch for changes to rebuild the CSS whenever something changes.

To setup the watcher, open a new terminal window and run:

```bash
./run watch
```

# Deploy

You can find the deployment config in the deploy folder.

## Licence

Code licensed [LGPLv3](http://opensource.org/licenses/lgpl-3.0.html) by [Canonical Ltd.](http://www.canonical.com/).

With ♥ from Canonical
