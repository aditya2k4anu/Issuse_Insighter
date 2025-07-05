<script>
  let stats = [];

  async function loadStats() {
    const res = await fetch("http://localhost:8000/stats");
    stats = await res.json();
  }

  loadStats();
</script>

<h2 class="text-xl font-bold mb-2">Dashboard</h2>
<ul>
  {#each stats as stat}
    <li>{stat.status}: {stat.count}</li>
  {/each}
</ul>
