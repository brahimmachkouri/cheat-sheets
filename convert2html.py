#!/usr/bin/python3
# -*- coding: utf-8 -*-

# author: Brahim Machkouri

import sys
import re
from jinja2 import Template

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    title = None
    commands = []

    for line in lines:
        # Recherche du titre dans la ligne contenant "##"
        #title_match = re.match(r'^\s*##\s*(.*)$', line)
        title_match = re.match(r'^\s*##\s*([^#].*)$', line)
        if title_match:
            title = title_match.group(1).strip()

        # Ignorer les lignes avec "| Commande | Description |" et "| --- | --- |"
        if "| Commande | Description |" in line or "| --- | --- |" in line:
            continue

        # Extraire les commandes et descriptions des lignes du tableau
        command_match = re.match(r'^\s*\|\s*`(.*)`\s*\|\s*(.*)\s*\|$', line)
        if command_match:
            command = command_match.group(1).strip()
            description = command_match.group(2).strip()
            commands.append({"commande": command, "description": description})

    return title, commands


def generate_html(title, commands):
    # Charger le template Jinja2 depuis une chaîne de caractères
    html_template = """
    <!DOCTYPE html>
    <html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.mathpix.com/fonts/cmu.css"/>
        <style>
          html,body {
    width: 100%;
    height: 100%;
  }
  *, *::before,*::after {
    box-sizing: border-box;
  }
  @-ms-viewport {
    width: device-width;
  }
  body {
    margin: 0;
    color: #1E2029;
    font-size: 14px;
    line-height: normal;
  }
  hr {
    box-sizing: content-box;
    height: 0;
    overflow: visible;
  }
  h1, h2, h3, h4, h5, h6 {
    margin-top: 0;
    margin-bottom: 0.5em;
    color: rgba(0, 0, 0, 0.85);
    font-weight: 500;
  }
  p {
    margin-top: 0;
    margin-bottom: 1em;
  }
  ol, ul, dl {
    margin-top: 0;
    margin-bottom: 1em;
  }
  ol ol, ul ul, ol ul, ul ol {
    margin-bottom: 0;
  }
  dt {
    font-weight: 500;
  }
  dd {
    margin-bottom: 0.5em;
    margin-left: 0;
  }
  blockquote {
    margin: 0 0 1em;
  }
  dfn {
    font-style: italic;
  }
  b, strong {
    font-weight: bolder;
  }
  small {
    font-size: 80%;
  }
  sub, sup {
    position: relative;
    font-size: 75%;
    line-height: 0;
    vertical-align: baseline;
  }
  sub {
    bottom: -0.25em;
  }
  sup {
    top: -0.5em;
  }
  a {
    color: #0B93ff;
    text-decoration: none;
    background-color: transparent;
    outline: none;
    cursor: pointer;
    transition: color 0.3s;
  }
  a:hover {
    color: #33aaff;
  }
  a:active {
    color: #0070d9;
  }
  a:active, a:hover {
    text-decoration: none;
    outline: 0;
  }
  a[disabled] {
    color: rgba(0, 0, 0, 0.25);
    cursor: not-allowed;
    pointer-events: none;
  }
  pre, code, kbd, samp {
    font-size: 1em;
  }
  pre {
    margin-top: 0;
    margin-bottom: 1em;
    overflow: auto;
  }
  figure {
    margin: 0 0 1em;
  }
  img {
    vertical-align: middle;
    border-style: none;
  }
  svg:not(:root) {
    overflow: hidden;
  }
  table {
    border-collapse: collapse;
  }
  caption {
    padding-top: 0.75em;
    padding-bottom: 0.3em;
    color: rgba(0, 0, 0, 0.45);
    text-align: left;
    caption-side: bottom;
  }
  th {
    text-align: inherit;
  }

mjx-container[jax="SVG"] {
  direction: ltr;
}

mjx-container[jax="SVG"] > svg {
  overflow: visible;
}

mjx-container[jax="SVG"] > svg a {
  fill: blue;
  stroke: blue;
}

mjx-assistive-mml {
  position: absolute !important;
  top: 0px;
  left: 0px;
  clip: rect(1px, 1px, 1px, 1px);
  padding: 1px 0px 0px 0px !important;
  border: 0px !important;
  display: block !important;
  width: auto !important;
  overflow: hidden !important;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

mjx-assistive-mml[display="block"] {
  width: 100% !important;
}

mjx-container[jax="SVG"][display="true"] {
  display: block;
  text-align: center;
  margin: 1em 0;
}

mjx-container[jax="SVG"][justify="left"] {
  text-align: left;
}

mjx-container[jax="SVG"][justify="right"] {
  text-align: right;
}

g[data-mml-node="merror"] > g {
  fill: red;
  stroke: red;
}

g[data-mml-node="merror"] > rect[data-background] {
  fill: yellow;
  stroke: none;
}

g[data-mml-node="mtable"] > line[data-line] {
  stroke-width: 70px;
  fill: none;
}

g[data-mml-node="mtable"] > rect[data-frame] {
  stroke-width: 70px;
  fill: none;
}

g[data-mml-node="mtable"] > .mjx-dashed {
  stroke-dasharray: 140;
}

g[data-mml-node="mtable"] > .mjx-dotted {
  stroke-linecap: round;
  stroke-dasharray: 0,140;
}

g[data-mml-node="mtable"] > svg {
  overflow: visible;
}

[jax="SVG"] mjx-tool {
  display: inline-block;
  position: relative;
  width: 0;
  height: 0;
}

[jax="SVG"] mjx-tool > mjx-tip {
  position: absolute;
  top: 0;
  left: 0;
}

mjx-tool > mjx-tip {
  display: inline-block;
  padding: .2em;
  border: 1px solid #888;
  font-size: 70%;
  background-color: #F8F8F8;
  color: black;
  box-shadow: 2px 2px 5px #AAAAAA;
}

g[data-mml-node="maction"][data-toggle] {
  cursor: pointer;
}

mjx-status {
  display: block;
  position: fixed;
  left: 1em;
  bottom: 1em;
  min-width: 25%;
  padding: .2em .4em;
  border: 1px solid #888;
  font-size: 90%;
  background-color: #F8F8F8;
  color: black;
}

foreignObject[data-mjx-xml] {
  font-family: initial;
  line-height: normal;
  overflow: visible;
}

.MathJax path {
  stroke-width: 3;
}

    #setText > div {
        justify-content: inherit;
        margin-top: 0;
        margin-bottom: 1em;
        
        
    }
    
    
    
    #setText div:last-child {
        margin-bottom: 0 !important;
    }

    #setText > br, #preview-content br {
        line-height: 1.2;
    }

    #preview-content > div {
        margin-top: 0;
        margin-bottom: 1em;
        
    }    
    
    .proof > div, .theorem > div {
        margin-top: 1rem;
    }

    #preview-content table {
      margin-bottom: 1em;
    }

    #setText table {
      margin-bottom: 1em;
    }
    
    #preview-content .sub-table table, #setText .sub-table table {
      margin-bottom: 0;
    }

    mjx-container {
      text-indent: 0;
      overflow-y: visible !important;
      padding-top: 1px;
      padding-bottom: 1px;
      
      
    }
    
    
    
    .math-inline mjx-container {
        display: inline-block !important;
        page-break-inside: avoid;
    }
    .math-block {
        align-items: center;
        min-width: min-content;
        page-break-after: auto;
        page-break-inside: avoid;
        margin-top: 1em;
        margin-bottom: 1em;
    }
    
    .math-block[data-highlight-color] mjx-container[jax="SVG"] > svg {
      background-color: var(--mmd-highlight-color);
    }    
    
    .math-block[data-highlight-text-color] mjx-container[jax="SVG"] > svg {
      color: var(--mmd-highlight-text-color);
    }    
    .math-inline[data-highlight-color] mjx-container[jax="SVG"] {
      background-color: var(--mmd-highlight-color);
    }    
    
    .math-inline[data-highlight-text-color] mjx-container[jax="SVG"] {
      color: var(--mmd-highlight-text-color);
    }
    
    .math-block p {
        flex-shrink: 1;
    }
    .math-block mjx-container {
        margin: 0 !important;
    }
    .math-error {
        background-color: yellow;
        color: red;
    }

    #preview-content svg, #setText svg { min-width: initial !important;}

    #preview-content img, #setText img {
        max-width: 100%;
    }
    
    #preview-content blockquote,  #setText blockquote {
        page-break-inside: avoid;
        color: #666;
        margin: 0 0 1em 0;
        padding-left: 3em;
        border-left: .5em solid #eee;
    }

    #preview-content pre, #setText pre {
        border: none;
        padding: 0;
        overflow: auto;
        font-size: 85%;
        line-height: 1.45;
        border-radius: 6px;
        box-sizing: border-box;
        background: #f8f8fa;
    }
    #preview-content pre code, #setText pre code{
        padding: 1rem;
        display: block;
        overflow-x: auto;
        line-height: 24px;
    }
    .empty {
        text-align: center;
        font-size: 18px;
        padding: 50px 0 !important;
    }

    #setText table, #preview-content table {
        display: table; 
        overflow: auto;
        max-width: 100%;
        border-collapse: collapse;
        page-break-inside: avoid;
    }
      
    #setText table th, #preview-content table th {
        text-align: center;
        font-weight: bold;
    }
    
    #setText table td, #preview-content table td,
    #setText table th, #preview-content table th {
        border: 1px solid #dfe2e5;
        padding: 6px 13px;
    }
      
    #setText table tr, #preview-content table tr {
        background-color: #fff;
        border-top: 1px solid #c6cbd1;
    }
    
    #setText table tr:nth-child(2n), #preview-content table tr:nth-child(2n) {
        background-color: #f6f8fa;
    }

    
    #setText .main-title, #setText .author, #preview-content .main-title, #preview-content .author  {
        text-align: center;
        margin: 0 auto;
    }
    
    #preview-content .main-title, #setText .main-title {
        line-height: 1.2;
        margin-bottom: 1em;
    }

    #preview-content .author, #setText .author  {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    #preview-content .author p, #setText .author p {
        min-width: 30%;
        max-width: 50%;
        padding: 0 7px;
    }

    #preview-content .author > p > span, #setText .author > p > span {
        display: block;
        text-align: center;
    }

    #preview-content .section-title, #setText .section-title {
        margin-top: 1.5em;
    }

    #preview-content .abstract, #setText .abstract {
        text-align: justify;
        margin-bottom: 1em;
    }

    #preview-content .abstract p, #setText .abstract p {
        margin-bottom: 0;
    }

    @media print {

      #preview {
        font-size: 10pt!important;
      }

      svg {
        shape-rendering: crispEdges;
      }

      .math-block svg, math-inline svg {
        margin-top: 1px;
      }

      #preview-content img, #setText img {
        display: block;
      }
      
      #preview-content .figure_img img, #setText .figure_img img {
        display: inline;
      }

      .preview-right {
        word-break: break-word;
      }

      #preview-content h1, #setText h1 {
        page-break-inside: avoid;
        position: relative;
        border: 2px solid transparent;
      }
  
      #preview-content h1::after, #setText h1::after {
        content: "";
        display: block;
        height: 100px;
        margin-bottom: -100px;
        position: relative;
      }
  
      #preview-content h2, #setText h2 {
        page-break-inside: avoid;
        position: relative;
        border: 2px solid transparent;
      }
  
      #preview-content h2::after, #setText h2::after {
        content: "";
        display: block;
        height: 100px;
        margin-bottom: -100px;
        position: relative;
      }
  
      #preview-content h3, #setText h3 {
        page-break-inside: avoid;
        position: relative;
        border: 2px solid transparent;
      }
  
      #preview-content h3::after, #setText h3::after {
        content: "";
        display: block;
        height: 100px;
        margin-bottom: -100px;
        position: relative;
      }
  
      #preview-content h4, #setText h4 {
        page-break-inside: avoid;
        position: relative;
        border: 2px solid transparent;
      }
  
      #preview-content h4::after, #setText h4::after {
        content: "";
        display: block;
        height: 100px;
        margin-bottom: -100px;
        position: relative;
      }
  
      #preview-content h5, #setText h5 {
        page-break-inside: avoid;
        position: relative;
        border: 2px solid transparent;
      }
  
      #preview-content h5::after, #setText h5::after {
        content: "";
        display: block;
        height: 100px;
        margin-bottom: -100px;
        position: relative;
      }
  
      #preview-content h6, #setText h6 {
        page-break-inside: avoid;
        position: relative;
        border: 2px solid transparent;
      }
  
      #preview-content h6::after, #setText h6::after {
        content: "";
        display: block;
        height: 100px;
        margin-bottom: -100px;
        position: relative;
      }
    }
    #preview-content sup, #setText sup {
      top: -.5em;
      position: relative;
      font-size: 75%;
      line-height: 0;
      vertical-align: baseline;
    }
    
    #preview-content .text-url, #setText .text-url {
      color: #0B93ff;
      cursor: text;
      pointer-events: none;
    }
    
    #preview-content .text-url a:hover, #setText .text-url a:hover {
      color: #0B93ff;
    }
    
    mark {
      background-color: #feffe6;
    }
    
    span[data-underline-type] mark {
      background: inherit;
      background-color: #feffe6;
      padding-top: 0;
      padding-bottom: 0;
    }
    
    *[data-has-dotfill] {
      position: relative;
      overflow: hidden;
    }
    
    *[data-has-dotfill] .dotfill::after {
      position: absolute;
      padding-left: .25ch;
      content: " . . . . . . . . . . . . . . . . . . . "
          ". . . . . . . . . . . . . . . . . . . . . . . "
          ". . . . . . . . . . . . . . . . . . . . . . . "
          ". . . . . . . . . . . . . . . . . . . . . . . "
          ". . . . . . . . . . . . . . . . . . . . . . . "
          ". . . . . . . . . . . . . . . . . . . . . . . "
          ". . . . . . . . . . . . . . . . . . . . . . . ";
      text-align: right;
    }

    #preview-content code, #setText code {
      font-family: Inconsolata;
      font-size: inherit;
      display: initial;
      background: #f8f8fa;
    }
    #preview-content .mmd-highlight code, #setText .mmd-highlight code, 
    #preview-content pre.mmd-highlight code, #setText pre.mmd-highlight code {
      background-color: transparent;
    }
    #preview-content pre code, #setText pre code {
      font-family: 'DM Mono', Inconsolata, monospace;
      color: #333;
      font-size: 15px;
    }

    .hljs-comment,
    .hljs-quote {
      color: #998;
      font-style: italic;
    }

    .hljs-command {
      color: #005cc5;
    }

    .hljs-keyword,
    .hljs-selector-tag,
    .hljs-subst {
      color: #d73a49;
      font-weight: bold;
    }

    .hljs-number,
    .hljs-literal,
    .hljs-variable,
    .hljs-template-variable,
    .hljs-tag .hljs-attr {
      color: #005cc5;
    }

    .hljs-string,
    .hljs-doctag {
      color: #24292e;
    }

    .hljs-title,
    .hljs-section,
    .hljs-selector-id {
      color: #6f42c1;
      font-weight: bold;
    }

    .hljs-subst {
      font-weight: normal;
    }

    .hljs-type,
    .hljs-class .hljs-title {
      color: #458;
      font-weight: bold;
    }

    .hljs-tag,
    .hljs-name,
    .hljs-attribute {
      color: #000080;
      font-weight: normal;
    }

    .hljs-regexp,
    .hljs-link {
      color: #009926;
    }

    .hljs-symbol,
    .hljs-bullet {
      color: #990073;
    }

    .hljs-built_in,
    .hljs-builtin-name {
      color: #24292e;
    }

    .hljs-meta {
      color: #999;
      font-weight: bold;
    }

    .hljs-meta-keyword {
      color: #d73a49;
    }

    .hljs-meta-string {
      color: #032f62;
    }

    .hljs-deletion {
      background: #fdd;
    }

    .hljs-addition {
      background: #dfd;
    }

    .hljs-emphasis {
      font-style: italic;
    }

    .hljs-strong {
      font-weight: bold;
    }

    .table_tabular table th,  .table_tabular table th {
        border: none !important;
        padding: 6px 13px;
    }
      
    #tabular tr, #tabular tr {
        border-top: none !important;
        border-bottom: none !important;
    }
    #tabular td, #tabular td {
        border-style: none !important;
        background-color: #fff;
        border-color: #000 !important;
        word-break: keep-all;
        padding: 0.1em 0.5em !important;
    }
    #tabular {
        display: inline-block !important;
    }
    #tabular td > p {
        margin-bottom: 0;
        margin-top: 0;
    }
    #tabular td._empty {
      height: 1.3em;
    }
    #tabular td .f {
      opacity: 0;
    }
    
    html[data-theme="dark"] #tabular tr, html[data-theme="dark"] #tabular td {
      background-color: #202226;
      border-color: #fff !important;
    }  
    .table_tabular {
        overflow-x: auto;
        padding: 0 2px 0.5em 2px;
    }
    .figure_img {
       margin-bottom: 0.5em;
       overflow-x: auto;
    }

  ol.enumerate, ul.itemize {
    padding-inline-start: 40px;
  }
/* It's commented because counter not supporting to change value 
  ol.enumerate.lower-alpha {
    counter-reset: item ;
    list-style-type: none !important;
  }
  .enumerate.lower-alpha > li {
    position: relative;
  }
  .enumerate.lower-alpha > li:before { 
    content: "("counter(item, lower-alpha)")"; 
    counter-increment: item; 
    position: absolute;
    left: -47px;
    width: 47px;
    display: flex;
    justify-content: flex-end;
    padding-right: 7px;
    flex-wrap: nowrap;
    word-break: keep-all;
  }
  */
  
  .itemize > li {
    position: relative;
  }
  .itemize > li > span.li_level, .li_enumerate.not_number > span.li_level { 
    position: absolute;
    right: 100%;
    white-space: nowrap;
    width: max-content;
    display: flex;
    justify-content: flex-end;
    padding-right: 10px;
    box-sizing: border-box;
  }
  .li_enumerate.not_number {
    position: relative;
    display: inline-block;
    list-style-type: none;
  }

  #preview {
    font-family: 'CMU Serif', 'Georgia', Helvetica, Arial, sans-serif;
    font-size: 17px;
    visibility: visible;
    word-break: break-word;
    padding: 2.5em;
    /*max-width: 800px;*/
    margin: auto;
    box-sizing: content-box;
  }

  #preview h1, #preview h2, #preview h3, #preview h4, #preview h5, #preview strong {
    font-family: 'CMU Serif Bold', 'Georgia', Helvetica, Arial, sans-serif;
  }

  #preview  i, #preview  em {
    font-family: 'CMU Serif Italic', 'Georgia', Helvetica, Arial, sans-serif;
  }

  .mmd-menu {
    max-width: 320px;
    position: absolute;
    background-color: white;
    color: black;
    width: auto;
    padding: 5px 0px;
    border: 1px solid #E5E6EB;
    margin: 0;
    cursor: default;
    font: menu;
    text-align: left;
    text-indent: 0;
    text-transform: none;
    line-height: normal;
    letter-spacing: normal;
    word-spacing: normal;
    word-wrap: normal;
    white-space: nowrap;
    float: none;
    z-index: 201;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -khtml-border-radius: 5px;
    box-shadow: 0px 10px 20px #808080;
    -webkit-box-shadow: 0px 10px 20px #808080;
    -moz-box-shadow: 0px 10px 20px #808080;
    -khtml-box-shadow: 0px 10px 20px #808080; 
  }
  
  .mmd-menu:focus { outline: none; }
  
  .mmd-menu.mmd-menu-sm {
    max-width: 100vw;
    padding-bottom: 34px;
    border-radius: 0;
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    -khtml-border-radius: 0;
  }

  .mmd-menu-item-icon {
    color: #1e2029;
    margin-left: auto;
    align-items: center;
    display: flex;
    flex-shrink: 0;
    display: none; 
  }

  .mmd-menu-item {
    padding-bottom: 8px;
    padding-top: 8px;
    padding-left: 1.25rem;
    padding-right: 1.25rem;
    display: flex;
    background: transparent; 
    height: 52px;
    max-height: 52px;
  }
  .mmd-menu-item:focus { outline: none; }

  .mmd-menu-item.active {
    background-color: #e1e0e5; 
  }

  .mmd-menu-item.active .mmd-menu-item-icon {
    display: flex; 
  }

  .mmd-menu-item-container {
    overflow: hidden; 
  }

  .mmd-menu-item-title {
    color: #1e2029;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    font-size: 14px;
    line-height: 20px; 
  }

  .mmd-menu-item-value {
    color: #7d829c;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    font-size: 12px;
    line-height: 16px; 
  }
  
  html[data-theme="dark"] .mmd-menu-item-title {
    color: #ebefe7;
  } 
  html[data-theme="dark"] .mmd-menu-item.active .mmd-menu-item-title {
    color: #1e2029;
  }
  html[data-theme="dark"] .mmd-menu {
    background-color: #33363a;
  }
  
  .mmd-context-menu-overlay{
    background: rgba(0, 0, 0, 0.56);
  }
  
.ClipboardButton {
  padding: 0;
  margin: 0.5rem;
  display: inline-block;
  cursor: pointer;
  color: rgb(36, 41, 47);
  background: rgb(246, 248, 250);
  border-radius: 6px;
  border: 1px solid rgba(31, 35, 40, 0.15);
  box-shadow: rgba(31, 35, 40, 0.04) 0 1px 0 0, rgba(255, 255, 255, 0.25) 0 1 0 0 inset;
  position: relative;
}

.ClipboardButton:hover {
  background-color: rgb(243, 244, 246);
  border-color: rgba(31, 35, 40, 0.15);
  transition-duration: .1s;
}

.mmd-clipboard-icon {
  fill: currentColor;
  vertical-align: text-bottom;
}

.mmd-clipboard-copy-icon {
  color: rgb(101, 109, 118);
}
.mmd-clipboard-check-icon {
  color: rgb(26, 127, 55);
}

.mmd-tooltipped-no-delay:hover::before,
.mmd-tooltipped-no-delay:hover::after {
  animation-delay: 0s;
}

.mmd-tooltipped:hover::before,
.mmd-tooltipped:hover::after {
  display: inline-block;
  text-decoration: none;
  animation-name: tooltip-appear;
  animation-duration: .1s;
  animation-fill-mode: forwards;
  animation-timing-function: ease-in;
  animation-delay: .4s;
}

.mmd-tooltipped-w::before {
  top: 50%;
  bottom: 50%;
  left: -7px;
  margin-top: -6px;
  border-left-color: rgb(36, 41, 47)
}

.mmd-tooltipped::before {
  position: absolute;
  z-index: 1000001;
  display: none;
  width: 0;
  height: 0;
  color: rgb(36, 41, 47);
  pointer-events: none;
  content: "";
  border: 6px solid transparent;
  opacity: 0;
}

.mmd-tooltipped-w::after {
  right: 100%;
  bottom: 50%;
  margin-right: 6px;
  transform: translateY(50%);
}


.mmd-tooltipped::after {
    position: absolute;
    z-index: 1000000;
    display: none;
    padding: 0.5em 0.75em;
    font: normal normal 11px/1.5 'CMU Serif', 'Georgia', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: subpixel-antialiased;
    color: rgb(255, 255, 255);
    text-align: center;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-wrap: break-word;
    white-space: pre;
    pointer-events: none;
    content: attr(aria-label);
    background: rgb(36, 41, 47);
    border-radius: 6px;
    opacity: 0;
}
  .page-break {
    display: none !important;
  }
  
  .cheatsheet-table td:first-child, .cheatsheet-table th:first-child {
    white-space: nowrap;         /* Pas de retour à la ligne automatique */
    max-width: 1px;              /* Laisse la colonne prendre toute la place nécessaire */
    overflow-x: auto;            /* Ajoute une barre de scroll si la commande est trop longue */
    font-family: monospace;      /* Pour l’aspect commande */
    background: #f5f5f5;
}
.cheatsheet-table {
    width: 100%;
    border-collapse: collapse;
}
.cheatsheet-table td, .cheatsheet-table th {
    border: 1px solid #ccc;
    padding: 6px 10px;
}

.commands-cell {
  white-space: nowrap;         /* Pas de retour à la ligne automatique */
  /*
  max-width: 1px;              /* Laisse la colonne prendre toute la place nécessaire */
  overflow-x: auto;            /* Ajoute une barre de scroll si la commande est trop longue */
  font-family: monospace;      /* Pour l’aspect commande */
  */
}
  
  </style>
    </head>
    <body>
        <div id="preview" class="preview scrollEditor">
            <div id="container-ruler"></div>
            <div id="preview-content">
                <div id="container-ruler"></div>
                <div id="preview-content" class="preview-content-note">
                    <div class="center preview-paragraph-0 preview-line 0 1 2" style="text-align: center"><strong>{{ title }}</strong></div>
                    <table align="center">
                        <thead>
                        <tbody>
                            {% for cmd in commands %}
                                <tr>
                                    <td class="commands-cell"><code>{{ cmd['commande'] }}</code></td>
                                    <td>{{ cmd['description'] }}</td>
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    #print(title, commands)

    # Créer un objet Template Jinja2
    template = Template(html_template)

    # Remplacer les placeholders dans le template avec les données
    html_content = template.render(title=title, commands=commands)

    # Enregistrez le contenu HTML dans un fichier ou imprimez-le selon vos besoins
    with open("output.html", 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

def save_html(html_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    # Vérifier s'il y a au moins un argument
    if len(sys.argv) < 2:
        print("Erreur : Veuillez fournir le nom du fichier markdown en argument.")
        print("Exemple : ./convert2html.py multipass.md")
        sys.exit(1)  # Quitter le programme avec un code d'erreur

    # Récupérer le chemin du fichier à partir des arguments de la ligne de commande
    file_path = sys.argv[1]

    # Exécuter le reste du code avec le chemin du fichier
    title, commands = process_markdown_file(file_path)
    generate_html(title, commands)
    
