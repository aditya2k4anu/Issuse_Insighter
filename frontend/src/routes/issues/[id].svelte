<script>
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  let issue = {};
  $: id = $page.params.id;

  async function fetchIssue() {
    const res = await fetch(`http://localhost:8000/issues/${id}`);
    issue = await res.json();
  }

  onMount(fetchIssue);
</script>

<h2 class="text-xl font-bold">{issue.title}</h2>
<p>{issue.description}</p>
<p>Status: {issue.status}</p>

{#if issue.file_path}
  {#if issue.file_path.endsWith(".pdf")}
    <iframe src={issue.file_path} width="100%" height="600px"></iframe>
  {:else}
    <img src={issue.file_path} alt="Attachment" />
  {/if}
{/if}
