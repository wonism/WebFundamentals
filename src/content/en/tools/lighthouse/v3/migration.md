project_path: /web/tools/_project.yaml
book_path: /web/tools/_book.yaml
description: TODO

{# wf_updated_on: 2018-05-01 #}
{# wf_published_on: 2018-05-01 #}
{# wf_blink_components: N/A #}

# Migration Guide: Lighthouse 2 to 3 {: .page-title }

This guide is intended for Lighthouse CLI and Node module users. It details how the configuration
and output of 

Intended for CLI and Node module users. DevTools and Extension users won't have significant
changes to their workflows. See Update post.

There are two major changes:

* Configuration
* JSON output

## Configuration changes {: #config }

## Output schema changes {: #output }

The code below represents the current output schema in Lighthouse 2. The highlighted properties
represent the ones that you'll need to change in order to migrate to Lighthouse 3.

<pre>
{
  userAgent: ...,
  lighthouseVersion: ...,
  generatedTime: ...,
  <strong>initialUrl</strong>: ...,
  url: ...,
  runWarnings: ...,
  <strong>reportGroups</strong>: ...,
  <strong>timing</strong>: ...
  audits: {
    
  },
  reportCategories: [
    {
      id: ...,
      name: ...,
    }
  ]
}
</pre>

The table below suggests how to change each item.
