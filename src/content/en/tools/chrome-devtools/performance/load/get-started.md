project_path: /web/tools/_project.yaml
book_path: /web/tools/_book.yaml
description: Learn how to view messages and run JavaScript in the Console.

{# wf_updated_on: 2018-04-10 #}
{# wf_published_on: 2018-04-05 #}
{# wf_blink_components: Platform>DevTools #}

{% include "web/tools/chrome-devtools/_shared/styles.html" %}

# Get Started With Analyzing Load Performance {: .page-title }

{% include "web/_shared/contributors/kaycebasques.html" %}

This tutorial teaches you how to use Chrome DevTools to analyze load performance
and detect common performance bottlenecks.

## Discover bottlenecks and establish a baseline with the Audits panel {: #discover }

The first step in performance optimization is to establish a baseline. The baseline provides
metrics on how your page currently performs. After you make optimizations to your page, you
take another set of measurements, and then compare the new metrics with the baseline. If your
page loads faster, then the optimization was a success.

The **Audits** panel is the recommended approach for establishing a baseline. You just click a
couple of buttons, and the **Audits** panel collects a whole bunch of metrics on the page's
load performance. It also shows you potential bottlenecks and provides guidance on how to fix
those bottlenecks.

1. [Open the demo](TODO).
1. Press <kbd>Command</kbd>+<kbd>Option</kbd>+<kbd>C</kbd> (Mac) or
   <kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> (Windows, Linux, Chrome OS) to
   open DevTools.
1. Click the **Audits** tab.
1. Click **Perform An Audit**.
1. Enable all the categories.
1. Click **Run Audit**.

TODO Chrome 67 has a **View Trace** button that opens up a Perf recording. That's the segue.

TODO mention mobile throttling.

## Feedback {: #feedback }

<aside class="note">
  <b>Help me help you!</b> Hi, I'm Kayce. I wrote this tutorial. Please take a moment to
  provide feedback. I really do monitor this data, and it helps me create better tutorials for
  you.
</aside>

Was this tutorial helpful?

{% framebox width="auto" height="auto" enable_widgets="true" %}
<script>
var label = 'Load Performance / Get Started / Helpful';
var url = 'https://github.com/google/webfundamentals/issues/new?title=[' +
      label + ']';
var feedback = {
  "category": "DevTools",
  "choices": [
    {
      "button": {
        "text": "Yes"
      },
      "response": "Thank you for the feedback!",
      "analytics": {
        "label": label
      }
    },
    {
      "button": {
        "text": "No"
      },
      "response": 'Sorry to hear that. Please <a href="' + url +
          '" target="_blank">open a GitHub issue</a> and tell me how I can ' +
          'make it better.',
      "analytics": {
        "label": label,
        "value": 0
      }
    }
  ]
};
</script>
{% include "web/_shared/multichoice.html" %}
{% endframebox %}
