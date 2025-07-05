<script>
  import { onMount } from "svelte";
  let issues = [];

  async function fetchIssues() {
    const res = await fetch("http://localhost:8000/issues");
    issues = await res.json();
  }

  onMount(() => {
    fetchIssues();
    const interval = setInterval(fetchIssues, 15000);
    return () => clearInterval(interval);
  });
</script>

<h2 class="text-xl font-bold mb-2">Issues</h2>
<ul>
  {#each issues as issue}
    <li>{issue.title} — {issue.status}</li>
  {/each}
</ul>
