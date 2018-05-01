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


The table below lists all of the changes that you need to make regarding how you consume
the JSON output of Lighthouse.

* When a row has a value in both the **v2** and **v3** columns, it means that you should
  change any reference to the **v2** property to the **v3**-equivalent.
* When a **v2** property doesn't have an equivalent, the **Suggestions** column describes
* Note that items such as <var>ID</var> represent placeholder text.

<table>
  <tr>
    <th>v2 Property</th>
    <th>v3-Equivalent</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><code>initialUrl</code></td>
    <td><code>requestedUrl</code></td>
    <td></td>
  </tr>
  <tr>
    <td><code>reportGroups</code></td>
    <td></td>
    <td>Removed. Use TODO instead.</td>
  </tr>
  <tr>
    <td><code>timing</code></td>
    <td></td>
    <td>Removed. Use TODO instead.</td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.name</code></td>
    <td><code>audits.<var>ID</var>.id</code></td>
    <td>
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.description</code></td>
    <td><code>audits.<var>ID</var>.title</code></td>
    <td>
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.helpText</code></td>
    <td><code>audits.<var>ID</var>.description</code></td>
    <td>
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.displayValue</code></td>
    <td></td>
    <td>
      Removed. Use TODO instead.
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.notApplicable</code></td>
    <td></td>
    <td>
      Removed. Use TODO instead.
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.informative</code></td>
    <td></td>
    <td>
      Removed. Use TODO instead.
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.manual</code></td>
    <td></td>
    <td>
      Removed. Use TODO instead.
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.rawValue</code></td>
    <td></td>
    <td>
      Removed. Use TODO instead.
    </td>
  </tr>
  <tr>
    <td><code>audits.<var>ID</var>.extendedInfo</code></td>
    <td></td>
    <td>
      Removed. Use TODO instead.
    </td>
  </tr>
</table>
