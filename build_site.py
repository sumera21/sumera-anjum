#!/usr/bin/env python3
"""Generate static HTML for Sumera Anjum's GitHub Pages site.

No dependencies. Run `python3 build_site.py` from this directory to rebuild.
Edit the page content, publication records, and news items below.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
BASE = 'https://sumera21.github.io/sumera-anjum/'
EMAIL = 'sumeraanjum@my.unt.edu'  # Corrected from the duplicated address in older HTML/PDF.
SCHOLAR = 'https://scholar.google.com/citations?user=a0jfZgEAAAAJ&hl=en'
GITHUB = 'https://github.com/sumera21'
LINKEDIN = 'https://www.linkedin.com/in/sumera-anjum-30345b1b0/'
CV_PDF = 'files/Sumera_Anjum_CV.pdf'

NAV = [
    ('index.html', 'About'), ('research.html', 'Research'),
    ('publications.html', 'Publications'), ('teaching.html', 'Teaching'),
    ('talks.html', 'Talks'), ('service.html', 'Service'),
    ('news.html', 'News'), ('cv.html', 'CV'),
]

PAPERS = [
    dict(id='poly-fever', year=2026, date='Oct 2026', title='Poly-FEVER: A Multilingual Hallucination Detection Benchmark',
         authors='Hanzhi Zhang, Sumera Anjum, Heng Fan, Weijian Zheng, Yan Huang, Yunhe Feng',
         venue='Findings of EMNLP 2026',
         links=[('Paper','https://aclanthology.org/2026.findings-emnlp.540/'), ('Dataset','https://huggingface.co/datasets/HanzhiZhang/Poly-FEVER')],
         abstract='Poly-FEVER is a multilingual fact-verification benchmark containing 77,973 supported and refuted claims aligned across 11 languages. It evaluates how factuality judgments and hallucination detection vary across languages, model families, and prompting strategies.',
         bib='''@inproceedings{zhang-etal-2026-poly,\n  title={Poly-{FEVER}: A Multilingual Hallucination Detection Benchmark},\n  author={Zhang, Hanzhi and Anjum, Sumera and Fan, Heng and Zheng, Weijian and Huang, Yan and Feng, Yunhe},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2026},\n  year={2026},\n  pages={11353--11369},\n  doi={10.18653/2026.findings-emnlp.540},\n  url={https://aclanthology.org/2026.findings-emnlp.540/}\n}'''),
    dict(id='beyond-vibe-coding', year=2026, date='2026 · forthcoming', title='Beyond Vibe Coding: Unified Multi-Framework Quantum Code Generation and Execution-Aware Evaluation with LLMs',
         authors='Sumera Anjum, Xiaokun Yang, Thomas Gerrity, Junhua Ding, Kewei Sha, Weijian Zheng, Song Fu, Antonio Paes, Yunhe Feng',
         venue='IEEE International Conference on Quantum Artificial Intelligence (QAI 2026) · Accepted',
         links=[],
         abstract='This work investigates quantum code generation with language models across PennyLane, Qiskit, and OpenQASM, using execution-aware evaluation to assess whether generated programs run and produce the intended quantum-state behavior.',
         bib='''@inproceedings{anjum2026beyondvibe,\n  title={Beyond Vibe Coding: Unified Multi-Framework Quantum Code Generation and Execution-Aware Evaluation with LLMs},\n  author={Anjum, Sumera and Yang, Xiaokun and Gerrity, Thomas and Ding, Junhua and Sha, Kewei and Zheng, Weijian and Fu, Song and Paes, Antonio and Feng, Yunhe},\n  booktitle={IEEE International Conference on Quantum Artificial Intelligence (QAI)},\n  year={2026}\n}'''),
    dict(id='quantum-hardware', year=2026, date='2026 · forthcoming', title='LLM-Driven Hardware Design for Quantum Simulation Acceleration',
         authors='Krishna Patel, Sumera Anjum, Spencer Buchanan, Xuechen Zhang, Yunhe Feng, Xiaokun Yang',
         venue='IEEE BigData 2026 · Undergraduate and REU Consortium',
         links=[],
         abstract='A research collaboration exploring language-model-assisted generation and evaluation of hardware designs for quantum simulation. The work evaluates proposed circuits and compares their behavior against reference designs.',
         bib='''@inproceedings{patel2026hardware,\n  title={LLM-Driven Hardware Design for Quantum Simulation Acceleration},\n  author={Patel, Krishna and Anjum, Sumera and Buchanan, Spencer and Zhang, Xuechen and Feng, Yunhe and Yang, Xiaokun},\n  booktitle={IEEE BigData Undergraduate and REU Consortium},\n  year={2026}\n}'''),
    dict(id='promcp', year=2026, date='Jul 2026', title='ProMCP: Profiling Token Flows and Latency Costs in Model Context Protocol–Based LLM Agents',
         authors='Sumera Anjum, Weijian Zheng, Rajkumar Kettimuthu, Heng Fan, Yunhe Feng',
         venue='Findings of ACL 2026 · Oral Presentation',
         links=[('Paper','https://aclanthology.org/2026.findings-acl.1967/'), ('Code','https://github.com/ResponsibleAILab/ProMCP')],
         abstract='ProMCP profiles token usage and latency throughout a six-stage Model Context Protocol pipeline, studying 20 MCP servers and 169 tools across local, cloud, and off-the-shelf agent configurations. It identifies orchestration and answer synthesis as significant cost drivers.',
         bib='''@inproceedings{anjum-etal-2026-promcp,\n  title={Pro{MCP}: Profiling Token Flows and Latency Costs in Model Context Protocol--Based {LLM} Agents},\n  author={Anjum, Sumera and Zheng, Weijian and Kettimuthu, Rajkumar and Fan, Heng and Feng, Yunhe},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},\n  year={2026},\n  pages={39476--39487},\n  doi={10.18653/v1/2026.findings-acl.1967},\n  url={https://aclanthology.org/2026.findings-acl.1967/}\n}'''),
    dict(id='halo', year=2025, date='Jun 2025', title='HALO: Hallucination Analysis and Learning Optimization to Empower LLMs with Retrieval-Augmented Context for Guided Clinical Decision Making',
         authors='Sumera Anjum, Hanzhi Zhang, Wenjun Zhou, Eun Jin Paek, Xiaopeng Zhao, Yunhe Feng',
         venue='IEEE/ACM CHASE 2025',
         links=[('Paper','https://arxiv.org/abs/2409.10011'), ('Code','https://github.com/ResponsibleAILab/HALO')],
         abstract='HALO combines external retrieval, query variation, and maximum marginal relevance to improve the reliability of large language models for clinical question answering. It is evaluated on MedMCQA and studies the effect of retrieved context on hallucinations.',
         bib='''@inproceedings{anjum2025halo,\n  title={HALO: Hallucination Analysis and Learning Optimization to Empower LLMs with Retrieval-Augmented Context for Guided Clinical Decision Making},\n  author={Anjum, Sumera and Zhang, Hanzhi and Zhou, Wenjun and Paek, Eun Jin and Zhao, Xiaopeng and Feng, Yunhe},\n  booktitle={2025 IEEE/ACM Conference on Connected Health: Applications, Systems and Engineering Technologies (CHASE)},\n  pages={187--198},\n  year={2025},\n  organization={IEEE}\n}''')
]

NEWS = [
 ('Nov 2026','Delivered a guest lecture on token economics, LLM inference, and MCP for students in Introduction to Artificial Intelligence at UNT Frisco.'),
 ('Oct 2026','Joined Argonne National Laboratory as a Visiting Student in Data Science and Learning.'),
 ('Oct 2026','<strong>Beyond Vibe Coding</strong> accepted to IEEE QAI 2026.'),
 ('Oct 2026','<a href="https://aclanthology.org/2026.findings-emnlp.540/">Poly-FEVER</a> published in Findings of EMNLP 2026.'),
 ('Summer 2026','Mentored REU student Krishna Patel on LLM-driven hardware design for quantum simulation acceleration.'),
 ('Jul 2026','Presented <a href="https://aclanthology.org/2026.findings-acl.1967/">ProMCP</a> at ACL Findings 2026 in San Diego, California.'),
 ('Jul 2026','Received the UNT Graduate Student Travel Award (Summer 2026).'),
 ('Jun 2026','Gave an REU research talk on ProMCP at the University of North Texas.'),
 ('Aug 2025','Began PhD study in Computer Science at UNT.'),
 ('Jun 2025','Presented HALO at IEEE/ACM CHASE 2025 in New York.'),
 ('Jun 2025','Received the NSF Student Travel Award for IEEE/ACM CHASE 2025.'),
 ('May 2025','Received the Distinguished Graduate Student Award and completed an MS in Computer Science at UNT with a 4.0 GPA.'),
]

def page(title, filename, body, desc='Research and academic profile of Sumera Anjum at the University of North Texas.'):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url==filename else '')+f'>{label}</a>' for url,label in NAV)
    metadata = escape(desc, quote=True)
    full_title = f'{escape(title)} | Sumera Anjum' if title!='About' else 'Sumera Anjum | PhD Researcher, University of North Texas'
    canonical = BASE + ('' if filename=='index.html' else filename)
    full = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{metadata}">
  <meta name="theme-color" content="#0d716e">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(full_title, quote=True)}">
  <meta property="og:description" content="{metadata}">
  <meta property="og:url" content="{canonical}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="app.js" defer></script>
  <title>{full_title}</title>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Person","name":"Sumera Anjum","url":"{BASE}","jobTitle":"PhD Researcher","affiliation":{{"@type":"CollegeOrUniversity","name":"University of North Texas"}},"sameAs":["{SCHOLAR}","{GITHUB}","{LINKEDIN}"]}}</script>
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header"><div class="header-inner">
    <a class="brand" href="index.html">Sumera Anjum<span class="brand-dot">.</span></a>
    <nav class="primary-nav" id="primary-nav" aria-label="Main navigation">{nav}</nav>
    <div class="header-tools">
      <button class="icon-btn" data-open-search type="button" aria-label="Search the website">Search <span aria-hidden="true">⌘K</span></button>
      <button class="icon-btn menu-btn" data-menu-toggle aria-controls="primary-nav" aria-expanded="false" type="button">Menu</button>
    </div>
  </div></header>
  <div class="shell">
    <aside class="sidebar" aria-label="Academic profile">
      <img class="avatar" src="images/SAnjum.png" alt="Portrait of Sumera Anjum" width="156" height="156">
      <div><h2 class="side-name">Sumera Anjum</h2><p class="side-role">PhD Student in Computer Science<br>Responsible AI Lab · UNT<br>Visiting Student · Argonne</p></div>
      <ul class="sidebar-list">
        <li><span class="side-symbol" aria-hidden="true">⌖</span> Denton, Texas</li>
        <li><span class="side-symbol" aria-hidden="true">✉</span> <a href="mailto:{EMAIL}">Email</a></li>
        <li><span class="side-symbol" aria-hidden="true">↗</span> <a href="{SCHOLAR}" target="_blank" rel="noopener noreferrer">Google Scholar</a></li>
      </ul>
      <div class="sidebar-links" aria-label="Profile links">
        <a href="{GITHUB}" target="_blank" rel="noopener noreferrer">GitHub</a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="{CV_PDF}" target="_blank" rel="noopener noreferrer">CV PDF ↗</a>
      </div>
    </aside>
    <main class="content" id="main-content">
{body}
      <footer class="site-footer"><span>© 2026 Sumera Anjum · Built for GitHub Pages</span><span><a href="mailto:{EMAIL}">Email</a> · <a href="{SCHOLAR}">Scholar</a> · <a href="{LINKEDIN}">LinkedIn</a></span></footer>
    </main>
  </div>
  <dialog class="search-dialog" id="site-search" aria-label="Search site">
    <div class="search-top"><input id="site-search-input" type="search" placeholder="Search publications, research, pages…" aria-label="Search query"><button data-close-search type="button" aria-label="Close search">Esc</button></div>
    <div class="search-results" id="site-search-results"></div>
    <p class="search-hint">Search across pages and key research topics · Ctrl/⌘ + K</p>
  </dialog>
</body></html>
'''
    (ROOT / filename).write_text(full, encoding='utf-8')


def heading(title, subtitle):
    return f'<div class="page-heading"><p class="eyebrow">Sumera Anjum · Academic profile</p><h1>{title}</h1><p>{subtitle}</p></div>'


def paper(p):
    link_markup = ''.join(f'<a class="pub-link" href="{escape(url,quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)} ↗</a>' for label,url in p['links'])
    ident = p['id']
    authors = escape(p['authors']).replace('Sumera Anjum','<strong>Sumera Anjum</strong>',1)
    abstract = escape(p['abstract'])
    bib = escape(p['bib'])
    return f'''<article class="publication" id="{ident}" data-publication data-year="{p['year']}" data-search="{escape(p['title']+' '+p['authors']+' '+p['venue']+' '+str(p['year']),quote=True)}">
  <div class="pub-date">{escape(p['date'])}</div>
  <div class="pub-content"><h3>{escape(p['title'])}</h3><p class="authors">{authors}</p><p class="venue">{escape(p['venue'])}</p>
  <div class="pub-tools">{link_markup}
    <details class="pub-details"><summary>Abstract</summary><div class="pub-panel"><p>{abstract}</p></div></details>
    <details class="pub-details"><summary>BibTeX</summary><div class="pub-panel"><button class="copy-btn" type="button" data-copy-target="bib-{ident}" aria-label="Copy BibTeX for {escape(p['title'],quote=True)}">Copy citation</button><pre id="bib-{ident}" class="bibtex">{bib}</pre></div></details>
  </div></div></article>'''


def detail(title,meta,body):
    return f'<article class="detail-card"><h3>{title}</h3><p class="detail-meta">{meta}</p>{body}</article>'


# -------------------- ABOUT (homepage) --------------------
home = '''<div class="hero">
  <p class="eyebrow">Computer Science · Responsible AI · University of North Texas</p>
  <h1 class="hero-title">Toward AI worth trusting.</h1>
  <p class="lead">I am <strong>Sumera Anjum</strong>, a PhD student in Computer Science at the <a href="https://computerscience.engineering.unt.edu/">University of North Texas</a>, advised by <a href="https://yunhefeng.me/">Dr. Yunhe Feng</a> in the <a href="https://yunhefeng.me/lab/">Responsible AI Lab</a>. My work explores trustworthy language models, agentic AI and the Model Context Protocol (MCP), and generative AI for quantum computing.</p>
  <p>I am also a Visiting Student in Data Science and Learning at <a href="https://www.anl.gov/">Argonne National Laboratory</a>, studying how to make LLM-based systems more resource-efficient.</p>
  <div class="chips"><span class="chip">Trustworthy LLMs</span><span class="chip">Agentic AI & MCP</span><span class="chip">LLM Inference Cost</span><span class="chip">Quantum AI</span></div>
  <div class="actions"><a class="btn" href="publications.html">Explore publications →</a><a class="btn btn-outline" href="cv.html">View CV</a></div>
</div>
<section class="section" aria-labelledby="area-heading">
  <div class="section-header"><h2 id="area-heading">Research interests</h2><a href="research.html" class="text-link">All research →</a></div>
  <div class="cards">
    <article class="card"><p class="card-kicker">01 · Responsible AI</p><h3>Reliable & trustworthy language models</h3><p>Hallucination detection, multilingual fact verification, and grounding answers in evidence.</p></article>
    <article class="card"><p class="card-kicker">02 · AI Systems</p><h3>Agents, MCP & token economics</h3><p>Measuring where LLM agents spend tokens, time, and API cost across tool workflows.</p></article>
    <article class="card"><p class="card-kicker">03 · Quantum AI</p><h3>Generative AI for quantum computing</h3><p>Generating quantum programs and evaluating them by execution and state fidelity.</p></article>
    <article class="card"><p class="card-kicker">04 · AI for health</p><h3>Retrieval-augmented clinical QA</h3><p>Using retrieved evidence to reduce hallucinations in medical question answering.</p></article>
  </div>
</section>
<section class="section" aria-labelledby="selected-pubs">
  <div class="section-header"><h2 id="selected-pubs">Selected publications</h2><a href="publications.html" class="text-link">Full list →</a></div>
'''
for item in ['promcp', 'poly-fever', 'beyond-vibe-coding']:
    home += paper(next(p for p in PAPERS if p['id']==item))
home += '''</section>
<section class="section" aria-labelledby="latest-news"><div class="section-header"><h2 id="latest-news">Recent news</h2><a class="text-link" href="news.html">All updates →</a></div><ul class="news-list">'''
for date, info in NEWS[:5]:
    home += f'<li><time>{date}</time><span>{info}</span></li>'
home += '''</ul></section>
<section class="section"><h2>Background</h2>
<p>I completed my MS in Computer Science at UNT with a 4.0 GPA and received the 2024–2025 Distinguished Graduate Student Award. Before joining UNT, I earned my B.Tech in Computer Science from Sreenidhi Institute of Science and Technology in Hyderabad, India.</p>
<p>Outside research, I enjoy painting, henna art, learning languages, traveling, and experimenting with new recipes.</p></section>'''
page('About','index.html',home,'Sumera Anjum is a PhD researcher at UNT working on trustworthy LLMs, MCP agents, inference costs, hallucination detection and quantum AI.')

# -------------------- PUBLICATIONS --------------------
body = heading('Publications','Peer-reviewed research in trustworthy AI, LLM agents, and quantum computing. For the complete record, visit <a href="'+SCHOLAR+'">Google Scholar</a>.')
body += '''<div class="filters" role="search" aria-label="Filter publications">
  <input class="filter-input" id="publication-filter" type="search" placeholder="Search title, author, venue, or year…" aria-label="Search publications">
  <button class="filter-btn" data-year-filter="all" aria-pressed="true" type="button">All</button>
  <button class="filter-btn" data-year-filter="2026" aria-pressed="false" type="button">2026</button>
  <button class="filter-btn" data-year-filter="2025" aria-pressed="false" type="button">2025</button>
</div><p class="result-count" id="publication-count" role="status" aria-live="polite">5 publications shown</p>'''
body += ''.join(paper(p) for p in PAPERS)
body += '<p class="empty-state" id="publication-empty" hidden>No publications match your search. Try another keyword or year.</p>'
body += '<div class="callout"><p><strong>Ongoing manuscript:</strong> <em>Token Economics of Large Language Model Inference: Consumption, Cost, and Optimization</em> (survey manuscript; not listed as a peer-reviewed publication).</p></div>'
page('Publications','publications.html',body,'Publications by Sumera Anjum: ProMCP, Poly-FEVER, Beyond Vibe Coding, quantum hardware design, and HALO.')

# -------------------- RESEARCH --------------------
body = heading('Research','My work combines empirical measurement and evidence-based evaluation to make AI systems more reliable and more practical.')
body += '''<section class="section"><p class="eyebrow">Research direction 01</p><h2>Trustworthy and responsible language models</h2>
<p>How can language models distinguish supported facts from fluent but incorrect answers? My research studies multilingual factuality and retrieval-augmented question answering.</p>
<div class="cards">
  <article class="card"><p class="card-kicker">EMNLP Findings 2026</p><h3>Poly-FEVER</h3><p>A factuality benchmark across 11 languages, designed to study language-sensitive hallucination detection.</p><a href="publications.html#poly-fever">Publication & dataset →</a></article>
  <article class="card"><p class="card-kicker">CHASE 2025</p><h3>HALO</h3><p>Retrieval-augmented clinical QA that incorporates external evidence and query variation to improve answer reliability.</p><a href="publications.html#halo">Publication & code →</a></article>
</div></section>
<section class="section"><p class="eyebrow">Research direction 02</p><h2>Agentic AI, MCP and LLM inference cost</h2>
<p>Tool use introduces more than model inference time: schemas, planning, serialization, and answer synthesis all affect token consumption and latency. I investigate the costs of these interactions and opportunities for optimization.</p>
<div class="cards">
  <article class="card"><p class="card-kicker">ACL Findings 2026</p><h3>ProMCP</h3><p>Profiles the complete MCP workflow, with token-level and latency-level visibility across 20 servers and 169 tools.</p><a href="publications.html#promcp">Publication & source code →</a></article>
  <article class="card"><p class="card-kicker">Ongoing research</p><h3>Token economics of LLM inference</h3><p>Studying prefill, decoding, caching, context growth, and workload-aware strategies for reducing inference and agent costs.</p><a href="talks.html">Related lecture →</a></article>
</div></section>
<section class="section"><p class="eyebrow">Research direction 03</p><h2>Generative AI for quantum computing</h2>
<p>Quantum programs have structural and execution constraints that conventional code-generation benchmarks often overlook. I study multi-framework generation and execution-aware evaluation across quantum software stacks.</p>
<div class="cards">
  <article class="card"><p class="card-kicker">IEEE QAI 2026 · Accepted</p><h3>Beyond Vibe Coding</h3><p>Framework-spanning quantum code generation and execution-aware evaluation across PennyLane, Qiskit, and OpenQASM.</p><a href="publications.html#beyond-vibe-coding">Publication details →</a></article>
  <article class="card"><p class="card-kicker">IEEE BigData 2026</p><h3>Quantum simulation hardware design</h3><p>LLM-assisted exploration of hardware designs for quantum simulation, with execution and reference-based checking.</p><a href="publications.html#quantum-hardware">Publication details →</a></article>
</div></section>
<section class="section"><h2>Research affiliations</h2>
'''
body += detail('Responsible AI Lab · University of North Texas','Graduate Research Assistant · 2023–present','<p>PhD research under the supervision of <a href="https://yunhefeng.me/">Dr. Yunhe Feng</a>.</p>')
body += detail('Argonne National Laboratory · Data Science and Learning','Visiting Student · 2026','<p>Research collaboration focused on reducing the API and inference costs of LLM-based systems.</p>')
body += '</section>'
page('Research','research.html',body,'Research areas: hallucination detection, Poly-FEVER, ProMCP, MCP costs, quantum code generation, and retrieval-augmented clinical QA.')

# -------------------- TEACHING --------------------
body = heading('Teaching & Mentoring','Teaching experience, guest lectures, and undergraduate research mentorship.')
body += '<section class="section"><h2>Teaching experience</h2>'
body += detail('CSCE 4110 · Algorithms','Instructional Assistant · Summer 2026 · University of North Texas', '<p>Supported course delivery, student questions, and assessment in algorithms.</p>')
body += detail('CSCE 3550 · Foundations of Cybersecurity','Teaching Assistant · University of North Texas', '<p>Supported instruction, coursework, and student learning in cybersecurity foundations.</p>')
body += detail('CSCE 3530 · Computer Networks','Teaching Assistant · University of North Texas', '<p>Supported undergraduate networking instruction and course assessment.</p>')
body += detail('Additional teaching and instructional support','University of North Texas','<p>Experience with courses including Introduction to Big Data, Methods in Empirical Analysis, and Introduction to Computer Science.</p>')
body += '</section><section class="section"><h2>Guest lectures</h2>'
body += detail('Token Economics and Model Context Protocol (MCP)','November 12, 2026 · Introduction to Artificial Intelligence · UNT Frisco','<p>A guest lecture introducing the LLM inference lifecycle, prefill and decoding, KV caching, token costs, and tool-using agents.</p>')
body += '</section><section class="section"><h2>Mentorship</h2>'
body += detail('NSF Research Experiences for Undergraduates (REU)','Research Mentor · Summer 2026','<p>Mentored Krishna Patel on LLM-driven hardware design for quantum simulation acceleration, including circuit evaluation and manuscript development.</p>')
body += '</section>'
page('Teaching & Mentoring','teaching.html',body,'Teaching and mentoring by Sumera Anjum at UNT, including Algorithms, cybersecurity, networks and undergraduate research.')

# -------------------- TALKS --------------------
body = heading('Talks & Presentations','Selected invited lectures, conference talks, and research presentations.')
body += '<h2 class="year-heading">2026</h2><div class="timeline">'
body += '''<article class="timeline-entry"><time class="when">Nov 12, 2026 · UNT Frisco</time><h3>Token Economics and Model Context Protocol (MCP)</h3><p>Guest lecture for students in Introduction to Artificial Intelligence. Topics included LLM prefill, decode, KV cache, and token cost.</p></article>
<article class="timeline-entry"><time class="when">Jul 2026 · ACL Findings, San Diego</time><h3>ProMCP: Profiling Token Flows and Latency Costs in MCP-Based LLM Agents</h3><p>Oral presentation of our MCP instrumentation and performance findings. <a href="https://aclanthology.org/2026.findings-acl.1967/">Paper ↗</a></p></article>
<article class="timeline-entry"><time class="when">Jun 2026 · University of North Texas</time><h3>ProMCP: REU Research Talk</h3><p>Presentation for the undergraduate summer research program, introducing MCP and its token-flow and latency overheads.</p></article>'''
body += '</div><h2 class="year-heading">2025</h2><div class="timeline">'
body += '''<article class="timeline-entry"><time class="when">Jun 2025 · IEEE/ACM CHASE, New York</time><h3>HALO: Retrieval-Augmented Context for Guided Clinical Decision Making</h3><p>Conference presentation on retrieval-augmented clinical QA and hallucination analysis. <a href="https://arxiv.org/abs/2409.10011">Paper ↗</a></p></article></div>'''
page('Talks & Presentations','talks.html',body,'Talks by Sumera Anjum on token economics, MCP, ProMCP and clinical question answering.')

# -------------------- SERVICE --------------------
body = heading('Professional Service','Reviewing, workshop organization, and research community participation.')
body += '<section class="section"><h2>Conference & Workshop Organization</h2>'
body += detail('Web Chair · QISNet 2027','2026–2027','<p>Workshop web chair, supporting the dissemination of workshop information and online presence.</p>')
body += '</section><section class="section"><h2>Peer review</h2>'
body += detail('NeurIPS 2026','Conference reviewer · 2026','<p>Research paper reviewing for the Neural Information Processing Systems conference.</p>')
body += detail('IEEE GLOBECOM 2026 · CISS','External reviewer · 2026','<p>External reviewer in the conference review process.</p>')
body += detail('ACM CIKM','External reviewer · 2025 and 2026','<p>External reviewing for the ACM International Conference on Information and Knowledge Management.</p>')
body += '</section><div class="callout"><p>For the current, complete list of professional activities and reviewing assignments, see my <a href="cv.html">CV</a>.</p></div>'
page('Professional Service','service.html',body,'Professional service by Sumera Anjum: workshop web chair, NeurIPS, CIKM and GLOBECOM peer review.')

# -------------------- NEWS --------------------
body = heading('News','Research, teaching, awards, presentations, and milestones.')
for yr in ('2026','2025'):
    body += f'<h2 class="year-heading">{yr}</h2><ul class="news-list">'
    for date, info in NEWS:
        if yr in date:
            body += f'<li><time>{date}</time><span>{info}</span></li>'
    body += '</ul>'
page('News','news.html',body,'Research and academic updates about Sumera Anjum at UNT and Argonne, 2025–2026.')

# -------------------- CV --------------------
body = heading('Curriculum Vitae','Academic training, research, teaching, service, and recognition.')
body += f'''<div class="actions"><a class="btn" href="{CV_PDF}" target="_blank" rel="noopener noreferrer">View / Download CV PDF ↗</a><a class="btn btn-outline" href="publications.html">Publications →</a></div>
<p class="pdf-note">The PDF in your existing repository was last updated August 3, 2026. Replace it with your latest CV before sharing widely.</p>
<section class="section"><h2>Education</h2>'''
body += detail('PhD in Computer Science','Aug 2025–present · University of North Texas','<p>Advisor: <a href="https://yunhefeng.me/">Dr. Yunhe Feng</a> · Responsible AI Lab</p>')
body += detail('MS in Computer Science · GPA 4.0','Aug 2023–May 2025 · University of North Texas','<p>Distinguished Graduate Student Award (2024–2025).</p>')
body += detail('B.Tech in Computer Science · GPA 8.91/10','Aug 2019–May 2023 · Sreenidhi Institute of Science and Technology','<p>Hyderabad, India.</p>')
body += '</section><section class="section"><h2>Research & professional experience</h2>'
body += detail('Visiting Student · Data Science and Learning','2026 · Argonne National Laboratory','<p>Research on strategies for more cost-efficient LLM inference and API usage.</p>')
body += detail('Graduate Research Assistant · Responsible AI Lab','Aug 2023–present · University of North Texas','<p>Research on trustworthy language models, agentic AI, MCP performance, and quantum AI.</p>')
body += detail('Teaching Assistant / Instructional Assistant','2024–2026 · University of North Texas','<p>Courses include Algorithms, Foundations of Cybersecurity, and Computer Networks.</p>')
body += detail('Support Engineer Intern · Kindle Reader','Jan 2023–Jul 2023 · Amazon (AWS), Chennai','<p>Built an internal diagnostic workflow using AWS Lambda, S3, and SNS for support ticket investigation.</p>')
body += '</section><section class="section"><div class="section-header"><h2>Publications</h2><a href="publications.html" class="text-link">All publication details →</a></div>'
for p in PAPERS:
    body += f'<article class="detail-card"><h3><a href="publications.html#{p["id"]}">{escape(p["title"])}</a></h3><p class="detail-meta">{escape(p["venue"])}</p></article>'
body += '</section><section class="section"><h2>Academic service & mentorship</h2>'
body += '<p><strong>Web Chair:</strong> QISNet 2027 Workshop.</p><p><strong>Reviewing:</strong> NeurIPS 2026; IEEE GLOBECOM 2026 (CISS); ACM CIKM 2025 and 2026.</p><p><strong>Research mentoring:</strong> Undergraduate REU mentoring in quantum simulation hardware design (Summer 2026).</p></section>'
body += '''<section class="section"><h2>Awards & recognition</h2><div class="awards">
<article class="card"><p class="card-kicker">2026</p><h3>Graduate Student Travel Award</h3><p>University of North Texas</p></article>
<article class="card"><p class="card-kicker">2025</p><h3>NSF Student Travel Award</h3><p>IEEE/ACM CHASE</p></article>
<article class="card"><p class="card-kicker">2025</p><h3>Distinguished Graduate Student Award</h3><p>University of North Texas</p></article>
</div></section>'''
page('Curriculum Vitae','cv.html',body,'Online curriculum vitae of Sumera Anjum with education, experience, research, publications, service, and awards.')

# -------------------- static support files --------------------
(ROOT / 'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0d716e"/><text x="32" y="42" font-family="Georgia,serif" font-size="30" fill="#fff" font-weight="bold" text-anchor="middle">SA</text></svg>''', encoding='utf-8')
(ROOT / '.nojekyll').write_text('', encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n', encoding='utf-8')
import datetime
parts = ['<?xml version="1.0" encoding="utf-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for fname,_ in NAV:
    parts += [f'  <url><loc>{BASE}{"" if fname=="index.html" else fname}</loc></url>']
parts += ['</urlset>']
(ROOT / 'sitemap.xml').write_text('\n'.join(parts)+'\n', encoding='utf-8')
print('Generated:', ', '.join(f for f,_ in NAV))
