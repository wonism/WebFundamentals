project_path: /web/_project.yaml
book_path: /web/updates/_book.yaml
description: TODO

{# wf_updated_on: 2018-04-30 #}
{# wf_published_on: 2018-04-18 #}
{# wf_tags: lighthouse #}
{# wf_featured_image: /web/progressive-web-apps/images/pwa-lighthouse.png #}
{# wf_featured_snippet: TODO #}
{# wf_blink_components: Platform>DevTools #}

# Announcing Lighthouse 3.0 {: .page-title }

<img src="/web/progressive-web-apps/images/pwa-lighthouse.png"
     style="height:auto;width:50%;"
     class="lighthouse-logo attempt-right" alt="Lighthouse Logo">

Lighthouse 3.0 is out! New features include:

* Faster audits and less fluctuation in scores.
* New audit: First Contentful Paint
* New report UI
* Throttle configuration

Major changes include:

* 3G -> 4G
* New scoring model.
* Input configuration for Node and CLI.
* JSON output.
* First Interactive -> First CPU Idle
* Perceptual Speed Index changed to Speed Index. Different measurement algorithm.

## Summary of noticeable changes {: #summary }

TODO this should be the intro para. Just focus on noticeable changes.

This is a summary of the changes that you might notice as you migrate from Lighthouse 2 to 3.

* Faster loading score, because of 4G

## Faster audits and less variability {: #lantern }

Thanks to a new internal auditing engine, codenamed Lantern, Lighthouse 3 completes your audits
faster, with less variability between runs.

Previously, Lighthouse would literally reload your page many times, in order to determine how the
page loaded under different conditions. Now, Lighthouse audits your page once, then uses Chrome's
trace data to estimate your score under different conditions.

## New Report UI {: #ui }

TODO don't like the sentence below...

The Lighthouse team conducted usability studies to learn how to improve the report UI, and
got a lot of useful feedback.

<figure>
  <img src="https://placeholder.com/500x500"
       alt="A screenshot of the new report UI."/>
  <figcaption>
    <b>Figure X</b>. A screenshot of the new report UI
  </figcaption>
</figure>

Thanks to [Jason](TODO) for conducting the user experience research, and to [Hwi](TODO) for
designing the new UI. And thanks to all of the research participants for your valuable feedback.

## New scoring model {: #scoring }

## New default network throttling level: 4G {: #throttling }

4G is now the default network throttling level.

## Configuration changes {: #config }

## Output changes {: #output }

The Lighthouse team has collected a lot of feedback from 

If you use Lighthouse in an automated workflow, such as CI, upgrading to Lighthouse 3 will
unfortunately require major changes.
