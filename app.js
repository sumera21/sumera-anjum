/* Accessible navigation, site search, publication filters, citation copying. */
(() => {
  'use strict';
  const menuBtn = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('#primary-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.textContent = open ? 'Close' : 'Menu';
    });
  }

  const searchable = [
    ['About Sumera Anjum', 'Home · PhD at UNT, Argonne, academic background', 'index.html'],
    ['Research overview', 'Trustworthy LLMs, agentic AI, token economics, quantum computing', 'research.html'],
    ['ProMCP', 'Six-stage profiling of MCP agents, token and latency costs, ACL 2026', 'publications.html#promcp'],
    ['Poly-FEVER', 'Multilingual factuality and hallucination detection, EMNLP 2026', 'publications.html#poly-fever'],
    ['Beyond Vibe Coding', 'Multi-framework quantum code generation, QAI 2026', 'publications.html#beyond-vibe-coding'],
    ['Quantum hardware design', 'LLM-Driven Hardware Design for Quantum Simulation Acceleration, BigData 2026', 'publications.html#quantum-hardware'],
    ['HALO', 'Clinical question answering, retrieval augmentation, CHASE 2025', 'publications.html#halo'],
    ['Projects and ongoing work', 'Argonne LLM API costs, token economics, quantum hardware', 'projects.html'],
    ['Beyond Research', 'Painting, henna, travel, cooking, languages', 'life.html'],
    ['Teaching and mentoring', 'Courses, student mentoring, REU research', 'teaching.html'],
    ['Talks and presentations', 'Token economics guest lecture, ACL ProMCP, CHASE HALO', 'talks.html'],
    ['Professional service', 'QISNet 2027 web chair, conference reviewing', 'service.html'],
    ['News', 'Academic updates 2025–2026', 'news.html'],
    ['Curriculum vitae', 'Education, research, experience, awards, downloadable PDF', 'cv.html']
  ];
  const searchDialog = document.querySelector('#site-search');
  const searchInput = document.querySelector('#site-search-input');
  const searchResults = document.querySelector('#site-search-results');
  function renderSearch(value = '') {
    if (!searchResults) return;
    const q = value.trim().toLocaleLowerCase();
    const hits = searchable.filter(([name, desc]) => (`${name} ${desc}`).toLocaleLowerCase().includes(q));
    searchResults.replaceChildren();
    if (!hits.length) {
      const p = document.createElement('p');
      p.className = 'search-hint'; p.textContent = 'No matching pages or topics.';
      searchResults.append(p); return;
    }
    for (const [name, desc, url] of hits.slice(0, 12)) {
      const a = document.createElement('a'); a.href = url; a.className = 'search-item';
      const title = document.createElement('strong'); title.textContent = name;
      const subtitle = document.createElement('span'); subtitle.textContent = desc;
      a.append(title, subtitle); searchResults.append(a);
    }
  }
  function showSearch() {
    if (!searchDialog) return;
    renderSearch('');
    if (typeof searchDialog.showModal === 'function' && !searchDialog.open) {
      searchDialog.showModal();
    } else { searchDialog.setAttribute('open', ''); }
    if (searchInput) { searchInput.value = ''; searchInput.focus(); }
  }
  document.querySelectorAll('[data-open-search]').forEach(b => b.addEventListener('click', showSearch));
  document.querySelectorAll('[data-close-search]').forEach(b => b.addEventListener('click', () => searchDialog?.close()));
  searchInput?.addEventListener('input', () => renderSearch(searchInput.value));
  searchDialog?.addEventListener('click', event => {
    if (event.target === searchDialog) searchDialog.close();
  });
  document.addEventListener('keydown', event => {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault(); showSearch();
    }
  });

  const pubSearch = document.querySelector('#publication-filter');
  const filterButtons = [...document.querySelectorAll('[data-year-filter]')];
  const pubs = [...document.querySelectorAll('[data-publication]')];
  const resultText = document.querySelector('#publication-count');
  const noResults = document.querySelector('#publication-empty');
  let yearFilter = 'all';
  function filterPubs() {
    const q = (pubSearch?.value || '').trim().toLocaleLowerCase();
    let shown = 0;
    pubs.forEach(pub => {
      const yearOK = yearFilter === 'all' || pub.dataset.year === yearFilter;
      const queryOK = (pub.dataset.search || pub.textContent).toLocaleLowerCase().includes(q);
      const visible = yearOK && queryOK;
      pub.hidden = !visible;
      if (visible) shown++;
    });
    if (resultText) resultText.textContent = `${shown} publication${shown === 1 ? '' : 's'} shown`;
    if (noResults) noResults.hidden = shown > 0;
  }
  if (pubs.length) {
    pubSearch?.addEventListener('input', filterPubs);
    filterButtons.forEach(b => b.addEventListener('click', () => {
      yearFilter = b.dataset.yearFilter;
      filterButtons.forEach(other => other.setAttribute('aria-pressed', String(b === other)));
      filterPubs();
    }));
    filterPubs();
  }

  document.querySelectorAll('[data-copy-target]').forEach(button => {
    button.addEventListener('click', async () => {
      const target = document.getElementById(button.dataset.copyTarget);
      if (!target) return;
      const citation = target.textContent.trim();
      try {
        if (navigator.clipboard?.writeText) { await navigator.clipboard.writeText(citation); }
        else {
          const tmp = document.createElement('textarea'); tmp.value = citation;
          document.body.append(tmp); tmp.select();
          const success = document.execCommand('copy'); tmp.remove();
          if (!success) throw new Error('Copy not supported');
        }
        const original = button.textContent;
        button.textContent = 'Copied ✓';
        window.setTimeout(() => { button.textContent = original; }, 1700);
      } catch (_) {
        button.textContent = 'Select text to copy';
      }
    });
  });
})();
