<script>
  let email = "";
  let password = "";

  async function login() {
    const res = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    console.log(data);
    localStorage.setItem("token", data.access_token);
  }
</script>

<form on:submit|preventDefault={login} class="space-y-2">
  <input bind:value={email} placeholder="Email" class="border p-2 w-full" />
  <input type="password" bind:value={password} placeholder="Password" class="border p-2 w-full" />
  <button class="bg-blue-500 text-white px-4 py-2">Login</button>
</form>
