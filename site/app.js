'use strict';
(() => {
  const tabs = Array.from(document.querySelectorAll('.chapter-tab'));
  const panels = tabs.map(tab => document.querySelector(tab.getAttribute('href')));
  const ids = panels.map(panel => panel.id);
  const controls = document.querySelector('.deck-controls');
  const previous = document.querySelector('#previous');
  const next = document.querySelector('#next');
  const progress = document.querySelector('#chapter-progress');
  let active = 0;
  const tablist = document.querySelector('.chapter-tabs');
  tablist.setAttribute('role', 'tablist');
  tabs.forEach((tab, index) => {
    tab.setAttribute('role', 'tab');
    tab.setAttribute('aria-controls', ids[index]);
    panels[index].setAttribute('role', 'tabpanel');
    panels[index].setAttribute('aria-labelledby', tab.id);
    panels[index].setAttribute('tabindex', '0');
  });
  function render() {
    const hash = window.location.hash.slice(1);
    active = ids.indexOf(hash);
    if (active < 0) {
      active = 0;
      // Only chapter IDs go into navigation URLs. No private draft content.
      window.history.replaceState(null, '', window.location.pathname + '#welcome');
    }
    tabs.forEach((tab, index) => {
      const selected = index === active;
      tab.setAttribute('aria-selected', String(selected));
      tab.setAttribute('tabindex', selected ? '0' : '-1');
      panels[index].hidden = !selected;
    });
    previous.disabled = active === 0;
    next.disabled = active === ids.length - 1;
    next.textContent = active < ids.length - 1 ? tabs[active + 1].textContent.trim().replace(/^\d+\s*/, '') + ' →' : 'The end';
    progress.textContent = `Chapter ${active + 1} of ${ids.length}`;
    controls.hidden = false;
  }
  function navigate(index, focusTab) {
    if (index < 0 || index >= ids.length) return;
    window.history.pushState(null, '', window.location.pathname + '#' + ids[index]);
    render();
    if (focusTab) tabs[index].focus();
    window.scrollTo({ top: 0, behavior: 'instant' });
  }
  document.addEventListener('click', event => {
    const anchor = event.target.closest('a[href^="#"]');
    if (!anchor || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (anchor.getAttribute('href') === '#main') {
      event.preventDefault();
      panels[active].focus();
      panels[active].scrollIntoView({ behavior: 'instant', block: 'start' });
      return;
    }
    const index = ids.indexOf(anchor.getAttribute('href').slice(1));
    if (index < 0) return;
    event.preventDefault();
    navigate(index, false);
    // Keep focus out of the panel that was just hidden.
    if (!anchor.matches('.chapter-tab')) tabs[index].focus();
  });
  tablist.addEventListener('keydown', event => {
    if (!event.target.matches('.chapter-tab')) return;
    let index = tabs.indexOf(event.target);
    if (event.key === 'ArrowRight') index = (index + 1) % tabs.length;
    else if (event.key === 'ArrowLeft') index = (index - 1 + tabs.length) % tabs.length;
    else if (event.key === 'Home') index = 0;
    else if (event.key === 'End') index = tabs.length - 1;
    else if (event.key === ' ') { event.preventDefault(); navigate(index, true); return; }
    else return;
    event.preventDefault();
    navigate(index, true);
  });
  previous.addEventListener('click', () => navigate(active - 1, true));
  next.addEventListener('click', () => navigate(active + 1, true));
  window.addEventListener('popstate', render);
  window.addEventListener('hashchange', render);
  // The introduction never needs tracking parameters or shared private fragments.
  window.history.replaceState(null, '', window.location.pathname + window.location.hash);
  render();
  window.addEventListener('load', () => {
    if (panels.includes(document.activeElement)) document.activeElement.blur();
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, { once: true });

  const form = document.querySelector('#idea-form');
  const idea = document.querySelector('#idea');
  const error = document.querySelector('#idea-error');
  const output = document.querySelector('#prompt-output');
  const copyStatus = document.querySelector('#copy-status');
  form.reset();
  output.value = ''; // No persisted story notes or restored form drafts.
  const starts = {
    idea: 'I am starting with an idea. Begin with story discovery, not a full draft.',
    outline: 'I already have some characters or an outline. Ask to see what I have, then help me find the strongest direction before drafting.',
    draft: 'I already have a draft. Ask me to share it, read it before proposing changes, and identify what to protect as well as the most consequential problems.'
  };
  form.addEventListener('submit', event => {
    event.preventDefault();
    const seed = idea.value.trim();
    if (!seed) {
      error.hidden = false;
      idea.setAttribute('aria-invalid', 'true');
      idea.focus();
      return;
    }
    error.hidden = true;
    idea.removeAttribute('aria-invalid');
    const feeling = document.querySelector('#feeling').value.trim();
    const keep = document.querySelector('#keep').value.trim();
    const startingPoint = starts[document.querySelector('#starting-point').value];
    const sourceMode = document.querySelector('#source-mode').value;
    const sourceBrief = {
      original: 'Original fiction. Research factual details where needed; do not invent real-world authority.',
      'based-on': 'Based on a true story. Agree factual fidelity before outlining. Use Story Factory research, with optional native helpers only when enabled, maintain a claim and source ledger, distinguish supported facts from disputes and invention, and audit the final draft with story-truth. Do not claim rights clearance.',
      'inspired-by': 'Inspired by a true story. Agree the boundary between real events and fictional invention. Use Story Factory research, with optional native helpers only when enabled, record source claims and deliberate departures separately, and audit the final draft and its truth label. Do not imply invented events really happened.'
    }[sourceMode];
    const scope = document.querySelector('#package-scope').value;
    const selected = Array.from(document.querySelectorAll('input[name="component"]:checked'));
    const packageBrief = scope === 'complete'
      ? 'I want the complete screenplay, all 15 studio sections, and all 16 reader-specific pitches. Confirm the scope before drafting.'
      : scope === 'custom'
        ? selected.length
          ? 'Create only these selected deliverables: ' + selected.map(item => item.dataset.label).join('; ') + '. Configure development/package_options.json to match. Everything else is optional and unselected; do not fill it merely to complete a template.'
          : 'I chose a custom package but have not selected any deliverables yet. Help me choose at least one before creating presentation materials. Do not assume a full package.'
        : 'Help me choose the deliverables later based on the reader. Every studio section and pitch is optional; do not assume I need the complete package.';
    const swarmMode = document.querySelector('#swarm-mode').value;
    const swarmTasks = Array.from(document.querySelectorAll('input[name="swarm-task"]:checked')).map(item => item.value);
    const swarmBrief = swarmMode === 'off'
      ? 'Parallel helpers are OFF. Work sequentially; do not spawn subagents.'
      : (swarmMode === 'ask' ? 'Ask me before starting native parallel helpers.' : 'Native parallel helpers may run automatically within the following limits.')
        + ' First verify actual native capability and current account/plan limits. Maximum concurrent helpers: ' + document.querySelector('#swarm-workers').value
        + '. Permitted tasks: ' + (swarmTasks.join(', ') || 'none; ask me to choose before spawning')
        + '. Keep one coordinating author. Helpers return evidence and findings; do not allow simultaneous screenplay edits. Do not add paid providers, API keys, or external model services. If unavailable, work sequentially and disclose it.';
    output.value = `I want to develop a film story with you using the Story Factory approach. Be a thoughtful writing partner and an honest story editor. I stay the author; help me make deliberate choices rather than quietly deciding everything for me.\n\nMY STARTING IDEA\n${seed}\n\n${feeling ? 'HOW IT SHOULD FEEL\n' + feeling + '\n\n' : ''}${keep ? 'WHAT TO KEEP OR AVOID\n' + keep + '\n\n' : ''}WHERE I AM STARTING\n${startingPoint}\n\nSOURCE AND TRUTH\n${sourceBrief}\n\nMY DELIVERABLES\n${packageBrief}\n\nPARALLEL HELPERS\n${swarmBrief}\n\nHOW WE WILL WORK\n1. Ask one useful question at a time. Find the person, the want, the obstacle, and the reason we should care. Do not ask questions I have already answered.\n2. Explore genuinely different directions when helpful, explain your recommendation, and let me choose the important creative commitments.\n3. Develop characters with their own wants and an outline where choices lead to consequences.\n4. Write real scenes in manageable sections. Keep the tone specific to this story.\n5. Review the full draft honestly. Name the biggest problems with scene evidence, protect what works, and repair structure before polishing lines. Check character agency, continuity, tone, and production feasibility. Assess the named-women Bechdel test with actual exchanges; it is a narrow diagnostic, not a quality guarantee. Offer studio notes as choices and apply only changes I accept.\n6. When ready, help me make a synopsis and pitches that describe the story we actually wrote. Do not invent attachments, professional approval, or financial certainty.\n7. Keep track of decisions and give me a short handoff when we stop so I can continue later.\n\nCheck important facts and rights questions for real-world material. Tell me when you are making an assumption. Do not publish or send my work without my explicit permission.\n\nStart with the single question that will help this story most.`;
    document.querySelector('#prompt-empty').hidden = true;
    document.querySelector('#prompt-result').hidden = false;
    copyStatus.textContent = '';
    document.querySelector('#result-heading').focus();
    document.querySelector('#prompt-room').scrollIntoView({ behavior: 'instant', block: 'start' });
  });
  document.querySelectorAll('input[name="component"]').forEach(input => {
    input.addEventListener('change', () => { document.querySelector('#package-scope').value = 'custom'; });
  });
  idea.addEventListener('input' , () => {
    if (idea.value.trim()) { error.hidden = true; idea.removeAttribute('aria-invalid'); }
  });
  document.querySelector('#use-example').addEventListener('click', () => {
    idea.value = 'A retired lighthouse keeper starts receiving letters from ships that disappeared years ago. Her estranged daughter is the only person she can ask for help.';
    document.querySelector('#feeling').value = 'Mysterious, quietly funny, and unexpectedly tender.';
    document.querySelector('#keep').value = 'The daughter should have a life and a story of her own. No easy reunion.';
    document.querySelector('#starting-point').value = 'idea';
    error.hidden = true;
    idea.removeAttribute('aria-invalid');
    idea.focus();
  });
  document.querySelector('#copy-prompt').addEventListener('click', async () => {
    try {
      if (!navigator.clipboard) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(output.value);
      copyStatus.textContent = 'Copied. Open your AI assistant and paste it into a new conversation.';
    } catch (_) {
      output.focus();
      output.select();
      copyStatus.textContent = 'Your browser could not copy automatically. The prompt is selected: use Copy, or save it as a text file.';
    }
  });
  document.querySelector('#download-prompt').addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob([output.value], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = 'my-story-factory-prompt.txt';
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    copyStatus.textContent = 'Your text file is ready. Keep a copy with your story notes.';
  });
})();
